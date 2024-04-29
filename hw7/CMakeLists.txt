cmake_minimum_required(VERSION 3.22)

#
# This file is generated only once,
# and is not re-generated if converter is called multiple times.
#
# User is free to modify the file as much as necessary
#

# Setup compiler settings
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS ON)


# Define the build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug")
endif()

# Set the project name
set(CMAKE_PROJECT_NAME DSP)

# Include toolchain file
include("cmake/gcc-arm-none-eabi.cmake")

# Enable compile command to ease indexing with e.g. clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)

# Enable CMake support for ASM and C languages
enable_language(C ASM)

# Core project settings
project(${CMAKE_PROJECT_NAME})
message("Build type: " ${CMAKE_BUILD_TYPE})

# Create an executable object type
add_executable(${CMAKE_PROJECT_NAME})

# Add STM32CubeMX generated sources
add_subdirectory(cmake/stm32cubemx)

# Link directories setup
target_link_directories(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user defined library search paths
    # Drivers/CMSIS/DSP/Lib/GCC
    # Drivers/CMSIS/DSP/Lib/ARM
)

# Add sources to executable
target_sources(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user sources here
    # Drivers/CMSIS/DSP/Source/TransformFunctions/arm_rfft_fast_f32.c
    # Drivers/CMSIS/DSP/Source/TransformFunctions/arm_rfft_fast_init_f32.c
    # Drivers/CMSIS/DSP/Source/ComplexMathFunctions/arm_cmplx_mag_f32.c
    Drivers/CMSIS/DSP/Examples/ARM/arm_fir_example/arm_fir_data.c
    Drivers/CMSIS/DSP/Examples/ARM/arm_fir_example/math_helper.c
    BSP/Drivers/BSP/B-L475E-IOT01/stm32l475e_iot01_accelero.c
    BSP/Drivers/BSP/Components/lsm6dsl/lsm6dsl.c
    BSP/Drivers/BSP/B-L475E-IOT01/stm32l475e_iot01.c
    Drivers/CMSIS/DSP/Source/FilteringFunctions/arm_fir_fast_q15.c
)

# Add include paths
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user defined include paths
    "Drivers/CMSIS/DSP/Include"
    "BSP/Drivers/BSP/B-L475E-IOT01"
    "BSP/Drivers/BSP/Components/Common"
    "BSP/Drivers/BSP/Components/lsm6dsl"
)

# Add project symbols (macros)
target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE
    # Add user defined symbols
    ARM_MATH_CM4
)

# Add linked libraries
target_link_libraries(${CMAKE_PROJECT_NAME}
    stm32cubemx

    # Add user defined libraries
    # libarm_cortexM4lf_math.a
)
