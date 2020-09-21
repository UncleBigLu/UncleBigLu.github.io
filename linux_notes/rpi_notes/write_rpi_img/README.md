# Install raspberry pi OS to SD card on Mac using termimal

**step1:** Insert the SD card into a card reader and attach it on your Mac.

**step2:** Launch your terminal.

**step3:** In this step you need to find your SD card in the terminal. Run `df -h` without your card reader, then attach sd card to your computer and run it again. Typically you'll get a device like **/dev/disk3s1**.

**step4:** unmount your SD card using command`sudo diskutil unmount device_name`. Eg, sudo diskutil unmount /dev/disk3s1.

**step5:** After unmount the card,  remove the s1

and add a 'r'before the device name, like /dev/rdisk3.

==please ensure that you won' t burn the iso file to your computer disk==



