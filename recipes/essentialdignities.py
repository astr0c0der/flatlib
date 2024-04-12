"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for handling 
    essential dignities.

"""

from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.dignities import essential, accidental


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos, IDs=const.LIST_OBJECTS, hsys=const.HOUSES_PLACIDUS)

for planet in const.LIST_SEVEN_PLANETS:
    obj = chart.getObject(planet)
    
    sun = chart.get(const.SUN)

    essential_dignities = essential.EssentialInfo(obj)
    accidental_dignities = accidental.dignities
    print(f"\n\nESSENTIALS FOR {obj.id}\n")
    print(f"""            ruler: {essential.ruler(obj.sign)}  
            exile: {essential.exile(obj.sign)} 
            exalted: {essential.exalt(obj.sign)} 
            fall: {essential.fall(obj.sign)} 
            day trip: {essential.dayTrip(obj.sign)} 
            almutum: {essential.nightTrip(obj.sign)} 
            almutum: {essential.almutem(obj.sign, obj.lon)} 
            term: {essential.term(obj.sign, obj.lon)} 
            face: {essential.face(obj.sign, obj.lon)}
            part trip: {essential.partTrip(obj.sign)}
            exaltation degree: {essential.exaltDeg(obj.sign)}
            fall degree: {essential.fallDeg(obj.sign)}
            sunrelation:{accidental.sunRelation(obj, sun)}
            anticisia: {obj.antiscia()}
            canticisia: {obj.cantiscia()}
            temperatment {obj.temperament()}
            orientality: {accidental.orientality(obj, sun)}
            viacombusta: {accidental.viaCombusta(obj)}
            houseofjoy: {obj.house_of_joy()}
            signofjoy: {obj.sign_of_joy()}
            
""")