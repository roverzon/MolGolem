#! /usr/bin/env python 
import os 
import re 
import glob 
import shutil

directory_name = [ 'b_NH3_H2O_Opted_collection','c_MEA_H2O_Opted_collection',
                   'd_MEA_NH3_Opted_collection','e_DEA_H2O_Opted_collection','f_DEA_NH3_Opted_collection',
                   'g_MEA_MEA_Opted_collection','h_MEA_DEA_Opted_collection','i_DEA_DEA_Opted_collection',
                   'j_NH3_CO2_Opted_collection','k_MEA_CO2_Opted_collection','l_DEA_CO2_Opted_collection' ]

path = '/date/roverzon/01_Dispersion_Functional_Anal/Opt_collection/'

directory = []

create_dir = 'Optimized_Geom_Counterpoise'

create_dir_destiny = [] 

for rn in directory_name: 
	directory.append( os.path.join( path , rn ) ) 

for cp in directory:
	dir = os.path.join(cp,create_dir)
	try :
#		os.makedirs(dir)
		create_dir_destiny.append(dir)
	except:
		continue 
#print create_dir_destiny 

target_dir_name = [ 'H2O_NH3_MP2_Geom_Anal', 'MEA_H20_MP2_Geom_Anal' , 'MEA_NH3_MP2_Geom_Anal',
		    'DEA_H2O_MP2_Geom_Anal', 'DEA_NH3_MP2_Geom_Anal' , 'MEA_Dimer_MP2_Geom_Anal',
		    'DEA_MEA_MP2_Geom_Anal', 'DEA_Dimer_MP2_Geom_Anal','NH3_CO2_MP2_Geom_Anal',
		    'MEA_CO2_MP2_Geom_Anal', 'DEA_CO2_MP2_Geom_Anal']

starting_path = '/date/roverzon/01_Dispersion_Functional_Anal'

dir = []

regex = '(.*?)_CounterPoise'
pattern = re.compile(regex)


for tp in target_dir_name :
	waking_path = os.path.join(starting_path,tp) 
	for a , b , c in os.walk( waking_path ):
		dir.append( b  )

counter_name = [] 

for i in dir:
	for j in i:
		if j != 0:
			counter_name.append( j )
#			print j 
test = [] 

#print counter_name 

for i in range(len(counter_name)):
	if re.match( pattern , counter_name[i] ):
		test.append(counter_name[i])

#print test 

dir_stack = [ ] 
	 
for i in range(len(target_dir_name)):
	try:
		dir = os.path.join(starting_path, target_dir_name[i])
		new_dir = os.path.join(dir,test[i])
		dir_stack.append( new_dir ) 
	except:
		print 'error' 

#print dir_stack 
#print create_dir_destiny 

for i in range(len(dir_stack)):
	os.chdir(dir_stack[i])
	files = glob.glob('*.com')
#	print files #	
	for j in files: 
#		print dir_stack[i] + '/' + j 
#		print create_dir_destiny[i]
#		shutil.copy( dir_stack[i] + '/' + j, create_dir_destiny[i])


#print len(dir_stack)
#print len(create_dir_destiny)

