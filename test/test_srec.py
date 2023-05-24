import binaryninja
from binaryninja import BinaryView
from bincopy import is_srec
from ..src.srec_view import SrecView

data = "S1137AF00A0A0D0000000000000000000000000061"


def make_view() -> BinaryView:
    return binaryninja.open_view(data.encode("utf8"))


def test_valid() -> None:
    assert is_srec(data)


def test_invalid() -> None:
    bv = binaryninja.open_view(b"\xff\xff\xff\xff")
    assert SrecView.is_valid_for_data(bv) is False


def test_make_view() -> None:
    view = make_view()
    assert view.view_type == "SREC"
