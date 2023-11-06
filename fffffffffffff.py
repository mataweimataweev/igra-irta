import json


personage = {
    'first': 'John',
    'second': 'Mary',
    'third': 'Mike',
    'fourth': 'Liza',
    'fifth': 'Tom'

}

with open('personage.json', 'w') as file:
    json.dump(personage, file, indent=4)


with open('personage.json', 'r') as file:
    personage = json.load(file)
del personage["third"]

with open('friend.json', 'w') as file:
     json.dump(personage, file, indent=4)

import csv

personage = [
    ['John'],
    ['Mary'],
    ['Mike'],
    ['Liza'],
    ['Tom']
]
with open('friend.csv', 'w', newline = '') as file:
    writer = csv.writer(file)

    for frrr in personage:
        writer.writerow(frrr)