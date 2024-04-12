#ifndef __MAG_SERVICE_SERVICE_H__
#define __MAG_SERVICE_SERVICE_H__

#include "mbed-os/connectivity/FEATURE_BLE/include/ble/BLE.h"
#include "mbed-os/connectivity/FEATURE_BLE/include/ble/Gap.h"
#include "mbed-os/connectivity/FEATURE_BLE/include/ble/GattServer.h"
#include "mbed-os/connectivity/FEATURE_BLE/include/ble/gatt/GattCharacteristic.h"

class MagService
{
public:
  // const static uint16_t MAG_SERVICE_UUID = 0xA000;
  // const static uint16_t MAG_STATE_CHARACTERISTIC_UUID = 0xA001;
  MagService(BLE &_ble, int16_t *magData) : ble(_ble), valueBytes(magData), hrmMag(0xA4B6, valueBytes.getPointer(), valueBytes.getNumValueBytes(), MagValueBytes::MAX_VALUE_BYTES, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY | GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_INDICATE | GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_READ | GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_WRITE, nullptr, 0, true) { setupService(); }

  void updateMagData(int16_t *magData)
  {

    valueBytes.updateMagData(magData);
    ble.gattServer().write(hrmMag.getValueHandle(), valueBytes.getPointer(), 6);
  }

protected:
  /**
   * Construct and add to the GattServer the heart rate service.
   */
  void setupService()
  {
    GattCharacteristic *charTable[] = {
        &hrmMag};
    GattService hrmService(
        0x5634,
        charTable,
        sizeof(charTable) / sizeof(charTable[0]));

    ble.gattServer().addService(hrmService);
  }

protected:
  struct MagValueBytes
  {
    static const unsigned MAX_VALUE_BYTES = 6;

    MagValueBytes(int16_t *magData) : valueBytes()
    {
      updateMagData(magData);
    }

    void updateMagData(int16_t *magData) // valueBytes[0] = magData[0];
                                         // valueBytes[1] = magData[1];
                                         // valueBytes[2] = magData[2];
    {
      // valueBytes[0] = magData[0];
      // valueBytes[1] = magData[1];
      // valueBytes[2] = magData[2];

      for (int i = 0; i < 3; ++i)
      {
        valueBytes[2 * i] = static_cast<int8_t>((magData[i] >> 8) & 0xFF); // Higher 8 bits
        valueBytes[2 * i + 1] = static_cast<int8_t>(magData[i] & 0xFF);    // Lower 8 bits
      }
    }

    uint8_t *getPointer()
    {
      return valueBytes;
    }

    unsigned getNumValueBytes()
    {
      return MAX_VALUE_BYTES;
    }

  private:
    uint8_t valueBytes[MAX_VALUE_BYTES];
  };

protected:
  BLE &ble;
  GattCharacteristic hrmMag;
  MagValueBytes valueBytes;
};

#endif /*__MAG_SERVICE_SERVICE_H__*/