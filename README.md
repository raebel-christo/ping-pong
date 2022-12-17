# Ping Pong
A Ping Pong ball game that is played on an 8x8 neopixel dot matrix, powered by Raspberry Pi using Python. The panels are controlled by keyboard using the `sshkeyboard` library since the raspberry pi was operated via an ssh terminal and the above mentioned library reads key presses over an ssh terminal.

![20221211_001216](https://user-images.githubusercontent.com/35605103/206886691-bece06c9-ade9-46df-8585-cebd836fd4bf.jpg)

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

#### Releases
There are two releases with different features:
##### V1.0.0A
This release uses the default ssh keyboard controls for the players. Player 1 uses `W` and `S`. whereas player 2 uses `I` and `K`.
##### V1.0.0B
This release uses default ssh keyboard control for player 1, but player 2 uses a webpage to control the panel. It is required to download the web server package in order to launch the webpage that hosts the controls of player 2.

Required dependancies for webserver:
- Node JS
- Cors
- socket.io

With the setup all complete, go ahead and try that python code. Have fun playing ping pong on a neopixel grid and relive that arcade experience!
