
namespace GATT_Client_Win11;

class Program
{
    static void Main(string[] args)
    {
        if(args.Length == 0)
        {
            AdvertisementScanner.StartScanning();
            while (true) {}
        }
        else if (args.Length == 1 && args[0].Equals("CPU"))
        {
            float cpu_usage = 0;
            CPUUsage.Init();
            while (true)
            {
                cpu_usage = CPUUsage.GetUsage();
                Console.WriteLine($"CPU Usage: {cpu_usage}%");
                Thread.Sleep(100);
            }
        }
        else
        {
            Console.WriteLine("Warning: Unknown option, program terminated.");
        }
    }
}
