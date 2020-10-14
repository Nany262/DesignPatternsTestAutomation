package test_cases;

import java.util.concurrent.TimeUnit;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import pages.AccountPage;
import pages.HomePage;
import pages.LoginPage;

public class LoginTest {

  public static WebDriver driver;
  public static HomePage homePage;
  public static LoginPage loginPage;
  public static AccountPage accountPage;

  @Before
  public void setUp() {
    if (driver == null) {
      driver = new ChromeDriver();
      homePage = new HomePage(driver);
      loginPage = new LoginPage(driver);
      accountPage = new AccountPage(driver);
      driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
      driver.get("http://automationpractice.com/index.php");
    }
  }

  @Test
  public void LoginUser() {
    HomePage.validateLoadPage();
    HomePage.goToSignInPage();
    LoginPage.writeEmail("automation.practice.dz@gmail.com");
    LoginPage.writePassword("AUTOMATION1");
    LoginPage.login();
    AccountPage.validateAccount();
  }

  @After
  public void tearDown() {
    if (driver != null) {
      driver.close();
      driver.quit();
    }
  }
}
