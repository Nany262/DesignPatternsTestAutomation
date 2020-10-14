package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {

  @FindBy(id = "email")
  public static WebElement inputEmail;

  @FindBy(id = "passwd")
  public static WebElement inputPassword;

  @FindBy(id = "SubmitLogin")
  public static WebElement buttonSignIn;

  public LoginPage(WebDriver driver) {
    PageFactory.initElements(driver, this);
  }

  public static void writeEmail(String email) {
    inputEmail.clear();
    inputEmail.sendKeys(email);
  }

  public static void writePassword(String password) {
    inputPassword.clear();
    inputPassword.sendKeys(password);
  }

  public static void login() {
    buttonSignIn.click();
  }
}
