#Psutil module in Python wit.   Python cross-platform library used to access system details and process utilities.
#https://www.geeksforgeeks.org/python/psutil-module-in-python/
import psutil
import time


print("Monitoring network traffic... (press Ctrl+C to stop)")

# Loop to check network traffic every second
while True:
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    #print(str(bytes_sent))
    print("Bytes Sent: " + str(bytes_sent) + " Bytes Received: " + str(bytes_recv) + " CPU:" + str(psutil.cpu_percent(1)) )
    time.sleep(1)   # wait 1 second before checking again
