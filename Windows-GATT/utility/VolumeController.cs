using AudioSwitcher.AudioApi.CoreAudio;

namespace GATT_Client_Win11;

class VolumeController
{
    private static CoreAudioController audioController = new CoreAudioController();
    private static CoreAudioDevice playbackDevice = audioController.DefaultPlaybackDevice;

    public static void SetVolume(int value)
    {
        playbackDevice.Volume = value;
    }
}