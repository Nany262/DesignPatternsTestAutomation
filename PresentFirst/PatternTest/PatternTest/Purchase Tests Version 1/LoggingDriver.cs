﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;

namespace PatternTest.Purchase_Tests_Version_1
{
    public class LoggingDriver : DriverDecorator
    {
        public LoggingDriver(Driver driver)
        : base(driver)
        {
        }

        public override void Start(Browser browser)
        {
            Console.WriteLine($"Start browser ? {Enum.GetName(typeof(Browser),browser)}");
            driver?.Start(browser);
        }

        public override void Quit()
        {
            Console.WriteLine("Close Browser");
            driver?.Quit();
        }

        public override void GoToUrl(string url)
        {
            Console.WriteLine($"Go to URL = {url}");
            driver?.GoToUrl(url);
        }

        public override Element FindElement(By locator)
        {
            Console.WriteLine("Find element");
            return driver?.FindElement(locator);
        }
        public override List<Element> FindElements(By locator)
        {
            Console.WriteLine("Find elements");
            return driver?.FindElements(locator);
        }
    }
}

