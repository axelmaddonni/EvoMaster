package org.evomaster.client.java.controller.db;

import io.restassured.http.ContentType;
import org.evomaster.client.java.controller.DatabaseTestTemplate;
import org.evomaster.client.java.controller.InstrumentedSutStarter;
import org.evomaster.client.java.controller.api.dto.database.operations.DatabaseCommandDto;
import org.evomaster.client.java.controller.api.dto.database.operations.InsertionDto;
import org.junit.jupiter.api.Test;

import java.util.List;

import static io.restassured.RestAssured.given;
import static org.evomaster.client.java.controller.api.ControllerConstants.BASE_PATH;
import static org.evomaster.client.java.controller.api.ControllerConstants.DATABASE_COMMAND;
import static org.evomaster.client.java.controller.db.dsl.SqlDsl.sql;
import static org.junit.jupiter.api.Assertions.*;

public class SqlScriptRunnerTest extends DatabaseTestTemplate {

    @Test
    public void testSimpleRemoteExecution() throws Exception {

        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(x INT);");

        int value = 42;

        String sql = "INSERT INTO Foo (x) VALUES (" + value + ")";
        executeViaRest(sql);

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(1, res.seeRows().size());
        assertEquals(value, res.seeRows().get(0).getValueByName("x"));
    }


    @Test
    public void testInsertWhenIdentity() throws Exception {

        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(" +
                "  id bigint generated by default as identity " +
                ", x integer " +
                ");"
        );

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(0, res.seeRows().size());

        int value = 42;

        SqlScriptRunner.execCommand(getConnection(), "INSERT INTO Foo (x) VALUES (" + value + ")");

        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(1, res.seeRows().size());
        assertEquals(value, res.seeRows().get(0).getValueByName("x"));
        assertNotNull(res.seeRows().get(0).getValueByName("id"));
    }


    @Test
    public void testTwoInsertionsWhenIdentity() throws Exception {

        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(" +
                "  id bigint generated by default as identity " +
                ", x integer " +
                ");"
        );

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(0, res.seeRows().size());

        int a = 42;
        int b = 66;

        SqlScriptRunner.execCommand(getConnection(), "INSERT INTO Foo (x) VALUES (" + a + ")");
        SqlScriptRunner.execCommand(getConnection(), "INSERT INTO Foo (x) VALUES (" + b + ")");

        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(2, res.seeRows().size());

        assertTrue(res.seeRows().stream().anyMatch(r -> r.getValueByName("x").equals(a)));
        assertTrue(res.seeRows().stream().anyMatch(r -> r.getValueByName("x").equals(b)));
        assertEquals(2, res.seeRows().stream().map(r -> r.getValueByName("id")).distinct().count());
    }

    @Test
    public void testInsertWhenForeignKey() throws Exception {

        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(" +
                "  id bigint generated by default as identity " +
                ", barId bigint not null " +
                ");" +
                " CREATE TABLE Bar(id bigint generated by default as identity);" +
                " ALTER TABLE Foo add constraint barIdKey foreign key (barId) references Bar;\n"
        );

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Bar;");
        assertEquals(0, res.seeRows().size());

        SqlScriptRunner.execCommand(getConnection(), "INSERT INTO Bar () VALUES ()");
        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Bar;");
        assertEquals(1, res.seeRows().size());
        long id = (Long) res.seeRows().get(0).getValueByName("id");


        SqlScriptRunner.execCommand(getConnection(), "INSERT INTO Foo (barId) VALUES (" + id + ")");
        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(1, res.seeRows().size());


        assertThrows(Exception.class, () ->
                //wrong foreign key
                SqlScriptRunner.execCommand(getConnection(), "INSERT INTO Foo (barId) VALUES (-20)"));
    }

    @Test
    public void testIdentityExtractGeneratedKey() throws Exception {


        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(" +
                "  id bigint generated by default as identity " +
                ", barId bigint not null " +
                ", primary key (id) " +
                ");" +
                " CREATE TABLE Bar(" +
                " id bigint generated by default as identity " +
                ", x integer " +
                ", primary key (id));" +
                " ALTER TABLE Foo add constraint barIdKey foreign key (barId) references Bar;\n"
        );

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Bar;");
        assertEquals(0, res.seeRows().size());

        Long a = SqlScriptRunner.execInsert(getConnection(), "INSERT INTO Bar (id,x) VALUES (default,42);");
        Long b = SqlScriptRunner.execInsert(getConnection(), "INSERT INTO Bar (x) VALUES (66);");

        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Bar;");
        assertEquals(2, res.seeRows().size());

        assertNotNull(a);
        assertNotNull(b);
        assertNotEquals(a, b);

        SqlScriptRunner.execInsert(getConnection(), "INSERT INTO Foo (barId) VALUES (" + a + ")");
        SqlScriptRunner.execInsert(getConnection(), "INSERT INTO Foo (barId) VALUES (" + b + ")");
        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(2, res.seeRows().size());
    }


    @Test
    public void testInsertionListWithGeneratedKeys() throws Exception {


        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(" +
                "  id bigint generated by default as identity " +
                ", barId bigint not null " +
                ", primary key (id) " +
                ");" +
                " CREATE TABLE Bar(" +
                " id bigint generated by default as identity " +
                ", x integer " +
                ", primary key (id));" +
                " ALTER TABLE Foo add constraint barIdKey foreign key (barId) references Bar;\n"
        );

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Bar;");
        assertEquals(0, res.seeRows().size());
        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(0, res.seeRows().size());


        List<InsertionDto> insertions = sql()
                .insertInto("Bar", 0L).d("id", "default").d("x", "42").and()
                .insertInto("Bar", 1L).d("id", "default").d("x", "66").and()
                .insertInto("Foo").r("barId", 0).and()
                .insertInto("Foo").r("barId", 1).dtos();

        SqlScriptRunner.execInsert(getConnection(), insertions);

        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Bar;");
        assertEquals(2, res.seeRows().size());
        res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(2, res.seeRows().size());
    }

    @Test
    public void testTimeStamp() throws Exception {

        SqlScriptRunner.execCommand(getConnection(), "create table Foo (" +
                "id bigint generated by default as identity, " +
                "creation_time timestamp not null, " +
                "primary key (id))");

        String year = "2030";
        String timestamp = year + "-2-17T4:55:50.000Z";
        String sql = "INSERT INTO Foo (CREATION_TIME) VALUES ('" + timestamp + "')";

        SqlScriptRunner.execCommand(getConnection(), sql);

        executeViaRest(sql);

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(2, res.seeRows().size());
        assertTrue(res.seeRows().get(0).getValueByName("creation_time").toString().contains(year));
        assertTrue(res.seeRows().get(1).getValueByName("creation_time").toString().contains(year));
    }

    @Test
    public void testVarchar() throws Exception {

        SqlScriptRunner.execCommand(getConnection(), "create table Foo (" +
                "id bigint generated by default as identity, " +
                "name varchar(255) not null, " +
                "primary key (id))");

        String name = "a name";
        String sql = "INSERT INTO Foo (NAME) VALUES ('" + name + "')";

        SqlScriptRunner.execCommand(getConnection(), sql);

        executeViaRest(sql);

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(2, res.seeRows().size());
        assertEquals(name, res.seeRows().get(0).getValueByName("name"));
        assertEquals(name, res.seeRows().get(1).getValueByName("name"));
    }

    private void executeViaRest(String sql) {
        DatabaseCommandDto dto = new DatabaseCommandDto();
        dto.command = sql;

        InstrumentedSutStarter starter = getInstrumentedSutStarter();

        String url = start(starter);

        given().contentType(ContentType.JSON)
                .body(dto)
                .post(url + BASE_PATH + DATABASE_COMMAND)
                .then()
                .statusCode(200);
    }

    @Test
    public void testStringGeneWithApostrophe() throws Exception {


        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Foo(" +
                "  name VARCHAR(255) " +
                ");"
        );

        List<InsertionDto> insertions = sql()
                .insertInto("Foo", 0L).d("name", "\"'\"").dtos();

        SqlScriptRunner.execInsert(getConnection(), insertions);

        QueryResult res = SqlScriptRunner.execCommand(getConnection(), "SELECT * FROM Foo;");
        assertEquals(1, res.seeRows().size());
    }


    @Test
    public void testDoubleIndirectForeignKey() throws Exception {


        SqlScriptRunner.execCommand(getConnection(), "CREATE TABLE Table1(" +
                "  id bigserial not null, " +
                " primary key (id)" +
                ");"
                +
                "CREATE TABLE Table2(" +
                "  id int8, " +
                " primary key (id)" +
                ");"
                +
                "CREATE TABLE Table3(" +
                "  id int8, " +
                " primary key (id)" +
                ");"
                +
                "alter table Table2 " +
                "  add constraint FKTable2 foreign key (id) references Table1;"
                +
                "alter table Table3 " +
                "  add constraint FKTable3 foreign key (id) references Table2;"
        );

        List<InsertionDto> insertions = sql()
                .insertInto("Table1", 1000L)
                .and()
                .insertInto("Table2", 1001L).r("Id", 1000L, true)
                .and()
                .insertInto("Table3", 1002L).r("Id", 1001L).dtos();

        SqlScriptRunner.execInsert(getConnection(), insertions);


    }
}
