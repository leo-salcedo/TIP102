def print_catchphrase(character):
	dictionary = {"Pooh": "Oh bother!", "Tigger": "TTFN: Ta-ta for now!", "Eeyore": "Thanks for noticing me.", "Christopher Robin": "Silly old bear."}
	if character in dictionary:
		print(dictionary[character])
	else:
		print("Sorry! I don't know " + character + "'s catchphrase!")
		
character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)