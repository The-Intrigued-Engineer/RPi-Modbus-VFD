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
import Modbus_Settings as MB

	## Create reading "instrument" called "turnie_boi" and import it's settings from the modbus settings module

turny_boi = minimalmodbus.Instrument(MB.USB_port,MB.mb_address )
turny_boi.mode = minimalmodbus.MODE_RTU
turny_boi.serial.parity = minimalmodbus.serial.PARITY_NONE
turny_boi.serial.baudrate = MB.baudrate
turny_boi.serial.bytesize = MB.bytesize
turny_boi.serial.stopbits = MB.stopbits		
turny_boi.serial.timeout  = MB.timeout
turny_boi.clear_buffers_before_each_transaction = MB.clear_buffers_before_call
turny_boi.close_port_after_each_call = MB.clear_buffers_after_call 


	## Create function for prompting the user to input a drive choice and returning the value to be given to the VFD drive command address
	## Returns the string "Drive Error" if the command is not understood

def get_user_drive():
	print("")
	print("")
	print("------------------------------------------")
	print("Input Drive Mode")
	print("----------------")	
	print("Forward = fwd, Reverse = rev, Stop = stop")
	print("------------------------------------------")	
	print("")
	print("Press Ctrl + C to Exit")
	drive_input = input()
	if drive_input == "fwd":
		return 2
	elif drive_input == "rev":
		return 4
	elif drive_input == "stop":
		return 1
	else:
		return "Drive Error"




	## Create function for prompting the user to input the desired RPM and returns the value to be given to the VFD frequency address
	## Returns the string "NaN" if the user input is not a number
	## Returns the string "OL" if the user input is outside the limits of 0-60Hz


def get_user_speed():
	print("")
	print("")
	print("------------------------------------------")
	print("Input Drive Speed")
	print("----------------")	
	print("Hirz between 0 - 60")
	print("------------------------------------------")	
	print("")
	print("Press Ctrl + C to Exit")

	speed_input= input()
	try:
		speed_int = int(float(speed_input)*100)
	except:		
		return "NaN"
	else:
		if isinstance(speed_int, int):
			
			if speed_int >=0 and speed_int <=6000:
				return speed_int
			else:				
				return "OL"
		else:
			return "NaN"



	## Create function for sending the input data to the VFD by casting the speed and drive mode 
	## to a list called "send_list" and passing this list and the write start address to the turny_boi call
	## Once set the port is closed

def send_to_vfd(drive_mode, speed, write_start):
	send_list = [speed,drive_mode]
	turny_boi.write_registers(write_start, send_list)
	turny_boi.serial.close()








