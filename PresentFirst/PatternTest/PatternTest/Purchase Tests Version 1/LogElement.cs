using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;

namespace PatternTest.Purchase_Tests_Version_1
{
    public class LogElement : ElementDecorator
    {
        public LogElement(Element element)
            : base(element)
        {

        }
        public override By By
        {
            get
            {
                return By;
            }
        }
        public override string Text
        {
            get
            {
                return element?.Text;
            }
        }
        public override bool? Displayed
        {
            get
            {
                return element?.Displayed;
            }
        }
        public override bool? Enabled 
        {
            get
            {
                return element?.Enabled;
            }
        }
        public override string GetAttribute(string attributeName)
        {
            return element?.GetAttribute(attributeName);
        }
        public override void TypeText(string text)
        {
             element?.TypeText(text);
        }
    }
}
