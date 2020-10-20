package com.designpatternstestautomation.userinterface;


import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class HomePage extends PageObject {

    public static final Target LABEL_HOME_PAGE = Target.the("Label Home Page")
            .locatedBy("//*[contains(text(),'Automation Practice Website')]");
    public static final Target LOGIN = Target.the("Login").located(By.className("login"));

}
