#! /usr/bin/env python
import os
import glob  
import shutil 

target_dir = '/date/roverzon/01_Dispersion_Functional_Anal/Opt_collection'
target_dir_stack = []
dir_path = [ ] 

for root, dir, files in os.walk( target_dir ):
	target_dir_stack.append( dir ) 

target_dir_stack =  sorted( target_dir_stack[0] ) 

for i in  target_dir_stack:
	new_path = os.path.join( target_dir , i )  
	dir_path.append( new_path )

#for i in target_dir_stack:
#	print i[0] 
#print dir_path 

path = '/date/roverzon/01_Functional_Assesement/Optimized_Counterpois_Collection'

dir_stack = [] 

for root, dir, file in os.walk(path):
	if dir:
		dir_stack.append(dir)

dir_stack = sorted(dir_stack[0])   

for i in dir_stack:
#	print i[0] 
	new_path = os.path.join(path,i) 
	os.chdir( new_path ) 
	files = glob.glob('*.com')
	for f in files:
		for dir in target_dir_stack:
			if f[0] == dir[0]:
				try:
					src = os.path.join( new_path , f )
					targ = os.path.join( target_dir + '/' + dir, 'Optimized_Geom_Counterpoise')
#					shutil.copy( src , targ ) 
#					  new_path + '/' +  f , target_dir + '/' + dir + '/' + 'Optimized_Geom_Counterpoise'    
#                                print   + '/' + f , target_dir + '/' + dir 
				except: 
					print 'error'
#		
#	print files 
	


