"""
A script to scrape Bing's image of the day
and set it to the background image on OS X

Tested on OS X High Sierra 10.13.5

Miles Crighton, 22-06-18
"""

import json
from subprocess import Popen
from os import getcwd
from urllib import request

#Script for applying desktop image on OS X
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to "%s" as POSIX file
end tell
END"""

#Function to run osascript and set background image
def set_desktop_background(filename):
    Popen(SCRIPT%filename, shell=True)

#Retrieve JSON details of Bing IOTD
json_url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

with request.urlopen(json_url) as url:
    json_data = json.loads(url.read().decode())

#Formulate current image URL of IOTD
img_url = 'http://bing.com' + json_data["images"][0]["url"]

#Save bing image to local directory
request.urlretrieve(img_url, "bing_image.jpg")

#Set desktop background to saved image
set_desktop_background(getcwd() + "/bing_image.jpg")
