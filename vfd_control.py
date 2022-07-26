"""
######################################################################

Simple Modbus Sensor Polling Code
Coded By "The Intrigued Engineer" over a coffee

Minimal Modbus Library Documentation
https://minimalmodbus.readthedocs.io/en/stable/

Thanks For Watching!!!

######################################################################
"""

import minimalmodbus
import user_inputs
import Modbus_Settings as MB
import stat_window as stat
from time import sleep 
import os
import sys



drive_set = False
speed_set = False
drive_package = 0
speed_package = 0


write_start = MB.control_offset-40001


while True:
	
	
	
	
	
	if drive_set == False:
		drive_package = user_inputs.get_user_drive()
	if drive_package == "Drive Error":
		print("")
		print("Drive Mode Not Recognised")
		print("")
		drive_set = False
	else:
		print("")
		print(f"Drive mode set to {drive_package}")
		print("")
		drive_set = True

			
	if drive_set == True and speed_set == False:
		speed_package = user_inputs.get_user_speed()
		if speed_package == "NaN":
			print("")
			print("Speed entered is not a number")
		elif speed_package == "OL":
			print("")
			print("Speed Under/Over Limits")
		else:
			print("")
			print(f"Speed set to {speed_package}")
			speed_set = True
			
	if drive_set == True and speed_set == True:
		user_inputs.send_to_vfd(drive_package, speed_package, write_start)
	
	while drive_set and speed_set:
		os.system('cls' if os.name == 'nt' else 'clear')
		stat.read_VFD()
		drive_set = False
		speed_set = False
		os.system('cls' if os.name == 'nt' else 'clear')
		
		
		
		

		


