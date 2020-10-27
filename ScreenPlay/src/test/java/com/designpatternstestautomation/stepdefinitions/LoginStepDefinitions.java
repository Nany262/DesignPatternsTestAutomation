package com.designpatternstestautomation.stepdefinitions;

import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import net.serenitybdd.screenplay.abilities.BrowseTheWeb;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.actions.Open;
import net.serenitybdd.screenplay.actors.OnStage;
import net.serenitybdd.screenplay.actors.OnlineCast;
import net.thucydides.core.annotations.Managed;
import org.openqa.selenium.WebDriver;

import static com.designpatternstestautomation.userinterface.HomePage.LOGIN;
import static com.designpatternstestautomation.utils.constants.GeneralConstants.*;

public class LoginStepDefinitions {

    @Managed(driver = CHROME)
    protected WebDriver hisBrowser;

    @Before
    public void preparation() {
        OnStage.setTheStage(new OnlineCast());
        OnStage.theActorCalled(CLIENT_USER);
        OnStage.theActorInTheSpotlight().can(BrowseTheWeb.with(hisBrowser));
    }

    @Given("the user is on the automation practices page")
    public void theUserIsOnTheAutomationPracticesPage() {
        OnStage.theActorInTheSpotlight().wasAbleTo(Open.url(AUTOMATION_PAGE),
                Click.on(LOGIN));
    }

    @When("he logs in with his {string} and {string}")
    public void heLogsInWithHisAnd(String string, String string2) {

    }

    @Then("He will be able to view the message Welcome to your account.")
    public void heWillBeAbleToViewTheMessageWelcomeToYourAccount() {

    }

}
