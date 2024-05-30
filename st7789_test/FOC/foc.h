#ifndef __FOC_H
#define __FOC_H

extern float voltage_power_supply;
extern int PolePair;
extern int DIR;

#define _constrain(amt, low, high) ((amt) < (low) ? (low) : ((amt) > (high) ? (high) : (amt)))
#define _3PI_2 4.71238898038f
#define _PI 3.14159265359f

float _electricalAngle(void);
float _normalizeAngle(float angle);
void setPwm(float Ua, float Ub, float Uc);
void AlignSensor(void);
void setPhaseVoltage(float Uq, float Ud, float angle_el);
void ClosedLoopPosition(float _Kp, float _Ki, float Kd, float TargetAngle);

#endif /* __FOC_H */