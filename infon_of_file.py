#! /usr/bin/env python
import os 
import glob 
import subprocess 
import re 

#file = 'H2O_H2O_B2PLYP_ATZ.out'
#text = subprocess.check_output(['tail',  file]).split('\n')[-2] 

path = './'

files_stack = []

for root, dirs, files in os.walk(path) :
	 files_stack.append(files)

file_stack =  sorted(files_stack[0] )

counter = 0 

for fp in file_stack:
	try:
		if  fp.split('.')[1] == 'log':
			text = subprocess.check_output(['tail', fp ]).split('\n')[-2]  
			print fp 
			if text.split(' ')[1] != 'Normal':
				print fp + ' is not normal termination '
			else:
				print text  
			counter += 1 
	except:	
		print fp 
	


print counter 
