# Ping Pong
A Ping Pong ball game that is played on an 8x8 neopixel dot matrix, powered by Raspberry Pi using Python. The panels are controlled by keyboard using the `sshkeyboard` library since the raspberry pi was operated via an ssh terminal and the above mentioned library reads key presses over an ssh terminal.

## Dependancies
It is required to install the following libraries in order to operate a neopixel grid on raspberry pi. For more details regarding the same, kindly refer to the [adafruit website](https://learn.adafruit.com/neopixels-on-raspberry-pi) on setting up the neopixels with raspberry pi.

You can use the following commands to install the required libraries

### Installing neopixel library
`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`

### Installing adafruit-blinka
`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`

### Installing sshkeyboard
`pip install sshkeyboard`

### Wiring setup
![Wiring](https://cdn-learn.adafruit.com/assets/assets/000/063/929/medium640/led_strips_raspi_NeoPixel_bb.jpg?15399811420)

#### Warning!
It is **important** to note here that the Raspberry Pi **cannot** supply sufficient current to drive all the LEDs on the neopixel grid. In this code, there are very few LEDs that turn on simultaneously and their brightness is kept minimum to minimize the current drawn by the neopixels. In order to improve the brightness and have the ability to turn on more LEDs, consider using an external power supply for the neopixel grid. Otherwise it is possible to burn the raspberry pi due to excess current drain.

![Alternate Wiring](https://cdn-learn.adafruit.com/assets/assets/000/064/121/medium640/led_strips_raspi_NeoPixel_Level_Shifted_bb.jpg?1540314807)

With the setup all complete, go ahead and try that python code. Have fun playing ping pong on a neopixel grid and relive that arcade experience!
