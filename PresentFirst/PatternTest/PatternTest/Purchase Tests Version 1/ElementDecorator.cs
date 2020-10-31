using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;

namespace PatternTest.Purchase_Tests_Version_1
{
    public class ElementDecorator : Element
    {
        protected Element element;

        public ElementDecorator(Element element)
        {
            this.element = element;
        }

        public override By By => throw new NotImplementedException();

        public override string Text => throw new NotImplementedException();

        public override bool? Enabled => throw new NotImplementedException();

        public override bool? Displayed => throw new NotImplementedException();

        public override void Click()
        {
            throw new NotImplementedException();
        }

        public override string GetAttribute(string attributeName)
        {
            throw new NotImplementedException();
        }

        public override void TypeText(string text)
        {
            throw new NotImplementedException();
        }
    }
}
