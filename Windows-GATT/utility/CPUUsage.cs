using System.Diagnostics;
namespace GATT_Client_Win11;

class CPUUsage
{
    private static PerformanceCounter cpuCounter = new PerformanceCounter();
    
    public static void Init()
    {
        cpuCounter = new PerformanceCounter("Processor", "% Processor Time", "_Total");
        // initialize and discard the first value
        _ = cpuCounter.NextValue();
        Thread.Sleep(1000);
    }
    
    public static float GetUsage()
    {
        float[] samples = new float[5];
        for (int i = 0; i < samples.Length; i++)
        {
            samples[i] = cpuCounter.NextValue();
            Thread.Sleep(200); // Sample every 200ms for a total of 1 second
        }

        float averageCpuUsage = samples.Average();
        
        return averageCpuUsage;
    }
}