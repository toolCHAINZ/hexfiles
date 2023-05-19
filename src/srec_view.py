from src.base_view import BaseView
from src.helper import HexfileType


class SrecView(BaseView):
    name = "SREC"
    long_name = "Motorola S-record"
    hexfile_type = HexfileType.SREC
