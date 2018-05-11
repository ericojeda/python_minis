from __future__ import print_function
from colorama import init, Fore, Back
from terminaltables import SingleTable
import json
import random

init(autoreset=True)

def pick_five():
	choices = []
	nums = list(range(8))
	for i in range(5):
		index = random.randrange(len(nums))
		choices.append(nums[index])
		del nums[index]
	return choices

with open('puzzle_cars.json') as data_file:    
    data = json.load(data_file)

all_cars = data['cars']

choices = [all_cars[i] for i in pick_five()]

Car_Table = [
	['Order', 'Car']
]

for (i,item) in enumerate(choices):
	color = item['color'].upper()
	if color == 'WHITE':
		Car_Table.append([i + 1, getattr(Back, color) + Fore.BLACK + ' ' + item['color'] + ' ' + item['type'] + ' ' + Fore.RESET + Back.RESET])
	else:
		Car_Table.append([i + 1, getattr(Back, color) + ' ' + item['color'] + ' ' + item['type'] + ' ' + Back.RESET])

table_instance = SingleTable(Car_Table, 'Puzzle')
table_instance.justify_columns[0] = 'right'
print(table_instance.table)