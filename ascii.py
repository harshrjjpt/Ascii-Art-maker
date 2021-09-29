from pyfiglet import figlet_format as nice
from termcolor import colored 
from colorama import init

init()

def art(word, color, style):
	colorplate = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
	answer = input(f"which word you want to convert into the art? : ")
	clr = input(f"which color you want to choose ? :")
	if clr not in colorplate:
		clr = "green"
	fnt = input(f"choose a font : 0,1,2,3,4,5,6 : ")
	font_plate = ["slant", "3-d", "3X5", "5lineoblique", "alphabet", "banner3-D", "doh"]
	design = font_plate[int(fnt)]
	result = nice(answer, font=design)
	print(colored(result, color = clr))

art("", "", "")

