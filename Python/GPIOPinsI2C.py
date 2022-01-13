# jkammau97
# Code for GPIO Pins - I2C
# 1/13/22
# Write a new program by combining the two example scripts you have already used.
# Mash these two programs together so that the X, Y, and Z accelerations measured by your accelerometer are displayed on your little OLED display. 
# And convert and scale the values to m/s2, rounded to two or three decimal places.  
# So, when it's just sitting flat on the table, the z-acceleration should be roughly 9.81 m/s2. 
# ---
# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time
import math

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()


while True:
    # Clear display.
    disp.clear()
    disp.display()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width #128
    height = disp.height #64
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Load default font.
    font = ImageFont.load_default()
    
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    # Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    #font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write 3 lines of text.
    draw.text((10, 0), 'ACCEL DATA', font=font, fill=255)
    draw.text((10, 16),  'X: ' + str(math.floor(accel_x*981/1024)), font=font, fill=255)
    draw.text((10, 32), 'Y: ' + str(math.floor(accel_y*981/1024)), font=font, fill=255)
    draw.text((10, 48), 'Z: ' + str(math.floor(accel_z*981/1024)), font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    
    # Wait half a second and repeat.
    time.sleep(0.5)
