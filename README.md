# hexfiles (v1.0.0)
Author: **toolCHAINZ**

_A simple loader for Motorola SREC, Intel HEX, and TI-TXT files._

## Description:

Hex files provides a simple `BinaryView` for "Hex" files. The actual parsing of hex files is offloaded to the excellent Python library `bincopy`. For now, this `BinaryView` is read-only (patches will not be saved back into the source hex file). Will hopefully add that soon.


## Installation Instructions

### Darwin

`pip install bincopy`

### Windows

`py -m pip install bincopy`

### Linux

`pip install bincopy`

## Minimum Version

This plugin requires the following minimum version of Binary Ninja:

* 2290


## License

This plugin is released under a MIT license.
## Metadata Version

2
