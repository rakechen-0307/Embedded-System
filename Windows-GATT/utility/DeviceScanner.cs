using Windows.Devices.Enumeration;
using Windows.Devices.Bluetooth;
namespace GATT_Client_Win11;

class DeviceScanner
{
    private static void DeviceWatcher_Added(DeviceWatcher watcher, DeviceInformation information)
    {
        Console.WriteLine($"Device added: {information.Name} ({information.Id})");
        if (information.Name == "Galaxy A52s 5G")
        {
            BLECommunicator.ConnectDevice(information.Id);
        }
    }
    private static void DeviceWatcher_Updated(DeviceWatcher watcher, DeviceInformationUpdate information)
    {
        Console.WriteLine($"Device updated: ({information.Id})");
    }
    private static void DeviceWatcher_Removed(DeviceWatcher watcher, DeviceInformationUpdate information)
    {
        // Console.WriteLine($"Device removed: {information.Id}");
    }
    private static void DeviceWatcher_EnumerationCompleted(DeviceWatcher watcher, Object obj)
    {
        // Console.WriteLine("Device enumeration completed.");
    }
    private static void DeviceWatcher_Stopped(DeviceWatcher watcher, Object obj)
    {
        // Console.WriteLine("Device watcher stopped.");
    }
    public static void StartScanning()
    {
        // Query for extra properties you want returned
        string[] requestedProperties = { "System.Devices.Aep.DeviceAddress", "System.Devices.Aep.IsConnected" };

        DeviceWatcher deviceWatcher =
                    DeviceInformation.CreateWatcher(
                    BluetoothLEDevice.GetDeviceSelectorFromPairingState(false),
                    requestedProperties,
                    DeviceInformationKind.AssociationEndpoint);

        // Register event handlers before starting the watcher.
        // Added, Updated and Removed are required to get all nearby devices
        deviceWatcher.Added += DeviceWatcher_Added;
        deviceWatcher.Updated += DeviceWatcher_Updated;
        deviceWatcher.Removed += DeviceWatcher_Removed;

        // EnumerationCompleted and Stopped are optional to implement.
        deviceWatcher.EnumerationCompleted += DeviceWatcher_EnumerationCompleted;
        deviceWatcher.Stopped += DeviceWatcher_Stopped;

        // Start the watcher.
        deviceWatcher.Start();
    }
    
}