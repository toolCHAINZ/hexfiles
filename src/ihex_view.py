from .base_view import BaseView
from .helper import HexfileType


class IHexView(BaseView):
    name = "IHex"
    long_name = "Intel HEX"
    hexfile_type = HexfileType.IHEX
