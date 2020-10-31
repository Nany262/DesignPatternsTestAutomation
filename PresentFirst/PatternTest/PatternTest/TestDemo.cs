using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;
using OpenQA.Selenium;

namespace PatternTest
{
    class TestDemo
    {
        IWebDriver driver;
        IWebDriver m_driver;

        [SetUp]
        public void startBrowser()
        {
            driver = new ChromeDriver("C:\\Users\\acer\\Desktop\\DesignPatternsTestAutomation\\DesignPatternsTestAutomation\\PresentFirst\\PatternTest\\drivers\\chromdriver.exe");
        }

        [Test]
        public void test()
        {
            driver.Url = "http://www.google.com";
        }

        [Test]
        public void cssDemo()
        {
            driver = new ChromeDriver("C:\\Users\\acer\\Desktop\\DesignPatternsTestAutomation\\DesignPatternsTestAutomation\\PresentFirst\\PatternTest\\drivers\\chromdriver.exe");
            m_driver.Url = "http://demo.guru99.com/test/guru99home/";
            m_driver.Manage().Window.Maximize();
            IWebelement link = m_driver.FindElement(By.XPath(".//*[@id='rt-header']//div[2]/div/ul/li[2]/a"));
            link.Click();
            m_driver.Close();
        }
    
        [TearDown]
        public void closeBrowser()
        {
            driver.Close();
        }
    }
}
