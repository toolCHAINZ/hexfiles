import binaryninja
from binaryninja import BinaryView
from bincopy import is_srec

data = "S1137AF00A0A0D0000000000000000000000000061"


def make_view() -> BinaryView:
    return binaryninja.open_view(data.encode("utf8"))


def test_valid():
    assert is_srec(data)


def test_make_view():
    view = make_view()
    assert view.view_type == "SREC"
