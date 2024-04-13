"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    aspects.

"""

from flatlib import aspects # needed for aspect calculations
from flatlib import const # constant variables
from flatlib import props
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
# id = name 
# lon = longitude decimals 
# lat = latitude decimals
# sign = sign, signlon = longitude position in sign 
# lonspeed = longitude speed 
# dms = decimal to dms 
# movement = planet movement
# condition is angular, cadent, succedant
sun = chart.getObject(const.SUN)

print (f""" 
    Sun: {sun.id} 
         {sun.lon}
         {sun.lat}
         {sun.sign}
         {sun.signlon}
         {sun.lonspeed}
         {sun.dms}
         {sun.movement()}
         {sun.orb()}
         {sun.element()}
         {sun.inElement()}
         {sun.isFast()}
""")

## for all objects do
for object_id in const.LIST_OBJECTS:

    obj = chart.getObject(object_id)

    print (f""" 
        {obj.id}: {obj.id} 
            {obj.lon}
            {obj.lat}
            {obj.sign}
            {obj.signlon}
            {obj.lonspeed}
            {obj.dms}
            {obj.movement()}
            {obj.orb()}
            {obj.element()}
            {obj.temperament()}
            {obj.inElement()}
    """)

