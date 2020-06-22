
## 2. Programming the Arty Board

The goal of this tutorial is to demonstrate downloading a bitstream to the Arty A7 35T board to change its behavior,
and then restore behavior to the built-in demo.

__Software Needed:__ openOCD

### Directions:

* Install "openocd" on your laptop: `sudo apt install openocd`
* Plug in the USB cable to connect the FPGA board to your laptop.
* Play around with the pre-loaded demo: press BTN0...BTN3 and see the LED behavior change.
* Clone this repository if you have not already, and `cd` to this directory. 
* Sitting in this directory, run the following command on your laptop:
  `openocd -f ./openocd_xilinx.cfg -c "init ; pld load 0 top.bit ; exit"`
* You should see the following on your laptop (details will vary):
```
$ openocd -f ./openocd_xilinx.cfg -c "init ; pld load 0 top.bit ; exit"
Open On-Chip Debugger 0.10.0+dev-01012-ged8fa09cf-dirty (2020-01-15-04:14)
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
Info : auto-selecting first available session transport "jtag". To override use 'transport select <transport>'.
fpga_program
Info : ftdi: if you experience problems at higher adapter clocks, try the command "ftdi_tdo_sample_edge falling"
Info : clock speed 25000 kHz
Info : JTAG tap: xc7.tap tap/device found: 0x0362d093 (mfg: 0x049 (Xilinx), part: 0x362d, ver: 0x0)
```
* On the board, you should see the `DONE` LED by the `PROG` button go dark for about a second, then come back on.
* You should see the behavior of the 4+4 LEDs change.   They should now start counting in binary.   The 4 LSB are the bright LEDs, and the 4 MSB are the smaller green LEDs.  The count should increment about every 2.5 seconds.
* Now, press the `PROG` button.   Behavior should revert to the built-in demo.
* If you wish, repeat using the `openocd` command to load the counter configuation, then resetting by power-cycling or pressing `PROG`.

### What happened? 

When the board is powered on, the FPGA will download a bitstream from the flash memory on the board
into its configuration storage.
The board is shipped with a demo bitstream in the flash memory.   The FPGA forgets its loaded bitstream
when it is turned off, so it must be reloaded every time it is turned on.

The `openocd` command transfers the laptop file `top.bit` into the FPGA's configuration storage using the USB cable.
This overwrites the previous contents of the FPGA's configuration storage, 
and the FPGA will take on different behavior.
_This does not affect the demo bitstream stored in the flash memory._   

Pressing the `PROG` button forces the FPGA to reload its configuration from the flash memory,
so it will get the demo bitstream again.

It is possible to change the bitstream stored in the flash memory (not covered here).   
If you update the flash bitstream, then the FPGA will load _that_ bitstream 
every time the board is powered on, or the `PROG` button is pushed.

[OpenOCD](http://openocd.org/doc-release/html/About.html)
has 
[many uses](http://openocd.org/doc-release/html/index.html)
beyond programming FPGAs.  


Source for `openocd_xilinx.cfg`:
```
https://github.com/litex-hub/linux-on-litex-vexriscv/blob/master/prog/openocd_xilinx.cfg
```




