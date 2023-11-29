#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unicorns import storage
from unicorns.Unicorn import Unicorn


storage.setup()

unicorns = storage.fetch_unicorns()
for unicorn in unicorns:
    print(str(unicorn.id) + ': ' + unicorn.name)
print("")

unicorn = storage.fetch_unicorn(3)
print(str(unicorn.id) + ': ' + unicorn.name)
print("Inrapporterad av: " + unicorn.reported_by)
print("")

unicorn.reported_by = 'Batman'
storage.update_unicorn(unicorn)
unicorn = storage.fetch_unicorn(3)
print(str(unicorn.id) + ': ' + unicorn.name)
print("Inrapporterad av: " + unicorn.reported_by)
print("")

unicorn = Unicorn()
unicorn.name = 'Konstig enhörning'
unicorn.description = 'Det här är ingen vacker enhörning'
unicorn.reported_by = 'Johan'
unicorn.spotted_where.name = 'Niagara'
unicorn.spotted_where.lat = 55.609183
unicorn.spotted_where.lon = 12.994875
unicorn.spotted_when = '2015-09-22 20:14:00'
unicorn.image = 'https://pbs.twimg.com/profile_images/512349801929650177/_hfDmaho.jpeg'
storage.add_unicorn(unicorn)
unicorn = storage.fetch_unicorn(5)
print(str(unicorn.id) + ': ' + unicorn.name)
print("")

unicorns = storage.fetch_unicorns()
print("Antal enhörningar: " + str(len(unicorns)))
storage.delete_unicorn(5)
unicorns = storage.fetch_unicorns()
print("Antal enhörningar: " + str(len(unicorns)))
