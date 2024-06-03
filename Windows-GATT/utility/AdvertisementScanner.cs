using Windows.Devices.Bluetooth;
using Windows.Devices.Bluetooth.Advertisement;
namespace GATT_Client_Win11;

public class AdvertisementScanner
{
    private static async void ConnectDevice(ulong addr)
    {
        Console.WriteLine($"connecting to device addr: {addr}");
        // Note: BluetoothLEDevice.FromIdAsync must be called from a UI thread because it may prompt for consent.
        BluetoothLEDevice bluetoothLeDevice = await BluetoothLEDevice.FromBluetoothAddressAsync(addr);
        Console.WriteLine("connection success");
        GetBLEData.GetData(bluetoothLeDevice);
    }
    private static void OnAdvertisementReceived(BluetoothLEAdvertisementWatcher watcher, BluetoothLEAdvertisementReceivedEventArgs eventArgs)
    {
        // Retrieve advertisement data
        var localName = eventArgs.Advertisement.LocalName;
        var address = eventArgs.BluetoothAddress;
        var rssi = eventArgs.RawSignalStrengthInDBm;
        // Print the result
        Console.WriteLine($"Device: {localName}, Address: {address}, RSSI: {rssi} dBm");
        if (localName == "STM32")
        {
            ConnectDevice(address);
            watcher.Received -= OnAdvertisementReceived;
        }
    }
    public static void StartScanning()
    {
        BluetoothLEAdvertisementWatcher watcher = new BluetoothLEAdvertisementWatcher();
        watcher.Received += OnAdvertisementReceived;
        watcher.Start();
        Console.WriteLine("BLE Start Scanning ...");
    }
}