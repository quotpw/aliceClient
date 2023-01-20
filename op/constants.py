from .functions import *
from . import OP

OP_TO_FUNCTION = {
    OP.HELLO: handle_hello,
    OP.OS_SYSTEM: handle_os_system,
    OP.SET_VOLUME: handle_set_volume,
    OP.GET_VOLUME: handle_get_volume,
    OP.SET_MUTE: handle_set_mute,
    OP.GET_MUTE: handle_get_mute,
}
