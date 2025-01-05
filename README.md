# SprigController 🎮

Use your Hack Club Sprig as a controller with xInput.

## Overview

Sprig is a DIY handheld console made by hackclub for teenagers.
This project allows your sprig to work as an xInput controller

## Getting Started

### Prerequisites

- A Hack Club Sprig console
- A computer
- USB cable to connect Sprig to PC

### Installation

1. **Get a Sprig:**

    Follow [these](https://github.com/hackclub/sprig/blob/main/docs/GET_A_SPRIG.md) instructions to get a Sprig from hackclub

2. **Install the circuitpython firmware:**

   - Download the .uf2 file from [here](https://circuitpython.org/board/raspberry_pi_pico_w/)
   - Plug your sprig to your computer while holding the BOOTSEL button (on the rpi pico)
   - Copy the .uf2 file to your rpi pico

3. **Clone the repository:**

    ```sh
    git clone https://github.com/Paylicier/SprigController.git
    cd SprigController
    ```
4. **Copy the files from the repo to the CIRCUITPY drive**

### Usage

1. Connect your Sprig console to the PC via USB.
2. The Sprig is now detected as a gamepad (hid)

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hack Club](https://hackclub.com/) for creating the awesome Sprig console.
- Adafruit for the libs
