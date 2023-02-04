# Python3 Disk Usage Notifier

This script is designed to check the available storage on specified mounts and send a Discord notification if the available storage falls below a specified threshold.

## Requirements
- Python 3
- Requests library
- Psutil library
- Dotenv library

## Setup
1. Clone the repository to your server
2. Create a `.env` file in the same directory as the script
3. Add the following environment variables to the `.env` file:
   - `STORAGE_THRESHOLD`: The available storage threshold, in GB, below which a notification should be sent
   - `MOUNTS_TO_CHECK`: A comma-separated list of mounts to check (defaults to `/` if not set)
   - `DISCORD_WEBHOOK_URL`: The URL of the Discord webhook to send notifications to
4. Install the required libraries using the following command:
    `pip install -r requirements.txt`
5. Run the script using the following command:
    `python disk_usage_notifier.py`

## Cronjob
To run the script twice a day, you can set up a cronjob by executing the following command:
    `crontab -e`

and then adding the following line to the crontab file:
    `0 0,12 * * * python /path/to/disk_usage_notifier.py`

This will run the script at midnight and noon every day.
