##########################################################
#                        Reles OS                        #
#                  Created by IgNatUsiK                  #
#                     Version  2.1.0        Python 3.9.7 #
##########################################################

try:

	# Main libs
	import os, shutil, time, subprocess

	# Colors
	import system.libs.colors
	from system.libs.colors import *
	# Tools
	import system.libs.tools
	from system.libs.tools import *
	# Texts
	import system.libs.texts
	from system.libs.texts import *

	# Start
	color = system.libs.colors
	tools = system.libs.tools
	texts = system.libs.texts

	# Load config
	exec(open("system/config.ini", "r").read())

	tools.clear()
	restart = False

	# Set Color
	os.system(sys_color)

	# Welcome
	print(texts.logo, end = " ")
	time.sleep(3)
	tools.clear()
	print(color.yT + "Write 'help' for list commands")

except Exception as error:
	try:
		restart = tools.bsod(error)
	except:
		print("Error Starting (BSOD is not load)")
		exit()

# Main
while restart != True:
	try:
		print(color.wT, end = "")

		# Input command
		if debug == True:
			print(os.getcwd(), end = "")
		else:
			print("-", end = "")
		cmd = input(("> ")).split(sep = " ")
		cmd[0] = cmd[0].lower()
		form = cmd[0].lower().split(sep = "-")

		# Standart Commands
		# Cmd: Stoping and Restaing
		if cmd[0] == "stop":
			restart = False
			break

		elif cmd[0] == "restart":
			restart = True
			break

		# Cmd: Clear
		elif cmd[0] == "clear":
			tools.clear()

		# Cmd: Change dir
		elif cmd[0] == "ch":
			os.chdir(cmd[1])

		# Cmd: Look dir
		elif cmd[0] == "dir":
			print(color.yT + os.getcwd())

		# Cmd: Version system
		elif cmd[0] == "ver":
			print(color.yT + "Version: " + version)

		# Cmd: Print string
		elif cmd[0] == "print":
			for i in cmd[1:]:
				print(color.yT + i, end = " ")
			print()

		# Cmd: List files
		elif cmd[0] == "list":
			for dirs,folder,files in os.walk(os.getcwd()):
				for i in folder:
					print(color.yT, "[D]", i)
				for i in files:
					print(color.wT, "[F]", i)
				break

		# Cmd: Read
		elif cmd[0] == "read":
			for dirs,folder,files in os.walk(os.getcwd()):
				break
			select = tools.menul(files)
			file = open(select, "r")
			print(f"{color.yT}=> {select}{color.wT}\n{file.read()}")
			file.close()

		# Cmd: App
		elif cmd[0] == "app":
			if cmd[1] == "list":
				for dirs,folder,files in os.walk("apps"):
					count = len(folder)
					if count > 0:
						print("App count:", count)
						for i in folder:
							print(color.yT, i)
					else:
						print(color.yT + "Apps not found")
					break
			else:
				if os.path.isfile(f"apps/{cmd[1]}/app.ini") == True:
					try:
						exec(open(f"apps/{cmd[1]}/app.ini", "r").read())
						print(color.yT + f"Name app:", color.mT + appName + color.yT,
							f"\nVersion app:",color.mT + appVersion + color.wT)
						exec(open(f"apps/{cmd[1]}/{mainFile}", "r").read())
						restart = False
					except:
						print(color.rT + "Error in app!")
				else:
					print("App not found or name is invalid")

		# Commands with FORM
		# Form: Create
		elif form[0] == "cr":
			if form[1] in ["f", "file", "fl"]:
				file = open(cmd[1], "w")
				file.close()
				print(color.yT + f"Created file {cmd[1]}")
			elif form[1] in ["f", "file", "fl"]:
				os.mkdir(cmd[1])
				print(color.yT + f"Created folder {cmd[1]}")
			else:
				print(color.rT + f"Format not found")

		# Form: Delete
		elif form[0] == "dl":
			if form[1] in ["f", "file", "fl"]:
				os.remove(cmd[1])
				print(color.yT + f"Deleted file {cmd[1]}")
			elif form[1] in ["f", "file", "fl"]:
				shutil.rmtree(f"{cmd[1]}", ignore_errors = True)
				print(color.yT + f"Deleted folder {cmd[1]}")
			else:
				print(color.rT + f"Format not found")

		# Form: Rename
		elif form[0] == "rn":
			if form[1] in ["f", "file", "fl"]:
				os.rename(cmd[1], cmd[2])
				print(color.yT + f"Renamed file from {cmd[1]} to {cmd[2]}")
			elif form[1] in ["f", "file", "fl"]:
				os.rename(cmd[1], cmd[2])
				print(color.yT + f"Renamed folder from {cmd[1]} to {cmd[2]}")
			else:
				print(color.rT + f"Format not found")

		# Form: Move
		elif form[0] == "mv":
			if form[1] in ["f", "file", "fl"]:
				shutil.move(cmd[1], cmd[2])
				print(color.yT + f"Moved file from {cmd[1]} to {cmd[2]}")
			elif form[1] in ["f", "file", "fl"]:
				shutil.move(cmd[1], cmd[2])
				print(color.yT + f"Moved folder from {cmd[1]} to {cmd[2]}")
			else:
				print(color.rT + f"Format not found")

		# Form: Copy
		elif form[0] == "cp":
			if form[1] in ["f", "file", "fl"]:
				shutil.copy(cmd[1], cmd[2])
				print(color.yT + f"Copied file from {cmd[1]} to {cmd[2]}")
			elif form[1] in ["f", "file", "fl"]:
				shutil.copy(cmd[1], cmd[2])
				print(color.yT + f"Copied folder from {cmd[1]} to {cmd[2]}")
			else:
				print(color.rT + f"Format not found")

		# List commands
		elif cmd[0] == "help":
			print(f"{color.bT}\nStandart commands {color.wT}\n"
				  f"{color.cT}STOP{color.wT}         stop system\n"
				  f"{color.cT}RESTART{color.wT}      restart system\n"
				  f"{color.cT}VER{color.wT}          print version system\n"
				  f"{color.cT}CLEAR{color.wT}        clear command lines\n"
				  f"{color.cT}LIST{color.wT}         list files and directories\n"
				  f"{color.cT}DIR{color.wT}          directory now\n"
				  f"{color.cT}APP{color.gT}   <name> {color.wT}run app from folder apps\n"
				  f"{color.cT}PRINT{color.gT} <mesg> {color.wT}print message\n"
				  f"{color.cT}CH{color.gT}    <path> {color.wT}change directory\n"
				  f"{color.cT}READ{color.gT}  <path> {color.wT}read file with select menu\n"
				  f"{color.bT}\nForm commands (Work for files and directories)\nUse command with '-' [cr-file file.txt]\n"
				  f"{color.cT}CR{color.gT} <path>        {color.wT}Create file and directory\n"
				  f"{color.cT}DL{color.gT} <path>        {color.wT}Delete file and directory\n"
				  f"{color.cT}RN{color.gT} <last> <new>  {color.wT}Rename file and directory\n"
				  f"{color.cT}MV{color.gT} <last> <new>  {color.wT}Move file and directory\n"
				  f"{color.cT}CP{color.gT} <main> <copy> {color.wT}Copy file and directory\n")

		else:
			path = os.path.isfile(f"system/batch/{cmd[0]}.py")
			if path == True:
				os.system(f"py system/batch/{cmd[0]}.py")
			else:
				# Error: Not found
				print(color.rT + f"Command not found")

	except Exception as error:
		try:
			restart = tools.bsod(error)
		except:
			print()

	except SyntaxError:
		try:
			restart = tools.bsod("Code error")
		except:
			print("Syntax error (BSOD is not load)")
			exit()

	except KeyboardInterrupt:
		print(color.rT + f"Keyboard Interrupt")

# Stop
try:
	if restart == False:
		print("Stoping Reles...")
		tools.clear()
	else:
		print("Restating Reles...")
		os.system("py main.py")
except:
	try:
		restart = tools.bsod("stoping error")
	except:
		print("Error stoping (BSOD is not load)")
		exit()