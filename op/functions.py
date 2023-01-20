import os
from ctypes import cast, POINTER

from comtypes import CLSCTX_ALL
from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.utils import AudioUtilities

import config
from op import helpers


def handle_hello() -> dict:
    return {
        "uid": config.uid,
        "names": config.names,
        "info": {
            "mac": helpers.get_mac_address(),
        }
    }


def handle_os_system(command: str):
    os.system(command)


def handle_set_volume(percent: int):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(percent / 100, None)
        devices.Release()
    except:
        pass


def handle_get_volume():
    result = 0

    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        result = int(round(volume.GetMasterVolumeLevelScalar() * 100))
        devices.Release()
    except:
        pass

    return {
        "value": result
    }


def handle_set_mute(mute: bool):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(int(mute), None)
        devices.Release()
    except:
        pass


def handle_get_mute():
    result = False

    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        result = bool(volume.GetMute())
        devices.Release()
    except:
        pass

    return {
        "value": result
    }
