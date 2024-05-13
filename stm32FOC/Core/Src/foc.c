#include "main.h"
#include "foc.h"
#include "AS5600.h"
#include "usart.h"
#include <math.h>
#include <stdlib.h>
#include <string.h>

float Ualpha, Ubeta = 0, Ua = 0, Ub = 0, Uc = 0;
float voltage_power_supply = 12;
float zero_electric_angle = 0;
int PolePair = 7;
int DIR = -1;
char msgFOC[20];

float _normalizeAngle(float angle)
{
    float a = fmod(angle, 2 * _PI);
    return a >= 0 ? a : (a + 2 * _PI);
}
float _electricalAngle(void)
{
    return _normalizeAngle((float)(DIR * PolePair) * bsp_as5600GetAngle() - zero_electric_angle);
}

void setPwm(float Ua, float Ub, float Uc)
{
    float dc_a = _constrain(Ua / voltage_power_supply, 0.0f, 1.0f);
    float dc_b = _constrain(Ub / voltage_power_supply, 0.0f, 1.0f);
    float dc_c = _constrain(Uc / voltage_power_supply, 0.0f, 1.0f);
    TIM3->CCR1 = round(dc_a * 10000);
    TIM3->CCR3 = round(dc_b * 10000);
    TIM3->CCR4 = round(dc_c * 10000);
}

void setPhaseVoltage(float Uq, float Ud, float phase_angle)
{
    Ualpha = -Uq * sin(phase_angle);
    Ubeta = Uq * cos(phase_angle);

    Ua = Ualpha + voltage_power_supply / 2;
    Ub = (sqrt(3) * Ubeta - Ualpha) / 2 + voltage_power_supply / 2;
    Uc = (-Ualpha - sqrt(3) * Ubeta) / 2 + voltage_power_supply / 2;
    setPwm(Ua, Ub, Uc);
}

void AlignSensor()
{
    setPhaseVoltage(3, 0, _3PI_2);
    HAL_Delay(2000);
    zero_electric_angle = _electricalAngle();
    sprintf(msgFOC, "Zero %f\n", zero_electric_angle);
    HAL_UART_Transmit(&huart1, (uint8_t *)msgFOC, strlen(msgFOC), HAL_MAX_DELAY);
    setPhaseVoltage(0, 0, _3PI_2);
}

float Error = 0;
float Error_last = 0;
float integral = 0;
float derivative = 0;
void ClosedLoopPosition(float _Kp, float _Ki, float _Kd, float TargetAngle)
{
    Error = TargetAngle - bsp_as5600GetWrappedAngle();
    integral += Error;
    derivative = Error - Error_last;
    float Uq = _constrain(DIR * (_Kp * Error + _Ki * integral + _Kd * derivative), -voltage_power_supply / 2, voltage_power_supply / 2);

    setPhaseVoltage(Uq, 0, _electricalAngle());
}