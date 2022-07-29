using System;

namespace turbo_cs
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = 1;
            var b = 2;
            var f = (a == b);
            Console.WriteLine(f ? "equal" : "not equal");
        }
    }
}
