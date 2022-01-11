#!/usr/bin/python3

import urllib.request
import json
import turtle

## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## JSON 2 Python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen() # create a screen object
screen.setup(720, 360) # set resolution
screen.setworldcoordinates(-180,-90,180,90) # set screen to match coordinates being used
screen.bgpic('iss_map.gif') # add map to screen

# add the turtle/sprite/icon to the screen
screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

# iss initial placement is in the middle of the screen
# this moves it to the actual location on the map
lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)
# this line should ALWAYS be at the bottom of your script. It prevents the graphic from closing!!!
turtle.mainloop()

