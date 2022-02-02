import os, time, keyboard
from colorama import Fore, Back, Style, init
from progress.spinner import Spinner
import selectmenu
from selectmenu import SelectMenu

def clear():
	os.system("cls||clear")
	pass

def click(key):
	print(f"\nClick {key} to continue...")
	keyboard.wait(key)
	pass

def bsod(error):	
	init()
	os.system("cls||clear")
	os.system("color 1F")

	print(f"""Fatal Error :(

A problem has been detected and Reles has been shut down to prevent damage
to your computer.

Error:
{error}

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Reles updates you might need
If problems continue, reinstall system...
	""")

	# Reloading...
	bar = Spinner('Reloading ', max = 40)
	j = 0
	while j < 40:
		j += 1
		bar.next()
		time.sleep(0.1)
	bar.finish()
	click("Space")
	clear()
	os.system("color 0F")
	return True

def menul(value):
	menu = SelectMenu()
	menu.add_choices(value)
	select = menu.select()
	return select

def sys_msg(message, color):
	print(Fore.WHITE, end = "")
	size = len(message) + 2
	j = 3
	print("┌", end = "")
	while j < size:
		print("─", end = "")
		j += 1
	print(f"[{Fore.RED}×{Fore.WHITE}]┐\n│{color}", message, f"{Fore.WHITE}│\n└", end = "")
	j = 0
	while j < size:
		print("─", end = "")
		j += 1
	print("┘")
	keyboard.wait("Enter")
