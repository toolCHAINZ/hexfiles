from binaryninja import BinaryView, BinaryViewType
from binaryninja.enums import SegmentFlag
from bincopy import BinFile, is_ihex

class IHexView(BinaryView):
    name = "Intel HEX"
    @classmethod
    def is_valid_for_data(self, data: BinaryView):
        actual_data = data.read(0, len(data)).decode('utf8')
        if is_ihex(actual_data):
            return True
        return False

    def __init__(self, data: BinaryView):
        actual_data = data.read(0, len(data)).decode('utf8')
        binfile = BinFile()
        binfile.add(actual_data)
        decoded = b''.join(s.data for s in binfile.segments)
        parent = BinaryView.new(data=decoded)
        self.hex_segments = binfile.segments
        BinaryView.__init__(self, file_metadata=data.file, parent_view=parent)

    def init(self):
        offset = 0
        for segment in self.hex_segments:
            length = len(segment.data)
            self.add_auto_segment(segment.address, length, offset, length, SegmentFlag.SegmentReadable | SegmentFlag.SegmentWritable | SegmentFlag.SegmentExecutable)
        return True
