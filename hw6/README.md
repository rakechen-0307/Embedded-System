# Embedded System HW2 (Group 8)

This code setups DMA to transfer audio data from `DFSDM` to `Buf_Mic0`. When the top and bottom half of `Buf_Mic0` are filled, the corresponding interrupts will generate.

We choose LED1 and LED2 pin as the `Buf_Mic0` half-full and full callback toggle pin. We chose `TIM6` as the timer to trigger the `DFSDM` conversion.

`TIM6` invoke `HAL_TIM_PeriodElapsedCallback` every 2s. In the callback, we toggle `LED3/4`. Each time `LED3/4` is HIGH we enable the `DFSDM` conversion. The `DFSDM` conversion will fill the `Buf_Mic0` with audio data. When the top and bottom half of `Buf_Mic0` are filled, the corresponding interrupts will generate. In the interrupt, we toggle `LED1`, the same happends for the top half.
## How to use
1. Clone the repository

```bash
git clone git@github.com:rakechen-0307/Embedded-System.git
```

2. Change the directory to the build directory

```bash
cd hw6/build
```
3. Compile the code

```bash
cmake ..
cmake --build .
```
4. Flash the following .elf file to the board

```bash
./hw6/build/audio2.elf
```