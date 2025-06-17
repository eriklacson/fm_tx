FM Transmitter in GNU Radio

A simple FM transmitter built using GNU Radio Companion (GRC) and Python, designed for experimentation and learning about FM modulation.

## Features

- FM Modulation using GNU Radio
- GRC flowgraph for visual editing
- Plays back audio files over FM
- Python script to run the transmission without opening GRC


## Requirements

- GNU Radio (v3.8+ recommended)
- Python 3.x
- numpy
- A compatible SDR device (e.g., HackRF, USRP)

Install Python dependency:
pip install numpy

---

## Setup & Usage

1. Clone the repo:
   git clone https://github.com/eriklacson/fm_tx.git
   cd fm_tx

2. Verify the sample audio file exists or replace it with your own .wav.

3. Run using GNU Radio Companion:
   - Open fm_tx.grc in GRC
   - Set your desired center frequency
   - Run the flowgraph

4. Or run directly via terminal:
   python3 top_block.py

---

## How to Use

- Start the transmitter
- Tune in to the center frequency with a radio or SDR receiver
- Listen to your audio being broadcast

---

## Customization

- Replace the .wav file in the source
- Change center frequency or gain in fm_tx.grc
- Modify sample rate to match your device’s specs

---

## Troubleshooting

- No audio? Confirm SDR is connected and frequency is clear.
- Distortion? Verify sample rates and audio file format.
- Issues with Python? Check dependencies and GRC version.

---

## Contributing

Contributions are welcome via pull request or issues.

---

## Contact

Created by Erik Lacson. For questions or feedback, open an issue on GitHub.

---

## Future Improvements

- Live mic input support
- RDS metadata
- Stereo broadcasting options
