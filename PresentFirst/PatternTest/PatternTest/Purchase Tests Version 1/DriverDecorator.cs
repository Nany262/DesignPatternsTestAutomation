﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;

namespace PatternTest.Purchase_Tests_Version_1
{
    public class DriverDecorator : Driver
    {
        protected Driver driver;

        public DriverDecorator(Driver driver)
        {
            this.driver = driver;
        }

        public override void Start(Browser browser)
        {
            driver?.Start(browser);
        }

        public override void Quit()
        {
            driver?.Quit();
        }

        public override void GoToUrl(string url)
        {
            driver?.GoToUrl(url);
        }

        public override Element FindElement(By locator)
        {
            return driver?.FindElement(locator);
        }
        public override List<Element> FindElements(By locator)
        {
            return driver?.FindElements(locator);
        }
    }
}
