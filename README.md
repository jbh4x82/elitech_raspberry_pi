# elitech_raspberry_pi
Elitech datareader implementation on Raspberry Pi with Elitech RC-4HC to upload temperature and humidity data to a server URL in JSON format.

Based on: https://pypi.org/project/elitech-datareader/

NB: This is written for Raspberry Pi and RC-4HC.
- If you are using a different operating system, you might have to change: /dev/ttyUSB0
- If you are getting no records, make sure you have started the datareader by long pressing the play button on the physical device (you will see a play-symbol once the recording has started).
- Should you use the set_reader_interval function, you will have to manual restart the recording function by long pressing the play button on the device.
