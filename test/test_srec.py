import binaryninja
from binaryninja import BinaryView
from bincopy import is_srec
from src.helper import HexfileType, is_valid_for_data
from src.srec_view import SrecView


def make_view() -> BinaryView:
    SrecView.register()
    return binaryninja.open_view(b"S1137AF00A0A0D0000000000000000000000000061")


def test_valid():
    assert is_srec("S1137AF00A0A0D0000000000000000000000000061")


def test_view_valid():
    bv = binaryninja.open_view(b"S1137AF00A0A0D0000000000000000000000000061")
    assert is_valid_for_data(bv, HexfileType.SREC) is True


def test_make_view():
    view = make_view()
    assert view.view_type == "SREC"
