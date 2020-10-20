package com.designpatternstestautomation.userinterface;

import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class LoginPage extends PageObject {
  public static final Target INPUT_EMAIL = Target.the("Input Email").located(By.id("email"));
  public static final Target INPUT_PASSWORD = Target.the("Input Password").located(By.id("passwd"));
  public static final Target BUTTON_SIGNIN = Target.the("Button SignIn").located(By.id("SubmitLogin"));

}
