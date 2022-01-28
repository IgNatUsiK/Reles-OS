##########################################################
#                        Reles OS                        #
#                  Created by IgNatUsiK                  #
#                     Version  1.0.5        Python 3.9.7 #
##########################################################


# Main libs
import os, shutil

# Menu
import selectmenu
from selectmenu import SelectMenu

# Colors
import system.libs.colors
from system.libs.colors import *
# Tools
import system.libs.tools
from system.libs.tools import *

# Start
print("Starting Reles...")
exec(open("system/config.ini", "r").read())
menu = SelectMenu()
color = system.libs.colors
tools = system.libs.tools

# Main
print("Welcome to Reles OS", version)
while True:
	print(color.wT, end = "")

	# Input command
	if debug == True:
		print(os.getcwd(), end = "")
	else:
		print("-", end = "")
	cmd = input(("> ")).split(sep = " ")
	form = cmd[0].split(sep = "-")

	# Formats
	fl = ["f", "file", "fl"]
	dl = ["d", "dir", "folder", "dr"]
	pl = ["p", "proj", "project", "pj"]

	# Standart Commands
	# Cmd: Stoping
	if cmd[0] == "stop":
		break

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
				print("[D]", i)
			for i in files:
				print("[F]", i)
			break

	# Cmd: Read
	elif cmd[0] == "read":
		files = os.listdir()
		menu.add_choices(files)
		select = menu.select()
		file = open(select, "r")
		print(file.read())
		file.close()


	# Commands with FORM
	# Form: Create
	elif form[0] == "cr":
		if form[1] in fl:
			file = open(cmd[1], "w")
			file.close()
			print(color.yT + f"Created file {cmd[1]}")
		elif form[1] in dl:
			os.mkdir(cmd[1])
			print(color.yT + f"Created folder {cmd[1]}")
		else:
			print(color.rT + f"Format not found")

	# Form: Delete
	elif form[0] == "dl":
		if form[1] in fl:
			os.remove(cmd[1])
			print(color.yT + f"Deleted file {cmd[1]}")
		elif form[1] in dl:
			shutil.rmtree(f"{cmd[1]}", ignore_errors = True)
			print(color.yT + f"Deleted folder {cmd[1]}")
		else:
			print(color.rT + f"Format not found")

	# Form: Rename
	elif form[0] == "rn":
		if form[1] in fl:
			os.rename(cmd[1], cmd[2])
			print(color.yT + f"Renamed file from {cmd[1]} to {cmd[2]}")
		elif form[1] in dl:
			os.rename(cmd[1], cmd[2])
			print(color.yT + f"Renamed folder from {cmd[1]} to {cmd[2]}")
		else:
			print(color.rT + f"Format not found")

	# Form: Move
	elif form[0] == "mv":
		if form[1] in fl:
			shutil.move(cmd[1], cmd[2])
			print(color.yT + f"Moved file from {cmd[1]} to {cmd[2]}")
		elif form[1] in dl:
			shutil.move(cmd[1], cmd[2])
			print(color.yT + f"Moved folder from {cmd[1]} to {cmd[2]}")
		else:
			print(color.rT + f"Format not found")

	# Form: Copy
	elif form[0] == "cp":
		if form[1] in fl:
			shutil.copy(cmd[1], cmd[2])
			print(color.yT + f"Copied file from {cmd[1]} to {cmd[2]}")
		elif form[1] in dl:
			shutil.copy(cmd[1], cmd[2])
			print(color.yT + f"Copied folder from {cmd[1]} to {cmd[2]}")
		else:
			print(color.rT + f"Format not found")

	# List commands
	elif cmd[0] == "help":
		print(f"{color.bT}\nStandart commands {color.wT}\n"
			  f"{color.cT}STOP{color.wT}         stop system\n"
			  f"{color.cT}VER{color.wT}          print version system\n"
			  f"{color.cT}CLEAR{color.wT}        clear command lines\n"
			  f"{color.cT}LIST{color.wT}         list files and directories\n"
			  f"{color.cT}DIR{color.wT}          directory now\n"
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
		# Error: Not found
		print(color.rT + f"Command not found")

# Stop
print("Stoping Reles...")