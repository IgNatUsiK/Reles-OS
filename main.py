# Libs
import os, colorama, time, sys
from colorama import init, Fore, Style, Back

init()

# Functions
def parameters_db():
	try:
		path = os.path.isfile(f"{dirs['dir.system']}parameters.ini")
		if path == False:
			parameters = {
				"version": "1.5.1"
			}
			with open(f"{dirs['dir.system']}parameters.ini",'w') as ini:
				for key, value in parameters.items():
					ini.write(f'{key}:{value}\n')
		else:
			parameters = {}
			with open(f"{dirs['dir.system']}parameters.ini", "r") as ini:
				for i in ini.readlines():
					key, value = i.strip().split(':')
					parameters[key] = str(value)
		return parameters
	except:
		print(f"{warning_msg} Parameters error")
		parameters_db()

def settings_db():
	try:
		path = os.path.isfile(f"{dirs['dir.system']}settings.ini")
		if path == False:
			settings = {
				"debug": 1
			}
			with open(f"{dirs['dir.system']}settings.ini",'w') as ini:
				for key, value in settings.items():
					ini.write(f'{key}:{value}\n')
		else:
			settings = {}
			with open(f"{dirs['dir.system']}settings.ini", "r") as ini:
				for i in ini.readlines():
					key, value = i.strip().split(':')
					settings[key] = int(value)
		return settings
	except:
		print(f"{warning_msg} Settings error")
		settings_db()

def parameters_save(parameters, key, value):
	try:
		with open(f"{dirs['dir.system']}parameters.ini",'w') as ini:
				ini.write(f'{key}:{value}\n')
		return parameters
	except:
		print(f"{warning_msg} Parameters error")

def settings_save(settings, key, value):
	try:
		with open(f"{dirs['dir.system']}settings.ini",'w') as ini:
			ini.write(f'{key}:{value}\n')
		return settings
	except:
		print(f"{warning_msg} Settings error")

def system():
	sysfolder = os.path.isdir(dirs["dir.system"])
	appfolder = os.path.isdir(dirs["dir.system.apps"])
	libfolder = os.path.isdir(dirs["dir.system.libs"])
	path = os.path.isdir(dirs["dir.system"])
	if sysfolder == False:
		print(f"{warning_msg} No folder system...")
		os.mkdir(dirs["dir.system"])
	if appfolder == False:
		print(f"{warning_msg} No folder apps...")
		os.mkdir(dirs["dir.system.apps"])
	if libfolder == False:
		print(f"{warning_msg} No folder libs...")
		os.mkdir(dirs["dir.system.libs"])
	return path

def licence():
	licence = os.path.isfile("licence.lic")
	if licence == False:
		return False
	file = open("licence.lic", "r")
	licence = file.read()
	file.close()
	if licence != text_licence:
		return False

def clear():
	os.system('cls||clear')
	pass

# Vars
dirs = {
	"dir.system": "system/",
	"dir.system.apps": "system/app/",
	"dir.system.libs": "system/lib/"
}

icon = (
	f"{Fore.WHITE}"
	"### ### #   ### ###   ### ###\n"
	"# # #   #   #   #     # # #  \n"
	f"{Fore.CYAN}"
	"### ##  #   ### ###   # # ###\n"
	"##  #   #   #     #   # #   #\n"
	f"{Fore.BLUE}"
	"# # ### ### ### ###   ### ###\n"
	f"{Fore.WHITE}")

text_licence = (
	"(c) IgNatUsiK and Nova\n"
	"Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:\n"
	"1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.\n"
	"2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.\n"
	"3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission."
	)

shotdown = ("exit", "stop", "restart")

protection_msg = f"{Fore.GREEN}[Protection]{Fore.WHITE}"
error_msg = f"{Fore.RED}[Error]{Fore.WHITE}"
warning_msg = f"{Fore.YELLOW}[Warning]{Fore.WHITE}"
system_msg = f"{Fore.CYAN}[System]{Fore.WHITE}"

# Starting
system()
parameters = parameters_db()
settings = settings_db()
print(f"{system_msg} Starting Reles {parameters['version']}...")
clear()
print(icon)

# Operations
while True:
	try:
		system()
		parameters = parameters_db()
		settings = settings_db()
		lic = licence()
		if lic == False:
			print(f"{protection_msg} There is no license or it is not correct")
			break
		cmd = input(("-> "))
		cmd = cmd.split()
		if cmd[0] in shotdown:
			break
		elif cmd[0] == "clear":
			clear()
		elif cmd[0] == "version":
			print(f"{parameters['version']}")
		elif cmd[0] == "licence":
			file = open("licence.lic", "r")
			lic = file.read()
			print(f"{Style.BRIGHT}{lic}{Style.RESET_ALL}")
			file.close()
		elif cmd[0] == "app":
			app = ' '.join(cmd[1:])
			path = os.path.isfile(f"{dirs['dir.system.apps']}{app}.py")
			if settings["debug"] == 1:
				print(f"{system_msg} App search: '{app}'")
			if path == True:
				os.system(f"py {dirs['dir.system.apps']}{app}.py")
			else:
				print(f"{system_msg} App is None")
		elif cmd[0] == "set":
			settings_save(settings, cmd[1], cmd[2])
		elif cmd[0] == "param":
			parameters_save(parameters, cmd[1], cmd[2])
		else:
			path = os.path.isfile(f"{dirs['dir.system.libs']}{cmd[0]}.py")
			if path == True:
				os.system(f"py {dirs['dir.system.libs']}{cmd[0]}.py")
			else:
				print(f"{error_msg} Command or lib '{cmd[0]}' not found")
	except Exception as error:
		if settings["debug"] == 1:
			print(f"{error_msg} {error}")
		elif settings["debug"] == 2:
			print(f"{error_msg} {error}")
			break
	except KeyboardInterrupt:
		print("\n", end = "")
		if settings["debug"] == 1:
			print(f"{error_msg} No copy")

# Stoping
if cmd[0] == "restart":
	print(f"{system_msg} Restarting Reles...")
	os.system("py main.py")
else:
	print(f"{system_msg} Closing Reles...")