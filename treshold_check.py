import os
import requests
import dotenv
from psutil import disk_usage

# Load environment variables from the .env file
dotenv.load_dotenv()

# Threshold for available storage, in GB
THRESHOLD = int(os.getenv("STORAGE_THRESHOLD"))

# Discord webhook URL
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Get the root partition usage information
root_partition = disk_usage("/")

# Calculate the available storage on the root partition
avail = root_partition.free // (1024**3)

# Check if available storage is below the threshold
if avail < THRESHOLD:
    # Send a Discord notification
    requests.post(WEBHOOK_URL, json={
        "content": f"Available storage on root partition is below {THRESHOLD}GB. Current available storage: {avail}GB"
    })
