Here's an updated `README.md` that includes your additional steps for installing CircuitPython on your M5Stack Cardputer:

---

# M5Unit-Synth-CircuitPython-Toolkit

This repository contains tools and scripts for interfacing with the M5Unit Synth using CircuitPython. It provides basic functionality such as resetting the synth, adjusting volume, and sending MIDI commands.

## Getting Started

### Prerequisites

Before you can use this toolkit, you'll need to install CircuitPython on your M5Stack Cardputer and set up your CircuitPython environment.

### Installation

1. **Install CircuitPython on M5Stack Cardputer**

   To install CircuitPython on your M5Stack Cardputer, follow these steps:

   - **Download the CircuitPython Firmware:**
     Visit the [CircuitPython M5Stack Cardputer](https://circuitpython.org/board/m5stack_cardputer/) page and download the `.bin` firmware file.

   - **Use the M5Stick-Launcher to Install CircuitPython:**
     You can use the [M5Stick-Launcher](https://github.com/bmorcelli/M5Stick-Launcher) to install the CircuitPython firmware from an SD card. Download and copy the `.bin` file to your SD card.

     - Insert the SD card into your M5Stack Cardputer.
     - Open the M5Stick-Launcher, navigate to the `.bin` file, and execute it.
     - The firmware will be installed, and your M5Stack Cardputer will boot into CircuitPython.

2. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Axlfc/M5Unit-Synth-CircuitPython-Toolkit.git
   ```

3. **Copy Files to Your CircuitPython Device**

   After cloning the repository, connect your CircuitPython device to your computer. Copy the files from the repository into the `CIRCUITPY` directory on your device.

4. **Install Required Libraries**

   This project depends on the `adafruit_midi` library. You need to download and place this library into the `lib` folder on your CircuitPython device.

   - **Download the `adafruit_midi` library:**
     Download the `adafruit_midi` library from the [Adafruit CircuitPython MIDI GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_MIDI).
     
     - Direct link to the `adafruit_midi` folder: [Adafruit MIDI Library Folder](https://github.com/adafruit/Adafruit_CircuitPython_MIDI/tree/main/adafruit_midi).

   - **Copy the Library:**
     Locate the `adafruit_midi` folder from the downloaded repository and copy it to the `lib` folder on your CircuitPython device.

   Your `lib` directory should now look like this:

   ```
   CIRCUITPY/
   ├── code.py
   └── lib/
       └── adafruit_midi/
   ```

5. **Run the Code**

   After setting everything up, your device should be ready to run the scripts in this toolkit and interact with the M5Unit Synth.

### Usage

This toolkit includes functions to send MIDI commands, reset the synth, and adjust the volume. Refer to the individual scripts for specific usage examples.

### Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. 

### License

This project is licensed under the GPL-2.0 License. See the `LICENSE` file for details.

### Acknowledgments

- Special thanks to [Adafruit](https://www.adafruit.com/) for providing the necessary libraries and support for CircuitPython development, and to [bmorcelli](https://github.com/bmorcelli) for the M5Stick-Launcher project.
- Big shoutout to [bmorcelli's M5Stick-Launcher project](bmorcelli/M5Stick-Launcher), thanks to that I was able to install CircuitPython into my M5Stack Cardputer with such ease.