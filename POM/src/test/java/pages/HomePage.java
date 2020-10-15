package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class HomePage {

  @FindBy(xpath = "//*[contains(text(),'Automation Practice Website')]")
  public static WebElement labelHomePage;

  @FindBy(className = "login")
  public static WebElement buttonSignIn;

  public HomePage(WebDriver driver) {
    PageFactory.initElements(driver, this);
  }

  public static void validateLoadPage() {
    labelHomePage.isDisplayed();
  }

  public static void goToSignInPage() {
    buttonSignIn.click();
  }
}
