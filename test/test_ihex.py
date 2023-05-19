import binaryninja
from binaryninja import BinaryView
from bincopy import is_ihex
from src.helper import HexfileType, is_valid_for_data
from src.ihex_view import IHexView


def make_view() -> BinaryView:
    IHexView.register()
    return binaryninja.open_view(b":10010000214601360121470136007EFE09D2190140")


def test_valid():
    assert is_ihex(":10010000214601360121470136007EFE09D2190140")


def test_view_valid():
    bv = binaryninja.open_view(b":10010000214601360121470136007EFE09D2190140")
    assert is_valid_for_data(bv, HexfileType.IHEX) is True


def test_make_ihex():
    view = make_view()
    assert view.view_type == "IHex"
