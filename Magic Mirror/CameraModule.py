
#To install
#sudo apt-get install python3-picamera

from picamera import PiCamera
from time import sleep

# Initialize PiCamera
camera = PiCamera()

# Start preview
camera.start_preview()

# Sleep for a few seconds to allow camera to warm up
sleep(2)

# Capture image
camera.capture('/home/pi/Desktop/image.jpg')

# Stop preview
camera.stop_preview()
