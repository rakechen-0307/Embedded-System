from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import matplotlib.pyplot as plt

# plt.figure(0)
value0 = [0]*30
# plt.ylim([0, 256])
# plt.plot(value0)
# plt.draw()
# plt.pause(0.01)

# plt.figure(1)
value1 = [0]*30
# plt.ylim([0, 256])
# plt.plot(value1)
# plt.draw()
# plt.pause(0.01)

# plt.figure(2)
value2 = [0]*30
# plt.ylim([0, 256])
# plt.plot(value2)
# plt.draw()
# plt.pause(0.01)


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)


class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, chandle, data):
        print(data)
        data0 = data
        data1 = data
        data2 = data

        value0.pop(0)
        value0.append(data0)
        # plt.figure(0)
        # plt.clf()
        # plt.ylim([0, 256])
        # plt.plot(value0)
        # plt.draw()
        # plt.pause(0.01)

        value1.pop(0)
        value1.append(data1)
        # plt.figure(1)
        # plt.clf()
        # plt.ylim([0, 256])
        # plt.plot(value1)
        # plt.draw()
        # plt.pause(0.01)

        value2.pop(0)
        value2.append(data2)
        # plt.figure(2)
        # plt.clf()
        # plt.ylim([0, 256])
        # plt.plot(value2)
        # plt.draw()
        # plt.pause(0.01)


complete_local_name = "Eric Device"       # Complete Local Name of device
service_uuid = 0x5634                         # GATT service UUID
service_char_uuid = 0xA4B6     # GATT service Characteristic UUID

scanner = Scanner().withDelegate(ScanDelegate())
# scan device for 5 seconds
devices = scanner.scan(5.0)

n = 0
target_n = -1
addr = []
NotificationFlag = 0

for dev in devices:

    addr.append(dev.addr)
    for (adtype, desc, value) in dev.getScanData():

        # find device by Complete Local Name
        if (desc == "Complete Local Name" and value == complete_local_name):
            print("Found ", complete_local_name)
            target_n = n

    n += 1

print("target device number", target_n)
number = target_n

print("Connecting...")
dev = Peripheral(addr[number], 'random')
dev.setDelegate(MyDelegate())

svc = dev.getServiceByUUID(service_uuid)
ch = svc.getCharacteristics(service_char_uuid)[0]

for descriptor in ch.getDescriptors():
    if (descriptor.uuid == 0x2902):
        print("Wait for Notifications...")

        # start
        print("Client Characteristic Configuration found at uuid 0x",
              str(descriptor.uuid),
              " with handle 0x",
              format(descriptor.handle, '02X'))

        CCCD_handle = descriptor.handle

        print("Before writing to CCCD:", end="")
        print(dev.readCharacteristic(CCCD_handle))

        # set CCCD value
        dev.writeCharacteristic(
            CCCD_handle, bytes([2, 0]), withResponse=True)

        print("After writing to CCCD:", end="")
        print(dev.readCharacteristic(CCCD_handle))

        if (dev.readCharacteristic(CCCD_handle) == bytes([0, 0])):
            print("Notification is turned off")
        else:
            NotificationFlag = 1
            print("Notification is turned on")
        # end

        if (NotificationFlag == 1):
            print("Waiting for notifications")
            while True:
                if (dev.waitForNotifications(1.0)):
                    # handleNotification was called
                    print("receive new data")
                    continue
