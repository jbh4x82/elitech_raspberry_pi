# elitech_raspberry_pi
Elitech datareader implementation on Raspberry Pi with Elitech RC-4HC to upload temperature and humidity data to a server URL in JSON format.

Based on: https://pypi.org/project/elitech-datareader/ and https://github.com/civic/elitech-datareader

NB: This is written for Raspberry Pi (Raspbian) and RC-4HC.
- If you are using a different operating system, you might have to change the device address from /dev/ttyUSB0 (you can browse the /dev folder on your PC to find a device that has "USB" in the name)
- If you are getting no records, make sure you have started the datareader by long pressing the play button on the physical device (you will see a play-symbol once the recording has started).
- Should you use the set_reader_interval function, you will have to manually restart the recording function by long pressing the play button on the device.
- Tested using this device: https://www.amazon.co.uk/gp/product/B00XWETE0I/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1
