import enum

from binaryninja import BinaryView
from bincopy import BinFile, _Segment, is_ihex, is_srec, is_ti_txt, is_verilog_vmem


class HexfileType(enum.IntEnum):
    TI_TXT = 1
    IHEX = 2
    SREC = 3
    # VMEM = 4


def is_valid_for_data(bv: BinaryView, ty: HexfileType) -> bool:
    length = bv.length
    capped_length = min(length, 1000)
    # read up to 1000 bytes
    data = bv.read(0, capped_length)
    # find last newline
    index = data.find(b"\n")
    trimmed = data
    if index != -1:
        trimmed = data[0:index]
    match ty:
        case HexfileType.TI_TXT:
            if bv.length < 2:
                return False
            last_two_bytes = bv.read(bv.length - 2, 2)
            print(last_two_bytes)
            if last_two_bytes not in [b"q\n", b"Q\n"]:
                return False
            return is_ti_txt(bv.read(0, bv.length).decode("utf8"))
        case HexfileType.IHEX:
            return is_ihex(trimmed.decode("utf8"))
        case HexfileType.SREC:
            return is_srec(trimmed.decode("utf8"))
        case HexfileType.VMEM:
            return is_verilog_vmem(trimmed.decode("utf8"))


def get_segments(bv: BinaryView) -> list[_Segment]:
    binfile = BinFile()
    binfile.add(bv.read(0, bv.length).decode("utf8"))
    return binfile.segments
