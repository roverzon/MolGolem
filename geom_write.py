#! /usr/bin/env python 
import os 
import glob 
import subprocess 

starting_path = '/date/roverzon/01_Dispersion_Functional_Anal/Opt_collection'
dir_stack = [] 
sub_dirs = []
dirs_walk = [] 
for root, dir, files in os.walk( starting_path ):
	if dir:
		dir_stack.append( dir )  

sub_dirs = sorted( dir_stack[1] )  
dir_stack = sorted( dir_stack[0] )	

#print dir_stack 

for s in dir_stack: 
	    new_path = os.path.join( starting_path  , s )
	    os.chdir( new_path )
	    files = glob.glob('*.out')
	    try:
		for f in files:
			file_text = subprocess.check_output(['grep', 'B 5 Rotational', f])	  
			print file_tesxt 
			break
	    except:
		print "error" 

  
	
	


