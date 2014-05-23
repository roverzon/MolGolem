#! /usr/bin/env python 
import os 
import glob 
import subprocess
import re 

files = glob.glob('*.log')

file_name = 'geometies_collection.txt'
file = open( file_name, 'w')

counter = 0 
for f in files:

#        file = open( file_name, 'w')

	try:	
		print f 
#		file = 'b_h2o_nh3_B2PLYPD_Opt.out'

		file_text = subprocess.check_output(['grep','-B 18',' Rotational', f])

		text  =  file_text.split('Rotational') 

		file_name = 'geometies_collection.txt'

#		file = open( file_name, 'w')

		file.write( f + '\n')

		for i in  text[-2].split('\n')[4:-2] : 
			file.write( i  + '\n')

		file.write('\n') 
#		break 
	except:
		print "error"
	 
	counter += 1 
file.close() 
print counter 
