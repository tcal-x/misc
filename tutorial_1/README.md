
## 1. Communicating with the Arty Board

The goal of this tutorial is to demonstrate another use of the USB cable connection: TTY-style communication with the board.

__Software Needed:__ picocom

* Install "picocom" on your laptop -- `sudo apt install picocom`
* Remember the new /dev/ttyUSBx that you saw?  We're going to connect to that.
* NOTE: If you unplug the board, then plug it in again, it might end up at a different ttyUSB!
* Run `picocom --baud 115200 /dev/ttyUSBx` -- replace 'x' with 0 or 1 or 2
* Don't worry -- you won't wreck anything if you choose the wrong one.
* You will see the board print out stuff on the terminal as you push buttons like before.
* You can also notice that a small LED by the USB cable connector on the board flickers as it sends data over the USB cable
* If you type a character in the picocom terminal, you will see the other LED by the cable flicker.   The board just ignores it with this gateware, however.
* To exit picocom, use "ctrl-a ctrl-x".

The initial printout from the board should look like this:

```
********************************************************
********************************************************
**        Avnet/Digilent Arty Evaluation Board        **
**        LEDs and switches GPIO Demonstration        **
********************************************************
********************************************************
**
Choose Task:
BTN0: Print PWM value.
BTN1: 'Cylon' LED display.
BTN2: Scrolling LED display.
BTN3: Return to this menu.
```

You can unplug the cable to power off the board (some other boards have a power switch, but Arty doesn't).   You probably want to unplug the cable from your laptop instead of unplugging from the board, since board connector doens't feel that sturdy to me.


### What happened? 

We're using the USB as a communication link.  This style is sometimes called "UART".  
There is just one bit in each direction.  When you start using it in designs, if you work with Verilog,
you will see the pins "rx" and "tx" for receive and transmit. 

If you don't set the speed/"baud" correctly, you will see jibberish, since you're not sampling the bits correctly, and this protocol isn't smart enough to auto-adapt.  But don't worry, you won't break anything if you have the wrong speed, so if you don't know, you can just try the commonly-used ones (115200, 406800, 1e6).



