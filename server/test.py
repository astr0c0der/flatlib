from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib import aspects
from flatlib.lists import ObjectList
from flatlib.aspects import Aspect
from flatlib.object import House
from flatlib.geopos import GeoPos
from flatlib.dignities import accidental, essential
from flatlib.dignities.accidental import AccidentalDignity
import pandas as pd

class AstrologyChart:
    def __init__(self, datestr, timestr, offsetstr, latitude, longitude):
        self.date = Datetime(datestr, timestr, offsetstr)
        self.pos = GeoPos(latitude, longitude)
        self.chart = Chart(self.date, self.pos, IDs=const.LIST_OBJECTS, hsys=const.HOUSES_PLACIDUS)

    def decimal_to_dms(self, longitude):
        sign_num = int(longitude // 30)
        pos_in_sign = longitude - (sign_num * 30)
        deg = int(pos_in_sign)
        full_min = (pos_in_sign - deg) * 60
        minute = int(full_min)
        full_sec = round((full_min - minute) * 60)

        deg = "{:02d}".format(deg)
        minute = "{:02d}".format(minute)
        full_sec = "{:02d}".format(full_sec)

        return f"{deg}° {minute}' {full_sec}"

    def generate_planet_data(self):
        planet_data = []
        for planet in const.LIST_OBJECTS:
            pl = self.chart.getObject(planet)
            hs = self.chart.houses.getObjectHouse(pl)
            planet_data.append({
                'id': pl.id,
                'sign': pl.sign,
                'lon': self.decimal_to_dms(pl.lon),
                'house': hs.id,
                'element': pl.sign
            })
        return pd.DataFrame(planet_data)
    
    def generate_house_data(self):
        house_data = []
        for house in const.LIST_HOUSES:
            hs = self.chart.get(house)
            
            house_data.append({
                'name': hs.id,
                'degrees': self.decimal_to_dms(hs.lon),
                'sign': hs.sign,
                'condition': House.condition(hs)
            })
        return pd.DataFrame(house_data)
    
    def generate_aspect_list(self):

        asplist = ObjectList(self.chart.getObjects())
        
        for obj in asplist:
            print(obj)

        return asplist
    
    def generate_aspect_data(self):
        # Loop through all objects in const.LIST_OBJECTS
        aspect_data = []
        for i, obj1_id in enumerate(const.LIST_OBJECTS):
            obj1 = self.chart.get(obj1_id)
            for obj2_id in const.LIST_OBJECTS[i+1:]:  # Start from the next planet in the list
                obj2 = self.chart.get(obj2_id)
                # Get the aspect
                aspect = aspects.aspectType(obj1, obj2, const.MAJOR_ASPECTS)

                aspect_data.append({
                    'obj1': obj1_id,
                    'obj2': obj2_id,
                    'aspect': aspect
                })

        return pd.DataFrame(aspect_data)


    def generate_accidental_dignities(self):
        planet_accidental = []
        for planet in const.LIST_OBJECTS:
            pl = self.chart.getObject(planet)
            sun = self.chart.get(const.SUN)
            haiz = 'N/A'
            if pl.id in const.LIST_SEVEN_PLANETS:
                haiz = accidental.haiz(pl, self.chart) if accidental.haiz(pl, self.chart) else 'N/A'
            planet_accidental.append({
                "id": pl.id,
                "Relation": accidental.sunRelation(pl, sun) or 'N/A',
                "Augmenting": accidental.light(pl, sun) or 'N/A',
                "Orientality": accidental.orientality(pl, sun) or 'N/A',
                'halz': haiz,
                "Peregrine": essential.EssentialInfo(pl).isPeregrine(),
            })
        return pd.DataFrame(planet_accidental)

    def generate_essential_dignities(self):
        essential.setTerms("Lilly Terms")
        essential.setFaces("Triplicity Faces")
        planet_essential = []
        for planet in const.LIST_OBJECTS:
            pl = self.chart.getObject(planet)
            planet_essential.append({
                "id": pl.id,
                "Exalted": essential.exalt(pl.sign),
                "Exile": essential.exile(pl.sign),
                "Domicile": essential.ruler(pl.sign),
                "Fall": essential.fall(pl.sign),
                "Triplicity": essential.dayTrip(pl.sign) + "/" + essential.nightTrip(pl.sign),
                "Term": essential.term(pl.sign, pl.lon % 30),
                "Face": essential.face(pl.sign, pl.lon % 30),
                "Peregrine": essential.isPeregrine(pl, pl.sign, pl.lon % 30)
            })
        return pd.DataFrame(planet_essential)

    def generate_prompt(self, question):
        planet_objects = self.generate_planet_data()
        planet_houses = self.generate_house_data()
        planet_asplist = self.generate_aspect_list()
        planet_accidental = self.generate_accidental_dignities()
        planet_essential = self.generate_essential_dignities()
        planet_aspects = self.generate_aspect_data()

        print(planet_asplist)

        prompt = f"""
        Horary Question: {question}

        Preliminary Evaluation:
        - Determine if the chart is radical and appropriate for the question asked.
        - Check the Moon's condition and its aspects to assess the question's viability.
        - Identify any strictures against judgment, such as the Moon being void of course.

        If the question is deemed valid, proceed with the astrological analysis. Otherwise, explain why the question cannot be answered.

        Astrological Data:
        {{
            "planets": {planet_objects.to_string()},
            "houses": {planet_houses.to_string()},
            "aspects": {planet_aspects.to_string()},
            "essential_dignities": {planet_essential.to_string()},
            "accidental_dignities": {planet_accidental.to_string()}
        }}

        Instructions (if question is valid):
        1. Identify the main significators based on the horary question and the houses involved.
        2. Analyze the condition of the main significators using the provided essential and accidental dignities.
        3. Examine the aspects between the main significators and other relevant planets.
        4. Consider the houses related to the question and their rulers.
        5. Synthesize the information to provide a coherent and meaningful interpretation.

        Important:
        - Base your interpretation solely on the provided astrological data.
        - Do not make assumptions or refer to positions not explicitly mentioned.
        - Adhere to traditional horary principles and avoid modern or unverified techniques.

        Interpretation (if question is valid):
        [LLM generates the interpretation here, following the given instructions and guidelines]
        """

        return prompt
# Usage
astro_chart = AstrologyChart("1984/06/23", "07:51", "+02:00", "52e22", "6e27")
question = "Why is Mike silent and does not react on any messages?"
prompt = astro_chart.generate_prompt(question)

print(prompt)