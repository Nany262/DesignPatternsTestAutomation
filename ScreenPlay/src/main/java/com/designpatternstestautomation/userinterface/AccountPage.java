package com.designpatternstestautomation.userinterface;

import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.screenplay.targets.Target;

public class AccountPage extends PageObject {
    public static final Target LABEL_ACCOUNT = Target.the("Label Account")
            .locatedBy("//*[contains(text(),'Welcome to your account')]");

}
