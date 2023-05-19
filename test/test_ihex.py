import binaryninja
from binaryninja import BinaryView
from bincopy import is_ihex

data = ":10010000214601360121470136007EFE09D2190140"


def make_view() -> BinaryView:
    return binaryninja.open_view(data.encode("utf8"))


def test_valid():
    assert is_ihex(data)


def test_make_ihex():
    view = make_view()
    assert view.view_type == "IHex"
