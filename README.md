# Copernicus Global Land Service data download

This repository provides a quick and dirty way to download Copernicus Global Land Service data. The data is provided in NetCDF format and can be downloaded from the [Copernicus Global Land Service](https://land.copernicus.eu/global/) website. The data is provided in tiles and can be downloaded manually from the website. However, if you need to download a large number of tiles, this can be a very time-consuming process. This repository provides a Python script which generates wget bash requests to download the data for you.

## Disclaimer

**This script exposes your Copernicus Global Land Service username and password in plain text. Use at your own risk.**

**Do not commit your USERNAME and PASSWORD to a public repository.**

## Requirements

- Python 3.10 or higher
- wget
- A Copernicus Global Land Service account

## Usage

1. Clone this repository

2. Run the script with the following command:

```zsh
python3 cgls_ssm_daily_download.py
```

3. Follow the instructions in the terminal
