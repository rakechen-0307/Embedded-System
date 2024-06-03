
using System.Diagnostics;
namespace GATT_Client_Win11;

class Program
{
    static void Main(string[] args)
    {
        // PerformanceCounter cpuCounter = new PerformanceCounter("Processor", "% Processor Time", "_Total");
        
        // // initialize and discard the first value
        // _ = cpuCounter.NextValue();
        // Thread.Sleep(1000);

        // CoreAudioController audioController = new CoreAudioController();
        // CoreAudioDevice playbackDevice = audioController.DefaultPlaybackDevice;
        // Console.WriteLine("Current Volume: " + playbackDevice.Volume);
        // while (true) 
        // {
            // float[] samples = new float[5];
            // for (int i = 0; i < samples.Length; i++)
            // {
            //     samples[i] = cpuCounter.NextValue();
            //     Thread.Sleep(200); // Sample every 200ms for a total of 1 second
            // }

            // float averageCpuUsage = samples.Average();

            // // Print the average CPU usage percentage
            // Console.WriteLine("Average CPU Usage: {0}%", averageCpuUsage);

            // // Wait for a second before getting the next set of samples
            // Thread.Sleep(100);

            // playbackDevice.Volume = 0;
            // Console.WriteLine("Current Volume: " + playbackDevice.Volume);
            // Thread.Sleep(1000);
            // playbackDevice.Volume = 50;
            // Console.WriteLine("Current Volume: " + playbackDevice.Volume);
            // Thread.Sleep(1000);
        // }
        AdvertisementScanner.StartScanning();
        while (true) {}
    }
}
