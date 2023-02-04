# Python3 System Storage Checker

A Python3 script that checks if the available system storage (diskusage) is above a specified threshold and sends a notification to a Discord webhook if it's below that threshold.

## Requirements

- Python 3
- psutil
- requests
- python-dotenv

## Setup

1. Clone this repository or download the script.

2. Install the required libraries by running the following command:

    pip install psutil requests python-dotenv

3. Create a `.env` file in the same directory as the script and add the following lines, replacing `YOUR_DISCORD_WEBHOOK_URL` with your own Discord webhook URL and adjusting the value of `STORAGE_THRESHOLD` as desired:

    DISCORD_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
    STORAGE_THRESHOLD=50

4. Make the script executable with the following command:

    chmod +x /path/to/script.py

## Usage

Run the script with the following command:

    /usr/bin/python3 /path/to/script.py

## Scheduling

To run the script automatically, you can use a cronjob. To add a cronjob that runs the script twice a day, run the following command:

    crontab -e

This will open the crontab file in the default text editor. Add the following line to the file and save it:

    0 0,12 * * * /usr/bin/python3 /path/to/script.py

This cronjob runs the script at `00:00` and `12:00` every day.

Note that the path to the `python3` binary and the script may be different on your system, so make sure to replace `/usr/bin/python3` and `/path/to/script.py` with the correct paths for your setup.