Lists
-----

In some cases, instead of retrieving objects, houses or angles one by one, it may be useful to get direct access to
their lists. The *chart* object provides the following lists:

* *chart.objects*, with a list of all objects
* *chart.houses*, with a list of all houses
* *chart.angles*, with a list of all angles
 
The following example uses the ``for`` command to iterate over all objects in the list of objects
and displays the objects in the signs::

   >>> for obj in chart.objects:
   ...     print(obj)
   ...
   <Moon Sagittarius +22:22:54 +13:16:01>
   <Venus Aries +25:30:11 +01:12:41>
   <Saturn Sagittarius +04:55:45 +00:00:06>
   <Mercury Pisces +00:48:57 +01:29:49>
   <North Node Libra +11:08:28 -00:03:11>
   <Syzygy Virgo +14:50:23 +11:48:44>
   <Sun Pisces +22:47:25 +00:59:51>
   <South Node Aries +11:08:28 -00:03:11>
   <Pars Fortuna Gemini +03:03:00 +00:00:00>
   <Mars Aries +16:32:48 +00:45:18>
   <Jupiter Leo +13:38:37 -00:04:45>

The same can be done with the house positions::
   >>> for house in chart.houses:
   ...   print(house)
   ...
   <House1 Virgo +03:27:30 23.980997522531624>
   <House2 Virgo +27:26:22 28.84643085829299>
   <House3 Libra +26:17:09 33.03167124703552>
   <House4 Scorpio +29:19:03 34.19328854833313>
   <House5 Capricorn +03:30:39 31.811365039742384>
   <House6 Aquarius +05:19:20 28.136246784064383>
   <House7 Pisces +03:27:30 23.980997522531595>
   <House8 Pisces +27:26:22 28.84643085829299>
   <House9 Aries +26:17:09 33.03167124703551>
   <House10 Taurus +29:19:03 34.19328854833315>
   <House11 Cancer +03:30:39 31.811365039742384>
   <House12 Leo +05:19:20 28.13624678406434>
   
Lists also provides us with useful functions. 
For instance, the house list provides a function to retrieve the house where an object is::

   # for a list with objects in the houses
   >>> for obj in chart.objects:
   >>>   house = chart.houses.getObjectHouse(obj)
   >>>   print(f"The object {obj.id} is in {house}")
   
   
In this specific case, the sun is in the 7th house. 
The `lists.py`_ file provides a full overview of what is available for each list.  
