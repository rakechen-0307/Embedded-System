using System.Text;
using Windows.Devices.Bluetooth;
using Windows.Devices.Bluetooth.GenericAttributeProfile;
using Windows.Storage.Streams;
namespace GATT_Client_Win11;

class GetBLEData
{
    private static GattDeviceService? gattService;
    private static GattCharacteristic? gattCharacteristic;
    private static int ExtractValue(string str)
    {
        str = str.Trim(new char[] { '{', '}' });
        string[] split_str = str.Split(':');
        str = split_str[1].Trim(new char[] { '"', ' ' });
        str = str.TrimStart('+');
        return int.Parse(str);
    }
    private static void Characteristic_ValueChanged(GattCharacteristic sender, GattValueChangedEventArgs args)
    {
        Console.WriteLine("notified");
        // An Indicate or Notify reported that the value has changed.
        var reader = DataReader.FromBuffer(args.CharacteristicValue);
        byte[] input = new byte[reader.UnconsumedBufferLength];
        reader.ReadBytes(input);
        string str = Encoding.ASCII.GetString(input);
        Console.WriteLine($"receive: {str}");
        int angleValue = ExtractValue(str);
        Console.WriteLine($"Extracted value: {angleValue}");
        VolumeController.SetVolume(angleValue);
    }
    public static async void GetData(BluetoothLEDevice bluetoothLeDevice)
    {
        Guid serviceUuid = new Guid("00055005-0000-0000-0001-000000000000");
        Guid characteristicUuid = new Guid("00055000-0000-0000-0003-000000000001");

        GattDeviceServicesResult serviceResult = await bluetoothLeDevice.GetGattServicesAsync();
        
        switch (serviceResult.Status)
        {
            case GattCommunicationStatus.Success: 
                Console.WriteLine("Communicator: Success");
                break;
            case GattCommunicationStatus.AccessDenied:
                Console.WriteLine("Communicator: AccessDenied");
                break;
            case GattCommunicationStatus.Unreachable:
                Console.WriteLine("Communicator: Unreachable");
                break;
            default:
            case GattCommunicationStatus.ProtocolError:
                Console.WriteLine("Communicator: ProtocolError");
                break;
        }
        if (serviceResult.Status != GattCommunicationStatus.Success)
        {
            Console.WriteLine("Communicator: cannot get GATT services");
            GetData(bluetoothLeDevice);
            return;
        }

        var services = serviceResult.Services;
        foreach (var service in services)
        {
            Console.WriteLine($"service uuid {service.Uuid}");
            if (service.Uuid != serviceUuid) { continue; }
            gattService = service;
            Console.WriteLine($"service get");

            GattCharacteristicsResult characterResult = await gattService.GetCharacteristicsAsync();
            if (characterResult.Status != GattCommunicationStatus.Success)
            {
                Console.WriteLine("Communicator: cannot get GATT characteristics");
                continue;
            }

            var characteristics = characterResult.Characteristics;
            foreach (var characteristic in characteristics)
            {
                Console.WriteLine($"characteristic uuid {characteristic.Uuid}");
                if (characteristic.Uuid != characteristicUuid) { continue; }
                gattCharacteristic = characteristic;
                Console.WriteLine("Charateristic get");
                GattCharacteristicProperties properties = gattCharacteristic.CharacteristicProperties;

                if (properties.HasFlag(GattCharacteristicProperties.Notify))
                {
                    GattCommunicationStatus status = await characteristic.WriteClientCharacteristicConfigurationDescriptorAsync(
                        GattClientCharacteristicConfigurationDescriptorValue.Notify);
                    if (status == GattCommunicationStatus.Success)
                    {
                        characteristic.ValueChanged += Characteristic_ValueChanged;
                    }
                }
            }
        }
    }
}