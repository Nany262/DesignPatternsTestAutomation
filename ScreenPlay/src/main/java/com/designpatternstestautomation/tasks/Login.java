package com.designpatternstestautomation.tasks;

import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.actions.Enter;
import net.serenitybdd.screenplay.matchers.WebElementStateMatchers;
import net.serenitybdd.screenplay.waits.WaitUntil;

import static com.designpatternstestautomation.userinterface.LoginPage.*;


public class Login implements Task {
    private final String user;
    private final String password;

    public Login(String user, String password) {
        this.user = user;
        this.password = password;
    }

    public static Login withCredentials(String user, String password) {
        return Tasks.instrumented(Login.class, user, password);
    }

    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(WaitUntil.the(INPUT_EMAIL, WebElementStateMatchers.isVisible())
                        .forNoMoreThan(2).seconds()
                        .then(Enter.theValue(user).into(INPUT_EMAIL)),
                Enter.theValue(password).into(INPUT_PASSWORD),
                Click.on(BUTTON_SIGNIN));
    }
}
