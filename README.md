# Internet Speed and File Transfer Time Calculator

This Python script allows you to check your internet connection speed and calculate the estimated time it would take to download a file of your specified size. It uses the `speedtest-cli` library to measure internet speed.

## Usage Instructions

1. Install the speedtest-cli library with this command:
```sh
	pip install speedtest-cli
```

2. Run the script with this command:
```sh
	python main.py
```

1. Follow the on-screen instructions:
	- First, it will display your internet download and upload speeds, as well as ping.
	- Next, enter the size of the file you want to download (in GB).

5. The script will calculate the estimated time it would take to download the specified file based on your internet speed.

## Example Execution
```python
Internet Connection Information:
Download Speed: 278.22 Mbps
Upload Speed: 94.54 Mbps
Ping: 11 ms
----------------------------------------
Enter the file size (in GB): 5
Estimated file download time: 0.15 seconds
```
