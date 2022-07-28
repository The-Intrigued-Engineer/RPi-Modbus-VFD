"""
######################################################################

VFD Control Over Modbus Code
Coded By "The Intrigued Engineer" over a few coffees

Minimal Modbus Library Documentation
https://minimalmodbus.readthedocs.io/en/stable/

Link to LS-M100 Datasheet:
https://www.seva-tec.de/media/pdf/f5/58/72/SEVA-LS-M100-Manual-Frequency-Inverter.pdf

Thanks For Watching!!!

######################################################################
"""

## Import the related modules / libraries
import minimalmodbus 
import user_inputs
import Modbus_Settings as MB
import stat_display as stat
from time import sleep 
import os
import sys


## Set some flags we use to step through the data input and parsing
drive_set = False
speed_set = False
drive_package = 0
speed_package = 0


## Calculate what the register address that should be passed to minimal modbus should be
write_start = MB.control_offset-40001


## Main loop of the program

while True:
	
		# If its not already been set, get drive setting from user and assign it to the variable "drive_package"
	if drive_set == False:
		drive_package = user_inputs.get_user_drive()
		
		# If the data from the user is wrong then tell the user 
	if drive_package == "Drive Error":
		print("")
		print("Drive Mode Not Recognised")
		print("")
		drive_set = False
		
		# If there was no error then set the flag "drive_set" true and tell the user what it is set to
	else:
		print("")
		print(f"Drive mode set to {drive_package}")
		print("")
		drive_set = True

			
		# If the drive mode has been set but the speed has not yet been set the get the speed setting from user and assign it to "speed_package"
	if drive_set == True and speed_set == False:
		speed_package = user_inputs.get_user_speed()
		
		# If the functinon returns any of the various errors, tell the user what the error was
		if speed_package == "NaN":
			print("")
			print("Speed entered is not a number")
		elif speed_package == "OL":
			print("")
			print("Speed Under/Over Limits")
			
		# If there was no error then set the flag "speed_set" true and tell the user what it is set to 
		else:
			print("")
			print(f"Speed set to {speed_package}")
			speed_set = True
		
	# If the dirve mode and the speed have both been set correctly then pass on the drive and speed packages as well as the register position to the funcion to send to the VFD	
	if drive_set == True and speed_set == True:
		user_inputs.send_to_vfd(drive_package, speed_package, write_start)
	
	# If both drive and speed are set and the data has been sent to the VFD, then clear the screen and call the snazzy info display function
	if drive_set and speed_set:
		os.system('cls' if os.name == 'nt' else 'clear')
		stat.read_VFD()
		drive_set = False
		speed_set = False
		os.system('cls' if os.name == 'nt' else 'clear')
