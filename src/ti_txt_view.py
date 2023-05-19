from src.base_view import BaseView
from src.helper import HexfileType


class TiTxtView(BaseView):
    name = "TI_TXT"
    long_name = "Texas Instruments TXT"
    hexfile_type = HexfileType.TI_TXT
