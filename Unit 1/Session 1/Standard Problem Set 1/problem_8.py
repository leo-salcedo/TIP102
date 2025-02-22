def print_todo_list(task):
	print("Pooh's To Dos:")
	cnt = 1
	for i in range(len(task)):
		print(str(cnt) + ". " + task[i])
		cnt += 1
	
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)