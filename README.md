# IOT - Raspberry Pi based Security Camers
This is an implementation of raspberry pi based securty camera.

## Overview- 
### Probelm- 
Develop a IOT type security camera that can be automatically triggered when there is a movement and take a picture, analyze that picture for people, count the number of people in the image and try to recognize the familier faces.

### Solution
The most important part for this setup is gettign the camera right, which means that we need to make sure the camera can be implemented and set up at a remote locaiton but can be accessed by the internet for service and software upgrades.
That leads to use the raspberry pi 3b+ (with its capability to use LAN and WiFi both) we can use the older raspberry pi 3 as well.
We can put all code on rpi for the later part where we want to process the pictures, I choose to have a seperate batch process that can run once every hour to grab all th epictures form the device and process them seperatly, this also helps with making sure we have all the data so we can later improve our facial recognization system. Also My plan is to move this process entirely to cloud for effecincy.

### Technical Design
1. We can use infrarred sensor, or a lazor based tripwire, but i choose PIR for its ability to capture movement in the focused area. PIR can detect the change sinthe infrarred signature of the environment, like poeple or pets moving. and that makes it the tool of choice.
2. We will have the PIR sensor trigger the cam and then we will make an entry with image date into mongo (online) 
3. once an hour, the process on cloud will run based onenteries in mongo and copy images from the rpi to the cloud
4. once a day the cloud based facial detection and indentificaiton will run

Here are all the components used
1. Raspberry pi 3B+
2. PIR sensor (passive infrared sensor)
3. Raspberry pi camera 


#### rpi_pirCam
Security camera using PIR sensor 
