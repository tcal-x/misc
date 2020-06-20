
## 1. Programming the Arty Board

The goal of this tutorial is to demonstrate downloading a bitstream to the Arty board to change its behavior,
and then restore behavior to the built-in demo.

__Software Needed:__ openOCD

* Install "openocd" on your laptop -- `sudo apt install openocd`
* etc.

```
openocd -f ./board-digilent-basys3.cfg -c "init ; pld load 0 top.bit ; exit"
openocd -f ./openocd_xilinx.cfg -c "init ; pld load 0 top.bit ; exit"
```

sources:
```
https://github.com/SymbiFlow/prjxray/blob/master/utils/openocd/board-digilent-basys3.cfg
https://github.com/litex-hub/linux-on-litex-vexriscv/blob/master/prog/openocd_xilinx.cfg
```



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

### What happened? 

blah blah

