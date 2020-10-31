using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Edge;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

namespace PatternTest.Purchase_Tests_Version_1
{
    public class WebDriver : Driver
    {
        private IWebDriver _webDriver;
        private WebDriverWait _webDriverWait;

        public override void Start(Browser browser)
        {
            switch (browser)
            {
                case Browser.Chrome:
                    _webDriver = new ChromeDriver(Environment.CurrentDirectory);
                    break;

                case Browser.Firefox:
                    _webDriver = new FirefoxDriver(Environment.CurrentDirectory);
                    break;

                case Browser.Edge:
                    _webDriver = new EdgeDriver(Environment.CurrentDirectory);
                    break;

                default:
                    throw new ArgumentOutOfRangeException(nameof(browser),browser,null);
            }
            _webDriverWait = new WebDriverWait(_webDriver,TimeSpan.FromSeconds(30));
            _webDriverWait.IgnoreExceptionTypes(typeof(NoSuchElementException));
            _webDriverWait.IgnoreExceptionTypes(typeof(WebDriverException));
        }

        public override void Quit()
        {
            _webDriver.Quit();
        }

        public override void GoToUrl(string url)
        {
            _webDriver.Navigate().GoToUrl(url);
        }

        public override Element FindElement(By locator)
        {
            IWebElement nativeWebElement=_webDriverWait.Until(drv=>drv.FindElement(locator));
            Element element = new WebElement(_webDriver, nativeWebElement, locator);

            //if we use log decorator
            LogElement logElement = new LogElement(element);

            return logElement;
        }

        public override List<Element> FindElements(By locator)
        {
            ReadOnlyCollection<IWebElement> nativeWebElements = _webDriverWait.Until(drv => drv.FindElements(locator));
            List<Element> elements = new List<Element>();
            foreach (var nativeWebElement in nativeWebElements)
            {
                Element element = new WebElement(_webDriver, nativeWebElement, locator);
                elements.Add(element);
            }
            return elements;
        }
    }
}
