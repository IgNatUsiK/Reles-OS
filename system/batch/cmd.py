import os

while True:
	cmd = input("$ ")
	if cmd == "exit":
		break
	else:
		os.system(cmd)
	pass