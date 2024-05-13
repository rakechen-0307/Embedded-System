#include "keyboard.h"
#include "usbd_customhid.h"
#include "main.h"
#include <string.h>

extern USBD_HandleTypeDef hUsbDeviceFS;
uint8_t hidbuffer1[17];
int VOL_UP_FLAG;
VOL_UP_FLAG = 0;
void keyboard(void)
{
    memset(hidbuffer1, 0, 17);
    hidbuffer1[0] = reportID1;
    if ((HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_13)) == 0)
    {
        HAL_Delay(100);
        if ((HAL_GPIO_ReadPin(GPIOC, GPIO_PIN_13)) == 0)
        {
            hidbuffer1[3] = 0b00000001;
        }
    }
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer1, 17);
}

uint8_t hidbuffer2[1];
void media_control(void)
{
    // 静音、播放
    hidbuffer2[0] = 0x04;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(40);
    hidbuffer2[0] = 0x00;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(1000);

    // 音量减
    hidbuffer2[0] = 0x02;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(40);
    hidbuffer2[0] = 0x00;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(1000);

    // 音量加
    hidbuffer2[0] = 0x01;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(40);
    hidbuffer2[0] = 0x00;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(1000);

    // 静音、播放
    hidbuffer2[0] = 0x04;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(40);
    hidbuffer2[0] = 0x00;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(1000);
}

void volume_control(int flag)
{
    hidbuffer2[0] = 0x00;
    if (flag == 1)
    {
        HAL_Delay(2);
        if (flag == 1)
        {
            hidbuffer2[0] = 0x01;
        }
    }
    else if (flag == -1)
    {
        HAL_Delay(2);
        if (flag == -1)
        {
            hidbuffer2[0] = 0x02;
        }
    }
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
}
void volume_down(void)
{
    hidbuffer2[0] = 0x02;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(40);
    hidbuffer2[0] = 0x00;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(1000);
}
void toggle_mute(void)
{
    hidbuffer2[0] = 0x04;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
    HAL_Delay(40);
    hidbuffer2[0] = 0x00;
    USBD_CUSTOM_HID_SendReport(&hUsbDeviceFS, hidbuffer2, 1);
}