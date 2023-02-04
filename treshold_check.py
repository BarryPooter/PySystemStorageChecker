import os
import requests
import dotenv
from psutil import disk_usage

# Load environment variables from the .env file
dotenv.load_dotenv()

# Threshold for available storage, in GB
THRESHOLD = int(os.getenv("STORAGE_THRESHOLD"))

# List of mounts to check
MOUNTS = os.getenv("MOUNTS_TO_CHECK", "/").split(",")

# Discord webhook URL
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

for mount in MOUNTS:
    # Get the usage information for the current mount
    usage = disk_usage(mount)

    # Calculate the available storage on the mount
    avail = usage.free // (1024**3)

    # Check if available storage is below the threshold
    if avail < THRESHOLD:
        # Send a Discord notification
        requests.post(WEBHOOK_URL, json={
            "content": f"Available storage on {mount} is below {THRESHOLD}GB. Current available storage: {avail}GB"
        })
