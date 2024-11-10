import psutil

# CPU
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"CPU Count (logical): {psutil.cpu_count(logical=True)}")
print(f"CPU Frequency: {psutil.cpu_freq().current} MHz")

# Mémoire
virtual_memory = psutil.virtual_memory()
print(f"Total Memory: {virtual_memory.total / (1024 * 1024):.2f} MB")
print(f"Used Memory: {virtual_memory.used / (1024 * 1024):.2f} MB")
print(f"Free Memory: {virtual_memory.free / (1024 * 1024):.2f} MB")

# Disque
disk_usage = psutil.disk_usage('/')
print(f"Total Disk Space: {disk_usage.total / (1024 * 1024 * 1024):.2f} GB")
print(f"Used Disk Space: {disk_usage.used / (1024 * 1024 * 1024):.2f} GB")
print(f"Free Disk Space: {disk_usage.free / (1024 * 1024 * 1024):.2f} GB")

# Réseau
net_io = psutil.net_io_counters()
print(f"Bytes Sent: {net_io.bytes_sent / (1024 * 1024):.2f} MB")
print(f"Bytes Received: {net_io.bytes_recv / (1024 * 1024):.2f} MB")
