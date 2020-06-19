
## 0. Getting Comfortable with the Arty Board

The goal of this tutorial is to cover the absolute basics of the Arty board -- just plugging it in, and playing around with its build-in demo.

__Software Needed:__ none

* Do `ls /dev/ttyUSB*` in a terminal on your laptop.   Remember what you see.
* Now, connect the Arty board to your laptop using the USB cable.  Be somewhat careful plugging the miniUSB end into the board.
* Some lights on the board should turn on.
* Do `ls /dev/ttyUSB*` again.   There should be something new there.  We're not going use that info in _this_ tutorial, but we will in the next one.
* Find the 4 pushbuttons in one corner of the board, `BTN0`...`BTN3`.  
* Press one of the two middle ones.  You should see some kind of flashing/cycling in the bright LEDs.
* Press the button _farthest_ from the corner to reset (`BTN3`).   You may need to hold it down for a second or so.
* Push the other middlish button -- you should see different behavior now.
* Press `BTN3` again to reset.
* Try `BTN0` (cornermost) now.  You won't see anything changing, but if you change the slide switches, you'll see the brightness of the 4 smaller green LEDs change.

### What happened? 

The Arty comes shipped with a demo bitstream loaded in its flash (nonvolatile) memory.   
When you power on the Arty by plugging it in, it automatically loads this bitstream into the FPGA.  

So far, the USB cable has only been used to supply power to the board.



