
## 0. Getting Comfortable with the Arty Board

The goal of this tutorial is to cover the absolute basics of the Arty board -- just plugging it in, and playing around with its built-in demo.

__Software Needed:__ none

* Do `ls /dev/ttyUSB*` in a terminal on your laptop.   Remember what you see.
* Now, connect the Arty board to your laptop using the USB cable.  Be somewhat careful plugging the miniUSB end into the board.
* Some lights on the board should turn on -- we have power!
* Do `ls /dev/ttyUSB*` again.   There should be something new there.  We're not going use that info in _this_ tutorial, but we will in the next one.
* Find the 4 pushbuttons in one corner of the board, `BTN0`...`BTN3`.  
* Press one of the two middle ones.  You should see some kind of flashing/cycling in the bright LEDs.
* Press the button _farthest_ from the corner to reset (`BTN3`).   You may need to hold it down for a second or so.
  * Or, you can press the `RESET` button.
  * _Or_, you can press the `PROG` button, which will reprogram the FPGA and put you back at the starting point.
* Push the other middlish button -- you should see different behavior now.
* Press `BTN3` (or `RESET` or `PROG`) again to reset.
* Try `BTN0` (cornermost) now.  You won't see anything flashing, but if you change the slide switches, you'll see the brightness level of the 4 smaller green LEDs change.

### What happened? 

The Arty comes shipped with a demo bitstream loaded in its flash (nonvolatile) memory.   
When you power on the Arty by plugging it in, it automatically loads this bitstream into the FPGA.  

So far, the USB cable has only been used to supply power to the board.

> Note: there is also a description of this demo, with pictures, available on the [Digilent Blog](https://blog.digilentinc.com/getting-started-with-arty/).


