# Local Meross API for Automation

This repo uses [Merosslot](https://github.com/albertogeniola/MerossIot) an aync Python library for controlling Meross devices.

By building an API that you can run locally, you can open new automation possibilities (iOS Shortcuts for instance).

The API currently supports one endpoint to toggle a device on and off.
To add or change the type of device, please refer to the [Merosslot documentation](https://albertogeniola.github.io/MerossIot/)

## Requirements

Merosslot requires Python 3.7+. Previous versions won't be supported by this library.

## Raspberry Pi

1. Update packages

```
sudo apt update && sudo apt upgrade -y
```

2. Dowload and run Docker

```
curl -sSL https://get.docker.com | sh
```

3. Clone this repo

```
https://github.com/monzanifabio/meross-local-api.git
```

4. Run the container

```
cd meross-local-api
docker build -t meross-api
docker run meross-api
```

The container will open a port 5000 on your device, so when making request use your device local ip address and the port (e.g. `192.168.12.34:5000`)
