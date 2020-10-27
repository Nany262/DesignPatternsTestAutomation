package com.designpatternstestautomation.runners;


import io.cucumber.junit.CucumberOptions;
import io.cucumber.junit.CucumberOptions.SnippetType;
import net.serenitybdd.cucumber.CucumberWithSerenity;
import org.junit.runner.RunWith;

@RunWith(CucumberWithSerenity.class)
@CucumberOptions(
        features = "src/test/resources/features/login.feature",
        glue = "com.designpatternstestautomation.stepdefinitions",
        snippets = SnippetType.CAMELCASE
)
public class LoginRunner {
}
