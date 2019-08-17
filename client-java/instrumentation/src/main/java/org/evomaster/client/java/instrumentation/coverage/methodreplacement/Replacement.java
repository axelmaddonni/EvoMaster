package org.evomaster.client.java.instrumentation.coverage.methodreplacement;

import org.evomaster.client.java.instrumentation.ObjectiveNaming;
import org.evomaster.client.java.instrumentation.staticstate.ObjectiveRecorder;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * Mark a static method as a replacement one for a method in the Java API.
 * As boolean values and exceptions lead to fitness plateaus, we need testability
 * transformations to give gradient, eg by creating new coverage targets,
 * in which we want to return true and false.
 * <br>
 * A {@code Replacement} method MUST have the same return type, and
 * match name/signature of replaced method, but last parameter being a
 * {@code String} id template.
 * However, if replacing a non-static method, then the replacement MUST
 * still be static, and have as first parameter the caller.
 */
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.METHOD})
public @interface Replacement {

    /**
     * Specify if the target replaced method was static
     */
    boolean replacingStatic() default false;

    enum TYPE{BOOLEAN, EXCEPTION}

    TYPE type();
}
