# hexfiles (v1.3.0)
Author: **toolCHAINZ**

_A simple loader for Motorola SREC, Intel HEX, and TI-TXT files._

## Description:

# Hexfiles

 `hexfiles` provides a simple `BinaryView` for "Hex" files (Motorola SREC, Intel Hex, TI-TXT). The actual parsing of hex files is offloaded to the excellent Python library `bincopy`. For now, this `BinaryView` is read-only (patches will not be saved back into the source hex file). Will hopefully add that soon.


## Installation Instructions

### Darwin

`pip install -r requirements.txt`

### Windows

`py -m pip install -r requirements.txt`

### Linux

`pip install -r requirements.txt`

## Minimum Version

This plugin requires the following minimum version of Binary Ninja:

* 2170


## License

This plugin is released under a MIT license.
## Metadata Version

2
