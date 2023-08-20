# Artnet Node Simulator

The Artnet Node Simulator is a Python-based project designed to simulate an Art-Net node. It currently supports the handling of `OpPoll` and `OpIpProg` messages. This simulator is intended to assist in testing and development related to Art-Net communication.

## Introduction

Art-Net is an industry-standard protocol used for transmitting DMX and RDM lighting control data over Ethernet networks. This project aims to provide a convenient simulation environment for testing and experimenting with Art-Net communication.

## Features

Currently, the Artnet Node Simulator offers the following features:

- Handling of `OpPoll` messages: Simulate the behavior of an Art-Net node responding to `OpPoll` queries.
- Handling of `OpIpProg` messages: Simulate the behavior of an Art-Net node responding to `OpIpProg` messages for IP address programming.
  
Making the simulated node visible in scan applications

## Usage

The Artnet Node Simulator is designed to be lightweight and requires only pre-installed Python modules 'socket' and 'json', eliminating the need for virtual environments and a `requirements.txt` file.

### Running the Simulator

To run the simulator, simply execute the following command:

```bash
python3 main.py
```

## Future Work
In the future, the following enhancements are planned:

- `ArtAddress` Support: Implement handling of OpArtAddress messages to simulate Art-Net node address configuration.
- `OpOutput` Handling: Add support for simulating OpOutput messages to control DMX output channels.
Your contributions and suggestions for additional features are welcome!

## Contributing
If you'd like to contribute to this project, follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your fork.
- Create a pull request describing your changes.

# Happy coding! 👨‍💻
