# STM32-ST7789

## Library Source Code

https://github.com/deividAlfa/ST7789-STM32-uGUI

The libraries are located in `./Drivers/LCD` and `./Drivers/UGUI`

## Pinout

- GND: GND
- VCC: 3.3V
- SCL: PA5(ARD_D13)
- SDA: PA7(ARD_D11)
- RES: PB2(ARD_D8)
- DC: PA15(ARD_D9)
- CS: PA2(ARD_D10)
- BLO: 3.3V

## Usage

In `./Core/Src/main.c`

- Include the needed libraries

```
/* USER CODE BEGIN Includes */

#include "ugui.h"
#include "lcd.h"

/* USER CODE END Includes */
```

- Include neccesary fonts

```
/* USER CODE BEGIN PD */

#define DEFAULT_FONT FONT_32X53

/* USER CODE END PD */
```

- Init the LCD driver

```
/* USER CODE BEGIN 2 */

LCD_init();

/* USER CODE END 2 */
```

- Run the example code for testing

```
  /* USER CODE BEGIN WHILE */

  while (1)
  {
	  UG_FillScreen(C_BLACK);
	  UG_FillFrame(70, 150, 170, 210, C_BLACK);
	  LCD_PutStr(120-32, 150, "80", DEFAULT_FONT, C_WHITE, C_BLACK);
	  UG_DrawDashboard(120, 150, 100, 90, 0, 80, C_YELLOW);
	  HAL_Delay(1000);
	  UG_FillFrame(70, 150, 170, 210, C_BLACK);
	  LCD_PutStr(120-32, 150, "60", DEFAULT_FONT, C_WHITE, C_BLACK);
	  UG_DrawDashboard(120, 150, 100, 90, 80, 60, C_BLACK);
	  HAL_Delay(1000);
	  UG_FillFrame(70, 150, 170, 210, C_BLACK);
	  LCD_PutStr(120-48, 150, "100", DEFAULT_FONT, C_WHITE, C_BLACK);
	  UG_DrawDashboard(120, 150, 100, 90, 60, 100, C_YELLOW);
	  HAL_Delay(1000);
	  UG_FillFrame(70, 150, 170, 210, C_BLACK);
	  LCD_PutStr(120-32, 150, "20", DEFAULT_FONT, C_WHITE, C_BLACK);
	  UG_DrawDashboard(120, 150, 100, 90, 100, 20, C_BLACK);
	  HAL_Delay(1000);

    /* USER CODE END WHILE */
  }
```
