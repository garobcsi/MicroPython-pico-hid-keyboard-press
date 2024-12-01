# MicroPython-Pico-HID-Keyboard-Press

A MicroPython project for the Raspberry Pi Pico that emulates a HID keyboard.

## Building

```
git submodule update --init --recursive
cd ports/rp2
mkdir build
cd build
cmake .. -DPICO_BOARD=pico
make
```