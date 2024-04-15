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
chart = Chart(date, pos, IDs=const.LIST_OBJECTS, include_fixed_stars=True)

# Print list with aspects of all objects
# --------------------------------------
# list all aspects.to decide the type of aspects  
# const.MAJOR_ASPECTS.
# const.MINOR_APSECTS
# const.ALL_ASPECTS
# To choose which objects to calculate the aspects
all_aspects = aspects.getAllAspects(chart.objects, const.MAJOR_ASPECTS)
for aspect in all_aspects:
    print(aspect)

