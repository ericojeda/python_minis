from __future__ import print_function

from terminaltables import SingleTable

import json
from roller import parse_dice
from random import randint, choice

def get_mod(a):
	mod = (int(a) - 10) // 2
	return mod

challenge = raw_input("Challenge Rating: ")

with open('5e-SRD-Monsters.json') as data_file:    
    data = json.load(data_file)

all_monsters = data['monsters']
filtered_monsters = []

for (i, item) in enumerate(all_monsters):
	if (item['challenge_rating'] == challenge):
		filtered_monsters.append(i)

monster = all_monsters[choice(filtered_monsters)]

hit_points = parse_dice(monster['hit_dice'])

speed = monster['speed'].replace(', ', '\n')

stat_block_1 = (
	('AC', 'SPEED', 'HP'),
	(monster['armor_class'], speed, hit_points),
)

stat_block_2 = (
	('STR', 'DEX','CON','INT', 'WIS', 'CHR'),
    (get_mod(monster['strength']), get_mod(monster['dexterity']), get_mod(monster['constitution']), get_mod(monster['intelligence']), get_mod(monster['wisdom']), get_mod(monster['charisma']))
)


title = monster["name"]

# SingleTable.
table_instance_1 = SingleTable(stat_block_1, title)
print(table_instance_1.table)

table_instance_2 = SingleTable(stat_block_2)
print(table_instance_2.table)