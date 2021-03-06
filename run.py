logo = """

   ___                      
  / __|_ _ ___  _____ _____ 
 | (_ | '_/ _ \/ _ \ V / -_)
  \___|_| \___/\___/\_/\___|
                            

"""


import click
import time
import sys
import os
import subprocess
from colorama import init, Fore, Back, Style
init()

if sys.platform == "darwin":
	
	local = os.path.join(os.path.expanduser('~'), 'Groove/Local')
	shared = os.path.join(os.path.expanduser('~'), 'Groove/Shared')

	if not os.path.isdir(local) and not os.path.isdir(shared):
		os.makedirs(local)
		os.makedirs(shared)
		print "OS X Directory"
	else: 
		print "Welcome Back!"

elif sys.platform == "win32":
	print "Windows Directory"
	print "I'll add support for this soon."


@click.command()
def hello():
	print(Fore.WHITE + logo)

	holder = []

	for file in os.listdir(os.path.join(os.path.expanduser('~'), 'Groove/Local')):
		if file.endswith(".mp3"):
			print(Fore.CYAN + file)
			holder.append(file)

	print "\n"
	value = click.prompt('Lets get this arty started, or what?', type=int)
	print "\n"
	message = "Now Jamming - %s" % holder[value - 1]
	print(Fore.RED + message)
	
	os.chdir(str(os.path.join(os.path.expanduser('~'), 'Groove/Local/')))
	track_directory = os.path.join(os.getcwd(), holder[value - 1])
	return_code = subprocess.call(["afplay", track_directory])



if __name__ == '__main__':
	hello()