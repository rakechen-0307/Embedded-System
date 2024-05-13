#include "main.h"
#include "usart.h"
#include "i2c.h"
#include "AS5600.h"
#define _PI 3.14159265359f
#define abs(x) ((x) > 0 ? (x) : -(x))

static int16_t angle_data_prev;
static int16_t full_rotation_offset;

void bsp_as5600Init(void)
{
    full_rotation_offset = 0;
    angle_data_prev = bsp_as5600GetRawAngle();
}

static int i2cWrite(uint8_t dev_addr, uint8_t *pData, uint32_t count)
{
    int status;
    int i2c_time_out = I2C_TIME_OUT_BASE + count * I2C_TIME_OUT_BYTE;

    status = HAL_I2C_Master_Transmit(&AS5600_I2C_HANDLE, dev_addr, pData, count, i2c_time_out);
    return status;
}

static int i2cRead(uint8_t dev_addr, uint8_t *pData, uint32_t count)
{
    int status;
    int i2c_time_out = I2C_TIME_OUT_BASE + count * I2C_TIME_OUT_BYTE;

    status = HAL_I2C_Master_Receive(&AS5600_I2C_HANDLE, (dev_addr | 1), pData, count, i2c_time_out);
    return status;
}

int16_t bsp_as5600GetRawAngle(void)
{
    int16_t raw_angle;
    uint8_t buffer[2] = {0};
    uint8_t raw_angle_register = AS5600_RAW_ANGLE_REGISTER;

    i2cWrite(AS5600_ADDR, &raw_angle_register, 1);
    i2cRead(AS5600_ADDR, buffer, 2);
    raw_angle = ((uint16_t)buffer[0] << 8) | (uint16_t)buffer[1];
    return raw_angle;
}

int16_t bsp_as5600GetWrappedRawAngle(void)
{
    int16_t angle_data = bsp_as5600GetRawAngle();
    int16_t d_angle = angle_data - angle_data_prev;
    if ((float)abs(d_angle) > (float)(0.8 * AS5600_RESOLUTION))
    {
        full_rotation_offset += (d_angle > 0 ? -1 : 1);
    }
    angle_data_prev = angle_data;

    return (int16_t)(full_rotation_offset * AS5600_RESOLUTION + angle_data);
}

float bsp_as5600GetAngle(void)
{
    return (float)bsp_as5600GetRawAngle() * 2 * _PI / AS5600_RESOLUTION;
}
float bsp_as5600GetWrappedAngle(void)
{
    return (float)bsp_as5600GetWrappedRawAngle() * 2 * _PI / AS5600_RESOLUTION;
}
