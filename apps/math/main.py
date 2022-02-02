import math
print("Print math string and press enter\nPrint 'exit' to break")
while True:
	try:
		math = input()
		if math == "exit":
			break
		print(math, "=", eval(math))
	except:
		print("Error")