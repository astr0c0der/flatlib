from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')

# get geo position object
pos = GeoPos('38n32', '8w54')

# Get the chart
chart = Chart(date, pos, hsys=const.HOUSES_PLACIDUS)

for hse in const.LIST_HOUSES:
    house = chart.getHouse(hse)
    print(house.id)
    print(house.lon)
    print(house.lat)
    print(house.sign)
    print(house.inElement())

# for a list with objects in the houses
for obj in chart.objects:
    house = chart.houses.getObjectHouse(obj)
    print(f"The object {obj.id} is in {house.id}")
