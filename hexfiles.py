from .src.ihex_view import IHexView
from .src.srec_view import SrecView
from .src.ti_txt_view import TiTxtView


def register():
    IHexView.register()
    TiTxtView.register()
    SrecView.register()
