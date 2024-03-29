"""
### Example of parallelism using threads in Python. ###

This program downloads multiple urls in parallel using threads.
It creates a thread for each url and starts them. Then it waits 
for all threads to finish.

Parallelism permits multiple tasks to be executed simultaneously. 
In this case, the program downloads multiple urls at the same time using
threads. It will improve the performance of the program by reducing 
the time taken to download all the urls sequentially.

The timestamps in the output show that the downloads are happening in parallel
as the download times are interleaved.
"""

import threading
import requests
from datetime import datetime

# Function to download a url and print the current time when the download
# is finished
def download(url):
    response = requests.get(url)
    print(f"Downloaded {url} at {datetime.now().strftime('%X.%f')}")

urls = ["https://www.google.com",
        "https://www.example.com", "https://www.github.com"]

# Create and starts a thread for each url
threads = []
for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    print(f"Starting thread for {url} at {datetime.now().strftime('%X.%f')}")
    threads.append(thread)
    thread.start()
print("****All threads started****")

# Wait for all threads to finish
for thread in threads:
    thread.join()
# Rather than downloading each url sequentially, the program downloads
# them in parallel.
print("***All downloads finished***")
