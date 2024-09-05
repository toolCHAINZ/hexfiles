from typing import Optional

from binaryninja import BinaryView, SegmentFlag, Settings, Platform
from bincopy import _Segment
import binaryninja

from .helper import (
    HexfileType,
    get_segments,
    is_valid_for_data,
)


class BaseView(BinaryView):  # type: ignore
    hexfile_type: HexfileType
    hex_segments: list[_Segment]

    @classmethod
    def get_load_settings_for_data(cls, _data: BinaryView) -> Optional[Settings]:
        s = Settings()
        return s

    @classmethod
    def is_valid_for_data(cls, data: BinaryView) -> bool:
        return is_valid_for_data(data, cls.hexfile_type)

    def __init__(self, data: BinaryView):
        self.hex_segments = get_segments(data)
        decoded = b"".join(s.data for s in self.hex_segments)
        parent = BinaryView.new(data=decoded)
        BinaryView.__init__(self, file_metadata=data.file, parent_view=parent)

    def init(self) -> bool:
        offset = 0
        platform_list = list(Platform)
        self.platform = platform_list[binaryninja.interaction.get_choice_input("Select the platform of the loaded file: ","Platform Selection", [x.name for x in platform_list])]
        for segment in self.hex_segments:
            length = len(segment.data)
            choice = binaryninja.interaction.get_choice_input(f"Select permission levels for the segment {hex(segment.address)}: ", f"Segment Permissions {hex(segment.address)}", ["r--", "rw-", "r-x","rwx"])
            perms = None
            match choice:
                case 0:
                    perms = SegmentFlag.SegmentReadable
                case 1:
                    perms = SegmentFlag.SegmentReadable | SegmentFlag.SegmentWritable
                case 2:
                    perms = SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable
                case 3:
                    perms = SegmentFlag.SegmentReadable | SegmentFlag.SegmentWritable | SegmentFlag.SegmentExecutable
                case _:
                    return False
            

            self.add_auto_segment(
                segment.address,
                length,
                offset,
                length,
                perms
            )
            offset += length
        return True

    def perform_get_address_size(self) -> int:
        return 4
