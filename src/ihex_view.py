from src.base_view import BaseView
from src.helper import HexfileType


class IHexView(BaseView):
    name = "IHex"
    long_name = "Intel HEX"
    hexfile_type = HexfileType.IHEX
