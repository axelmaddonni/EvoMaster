import unittest
import json
import requests
import evomaster_benchmark.ncs.em_handler


# This file was automatically generated by EvoMaster on 2021-01-19T21:22:16.768475-03:00[America/Argentina/Buenos_Aires]
#
# The generated test suite contains 7 tests
#
# Covered targets: 99
#
# Used time: 0h 0m 10s
#
# Needed budget for current results: 55%
#
# 
class EvoMasterTest(unittest.TestCase):

    
    controller = evomaster_benchmark.ncs.em_handler.EMHandler()
    
    
    @classmethod
    def setUpClass(cls):
        cls.controller.setup_for_generated_test()
        cls.test_client = cls.controller.app().test_client()
    
    
    @classmethod
    def tearDownClass(cls):
        cls.controller.stop_sut()
    
    
    def setUp(self):
        self.controller.reset_state_of_sut()
    
    
    
    
    def test_0(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/triangle/4195162/760/886",
                    headers=headers)
        assert res_0.json == json.loads("{\"resultAsInt\": 0}\n")
    
    
    def test_1(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/bessj/-3600/0.5200834946593118",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/triangle/156/543/-273",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/triangle/1787/218/357",
                    headers=headers)
        assert res_2.json == json.loads("{\"resultAsInt\": 0}\n")
    
    
    def test_2(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/triangle/858/760/886",
                    headers=headers)
        assert res_0.json == json.loads("{\"resultAsInt\": 1}\n")
    
    
    def test_3(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/bessj/699/0.22002290607426556",
                    headers=headers)
        assert res_0.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/triangle/98/215/187",
                    headers=headers)
        assert res_1.json == json.loads("{\"resultAsInt\": 1}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/bessj/989/0.4995136708789274",
                    headers=headers)
        assert res_2.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_3 = self.test_client \
                .get("/api/bessj/89/0.15643579665191532",
                    headers=headers)
        assert res_3.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_4 = self.test_client \
                .get("/api/bessj/250/0.12442479941654516",
                    headers=headers)
        assert res_4.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_5 = self.test_client \
                .get("/api/triangle/-1875877253/489/875",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_6 = self.test_client \
                .get("/api/bessj/556/0.24439926991298644",
                    headers=headers)
        assert res_6.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_7 = self.test_client \
                .get("/api/bessj/16961/0.38354870730689383",
                    headers=headers)
        assert res_7.json == json.loads("{\"message\": \"The browser (or proxy) sent a request that this server could not understand.\"}\n")
    
    
    def test_4(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/bessj/699/0.22002290607426556",
                    headers=headers)
        assert res_0.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/bessj/740/0.6769596126855836",
                    headers=headers)
        assert res_1.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/triangle/98/215/187",
                    headers=headers)
        assert res_2.json == json.loads("{\"resultAsInt\": 1}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_3 = self.test_client \
                .get("/api/bessj/989/0.4995136708789274",
                    headers=headers)
        assert res_3.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_4 = self.test_client \
                .get("/api/bessj/89/0.15643579665191532",
                    headers=headers)
        assert res_4.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_5 = self.test_client \
                .get("/api/bessj/250/0.12442479941654516",
                    headers=headers)
        assert res_5.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_6 = self.test_client \
                .get("/api/triangle/-1875877765/489/875",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_7 = self.test_client \
                .get("/api/bessj/556/0.24439926991298644",
                    headers=headers)
        assert res_7.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_8 = self.test_client \
                .get("/api/bessj/577/0.38354870730689383",
                    headers=headers)
        assert res_8.json == json.loads("{\"resultAsFloat\": -0.0}\n")
    
    
    def test_5(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/bessj/881/0.7241601465391557",
                    headers=headers)
        assert res_0.json == json.loads("{\"resultAsFloat\": -0.0}\n")
    
    
    def test_6(self):
        
        headers = {}
        headers['Accept'] = "*/*"
        res_0 = self.test_client \
                .get("/api/bessj/698/0.22002290607426556",
                    headers=headers)
        assert res_0.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_1 = self.test_client \
                .get("/api/triangle/98/215/187",
                    headers=headers)
        assert res_1.json == json.loads("{\"resultAsInt\": 1}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_2 = self.test_client \
                .get("/api/bessj/989/311061.94572452334",
                    headers=headers)
        assert res_2.json == json.loads("{\"resultAsFloat\": 0.0012581265227621635}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_3 = self.test_client \
                .get("/api/bessj/89/0.15643579665191532",
                    headers=headers)
        assert res_3.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_4 = self.test_client \
                .get("/api/triangle/-1875877253/497/-31893",
                    headers=headers)
        
        headers = {}
        headers['Accept'] = "*/*"
        res_5 = self.test_client \
                .get("/api/bessj/556/0.24439926991298644",
                    headers=headers)
        assert res_5.json == json.loads("{\"resultAsFloat\": -0.0}\n")
        
        headers = {}
        headers['Accept'] = "*/*"
        res_6 = self.test_client \
                .get("/api/bessj/14913/0.38354870730689383",
                    headers=headers)
        assert res_6.json == json.loads("{\"message\": \"The browser (or proxy) sent a request that this server could not understand.\"}\n")
