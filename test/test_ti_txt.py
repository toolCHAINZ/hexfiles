import binaryninja
from binaryninja import BinaryView
from bincopy import BinFile, is_ti_txt
from src.ti_txt_view import TiTxtView

data = """
@F000
31 40 00 03 B2 40 80 5A 20 01 D2 D3 22 00 D2 E3
21 00 3F 40 E8 FD 1F 83 FE 23 F9 3F
@FFFE
00 F0
Q
"""


def make_view() -> BinaryView:
    TiTxtView.register()
    return binaryninja.open_view(data.encode("utf8"))


def test_valid():
    b = BinFile()
    b.add_ti_txt(data)
    assert is_ti_txt(data)


def test_make_view():
    view = make_view()
    assert view.view_type == "TI-TXT"
