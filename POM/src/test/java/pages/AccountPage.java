package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class AccountPage {

  @FindBy(xpath = "//*[contains(text(),'Welcome to your account')]")
  public static WebElement labelAccount;

  public AccountPage(WebDriver driver) {
    PageFactory.initElements(driver, this);
  }

  public static void validateAccount() {
    labelAccount.isEnabled();
  }
}
