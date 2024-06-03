# GATT-Client-Win11
A GATT client implementation on Windows 11.

## Prerequisite
### .NET8.0
* link: https://dotnet.microsoft.com/en-us/download
* check versions: `dotnet --list-sdks`

## Run Project
`dotnet run`

## Initialize Project
This part is done already in this repo, this is only a tutorial for those who want to start a similar project from scratch. The steps avoids the trouble of failing to use Windows.Devices API.
1. Generate Project
    `dotnet new console --framework net8.0 --use-program-main`
2. Project Settings
    * modify `<TargetFramework>` in the `.csproj` file to `<TargetFramework>net8.0-windows$([Microsoft.Build.Utilities.ToolLocationHelper]::GetLatestSDKTargetPlatformVersion('Windows', '10.0'))</TargetFramework>`
    * I am not sure about the `GetLatestSDKTargetPlatformVersion('Windows', '10.0')` but 10.0 works well on Win11, while 11.0 doesn't.
3. Add Package
    * Windows Device API
        `dotnet add package Microsoft.Windows.CsWinRT --version 2.0.7`
    * Audio Core API
        `dotnet add package AudioSwitcher.AudioApi.CoreAudio --version 3.0.3`
        * Please note that the current version is not specifically designed for .NET 8.0, but it works in this scenario. If you need to use additional core audio functions that are not compatible with .NET 8.0, you may need to find alternative packages that support your requirements.
    * Performance counter
        `dotnet add package System.Diagnostics.PerformanceCounter --version 8.0.0`

## Reference
### Microsoft Introduction
https://learn.microsoft.com/en-us/windows/uwp/devices-sensors/bluetooth-low-energy-overview