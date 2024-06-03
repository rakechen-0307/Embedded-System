using Windows.Devices.Bluetooth;
using Windows.Devices.Bluetooth.GenericAttributeProfile;
using Windows.Storage.Streams;
namespace GATT_Client_Win11;

class BLECommunicator
{
    private static void Characteristic_ValueChanged(GattCharacteristic sender, GattValueChangedEventArgs args)
    {
        // An Indicate or Notify reported that the value has changed.
        var reader = DataReader.FromBuffer(args.CharacteristicValue);
                        // Parse the data however required.
    }
    
    public static async void ConnectDevice(string id)
    {
        Console.WriteLine($"connecting to device id: {id}");
        // Note: BluetoothLEDevice.FromIdAsync must be called from a UI thread because it may prompt for consent.
        BluetoothLEDevice bluetoothLeDevice = await BluetoothLEDevice.FromIdAsync(id);

        GattDeviceServicesResult serviceResult = await bluetoothLeDevice.GetGattServicesAsync();

        if (serviceResult.Status != GattCommunicationStatus.Success)
        {
            Console.WriteLine("Communicator: cannot get GATT services");
            return;
        }

        var services = serviceResult.Services;
        foreach (var service in services)
        {
            // if (service.Uuid != serviceUuid) { continue; }

            GattCharacteristicsResult characterResult = await service.GetCharacteristicsAsync();
            if (characterResult.Status != GattCommunicationStatus.Success)
            {
                Console.WriteLine("Communicator: cannot get GATT characteristics");
                continue;
            }

            var characteristics = characterResult.Characteristics;
            foreach (var characteristic in characteristics)
            {
                // if (characteristic.Uuid != characteristicUuid) { continue; }
                GattCharacteristicProperties properties = characteristic.CharacteristicProperties;

                if (properties.HasFlag(GattCharacteristicProperties.Read))
                {
                    GattReadResult result = await characteristics[0].ReadValueAsync();
                    if (result.Status == GattCommunicationStatus.Success)
                    {
                        var reader = DataReader.FromBuffer(result.Value);
                        byte[] input = new byte[reader.UnconsumedBufferLength];
                        reader.ReadBytes(input);
                        // Utilize the data as needed
                        Console.WriteLine(input);
                    }
                }
            }
        }
    }
}