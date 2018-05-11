from roller import parse_dice
from colorama import init, Fore
import re

init(autoreset=True)

roll_pattern = re.compile("^([1-9]{1,4})(d)(4|6|8|10|12|20|100)$")
mod_pattern = re.compile("^([-+]?[0-9]{1,4})$")

def get_total(r,m):
	full_total = r + m
	return max(0, full_total)

while True:
	while True:
		response = raw_input("Roll Dice [1d20]: ") or "1d20"
		if (roll_pattern.match(response)) or (response == "exit"):
			break
		print "Invalid Input"
	if(response == "exit"):
		break

	while True:
		mod_response = raw_input("Modifier [0]: ") or "0"
		if (mod_pattern.match(mod_response)) or (mod_response == "exit"):
			break
		print "Invalid Input"

	if (mod_response == "exit"):
		break

	final_total = get_total(parse_dice(response, True), int(mod_response))

	print(Fore.YELLOW + "Modifier: " + mod_response)
	print(Fore.GREEN + "Total Roll: " + str(final_total))
	
	