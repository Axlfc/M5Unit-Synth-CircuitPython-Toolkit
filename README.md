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

   This project depends on several libraries. You need to download and place these libraries into the `lib` folder on your CircuitPython device.

   - **Download the `adafruit_midi` library:**
     Download the `adafruit_midi` library from the [Adafruit CircuitPython MIDI GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_MIDI).
     - Direct link to the `adafruit_midi` folder: [Adafruit MIDI Library Folder](https://github.com/adafruit/Adafruit_CircuitPython_MIDI/tree/main/adafruit_midi).

   - **Download the `asyncio` library:**
     Download the `asyncio` library from the [Adafruit CircuitPython asyncio GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_asyncio/releases/tag/1.3.2).
     - Direct link to the library release: [Adafruit CircuitPython asyncio 1.3.2](https://github.com/adafruit/Adafruit_CircuitPython_asyncio/releases/tag/1.3.2).

   - **Download the `adafruit_ticks` library:**
     Download the `adafruit_ticks` library from the [Adafruit CircuitPython Ticks GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_Ticks/releases/tag/1.1.0).
     - Direct link to the library release: [Adafruit CircuitPython Ticks 1.1.0](https://github.com/adafruit/Adafruit_CircuitPython_Ticks/releases/tag/1.1.0).
   
   - **Download the `adafruit_display_text` library:**
     Download the `adafruit_display_text` library from the [Adafruit CircuitPython Display Text GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text).
     - Direct link to the library release: [Adafruit CircuitPython Display Text 3.1.2](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases/tag/3.1.2).
   
   - **Download the `adafruit_display_shapes` library:**
     Download the `adafruit_display_shapes` library from the [Adafruit CircuitPython Display Shapes GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_Display_Shapes).
     - Direct link to the library release: [Adafruit CircuitPython Display Shapes 2.8.3](https://github.com/adafruit/Adafruit_CircuitPython_Display_Shapes/releases/tag/2.8.3).

   - **Download the `adafruit_displayio_layout` library:**
     Download the `adafruit_displayio_layout` library from the [Adafruit CircuitPython DisplayIO Layout GitHub Repository](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_Layout).
     
     - Direct link to the library release: [Adafruit CircuitPython DisplayIO Layout 2.1.0](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_Layout/releases/tag/2.1.0).
	
   - **Copy the Libraries:**
     Locate the `adafruit_midi`, `asyncio`, `adafruit_ticks`, `adafruit_display_text`, `adafruit_displayio_layout` folders from the downloaded repositories and copy them to the `lib` folder on your CircuitPython device.

   Your `lib` directory should now look like this:

   ```
   CIRCUITPY/
   ├── code.py
   └── lib/
       ├── adafruit_midi/
       ├── adafruit_display_text/
       ├── adafruit_displayio_layout/
       ├── adafruit_display_shapes/	   
       ├── adafruit_ticks.py
       └── asyncio/
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
- Big shoutout to [bmorcelli's M5Stick-Launcher project](https://github.com/bmorcelli/M5Stick-Launcher), thanks to that I was able to install CircuitPython into my M5Stack Cardputer with such ease.
- Refer to [M5Stack documentation](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Synth/SAM2695.pdf) for more information.
