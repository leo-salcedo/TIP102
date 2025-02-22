def final_value_after_operations(operations):
	tigger = 1
	for operation in operations:
		if operation == "bouncy" or operation == "flouncy":
			tigger += 1
		else:
			tigger -= 1
	return tigger



operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))