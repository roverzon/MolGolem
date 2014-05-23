#!/usr/bin/env python
import subprocess
import commands
import re

text = commands.getoutput('ls *.out')

list_of_file =  text.split('\n')


functional_database = ['M05-2X','BLYP-D','B3LYP-D','M06-L']

file_stacke = []

for fp in list_of_file:
	tmp =  fp.split('.')
	if len(tmp) == 2:
		
		try: 
			file_name = fp
#		file_name  = 'DEA_H2O_M05-2X_CounterPoise.out'

			dft_energy_text = subprocess.check_output( ['grep', 'Total DFT energy' , file_name] )

			regex = 'Total DFT energy =    (.*?)\n'

			pattern = re.compile(regex)

			results  = re.findall( pattern , dft_energy_text )

			binding_energy = 627.5*(float(results[0]) - float(results[2]) - float(results[4]))

			print   file_name  + '  : ' +  str(round(binding_energy,2))
		except: 
			print 'error' 
 
 
