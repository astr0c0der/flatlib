"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    aspects.

"""

from flatlib import aspects # needed for aspect calculations
from flatlib import const # constant variables
from flatlib.chart import Chart # needed for chart
from flatlib.datetime import Datetime # datetime
from flatlib.geopos import GeoPos # geolocation

# create datetime object for the chart
date = Datetime('2015/03/13', '17:00', '+00:00')

# Create geolocation object.
pos = GeoPos('38n32', '8w54')

# Then create the chart object containing all positions
chart = Chart(date, pos, IDs=const.LIST_OBJECTS)

# get single planet positions
sun = chart.getObject(const.SUN)
print (f""" 
    Sun: {sun.id}
         {sun.lon}
         {sun.lat}
         {sun.sign}
         {sun.signlon}
         {sun.lonspeed}
         {sun.dms}
""")

for obj in chart.objects:
    print (f"{obj.id}: {obj.id} {obj.lon} {obj.lat} {obj.sign} {obj.signlon} {obj.lonspeed}")