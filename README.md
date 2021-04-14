# luma

This script reboots an IP camera, then during lens initialization, PoE power is cut off.

When the device powers back on, it logs back into the web UI and takes a screenshot of the camera image post fault insertion. Each screenshot is stored in the "Screenshots" folder and the logs are stored in the "logs" folder. 

Follow the instructions below to run the script.

# Instructions

1. Unzip or clone repo locally
2. Open project in Pycharm IDE
3. Open a terminal window (bottom bar)
4. type "python 710_reboot.py" then press ENTER
5. The script will ask for the IP address of the camera under test
6. Enter number of loops you want the script to perform
7. Press 'Y' or 'y' key, then ENTER.
8. When the script is finished, it will log in the terminal output "Process finished with exit code 0"
