import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping
    return download_speed, upload_speed, ping

def print_internet_information(download_speed, upload_speed, ping):
    print("Internet Connection Information:")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")
    print("----------------------------------------")

def calculate_transfer_time(file_size_gb, download_speed):
    size_in_mb = file_size_gb * 1024
    time_in_seconds = size_in_mb / download_speed
    return time_in_seconds

download_speed, upload_speed, ping = check_internet_speed()
print_internet_information(download_speed, upload_speed, ping)

file_size_gb = float(input("Enter the file size (in GB): "))

transfer_time = calculate_transfer_time(file_size_gb, download_speed)
print(f"Estimated file download time: {transfer_time:.2f} seconds")
