#!/usr/bin/env python
import subprocess 
import commands  
import re 

text = commands.getoutput('ls *.log')

list_of_file =  text.split('\n')

functional_database = ['B3LYPD-GD2','BLYPD-GD2','M05-2X','M052X','M06-L','M06L','wB97',
		       'wB97X','wB97XD','M06HF','M06-HF','M062X','M06-2X', 'B97-D','B97D',
		       'CAM-B3LYP','B2PLYP','B2PLYP-D','B2PLYPD','LC-wPBE','B3LYPD-GD3']

file_stacke = []

job_task = [ 'Counterpoise ' ]

count = 0 

for fp in list_of_file:
 
        new_i =  fp.split('.')

        tmp = new_i[0].split('_')
	

        for fn in tmp:
 
                if fn in  functional_database :
			try: 
             			file_name = fp.split(fn)[0] + fn +  fp.split(fn)[1]   		
#				
#				print file_name 
				arg = ' '
#				print fn[:3] 
 
				if fn == 'BLYPD-GD2':
					arg = 'RB-LYP'
				else:
					arg = fn[:3]

				energy_text = subprocess.check_output( ['grep', arg , file_name])
				
#				print energy_text 
				
                		if fn == 'B3LYPD-GD2':
                       			 key_word = 'RB3LYP'

				elif fn == 'BLYPD-GD2':
					key_word = 'RB\-LYP'

				elif fn == 'B3LYPD-GD3':
					key_word = 'RB3LYP'

				elif fn == 'B2PLYP-D':
					key_word = 'RB2PLYPD'

				elif fn =='B97-D':
					key_word = 'RB97D'

				elif fn == 'M05-2X':
					key_word = 'RM052X'

				elif fn == 'M06-L':
					key_word = 'RM06L'
			
				elif fn == 'M06-2X':
					key_word = 'RM062X'

				elif fn == 'M06-HF':
					key_word = 'RM06HF'

                		else:
                        		key_word = 'R' + fn

#				regex2 = r'E\((.*?)\) = (.*?) A.U.'
	               		regex = 'E\(' + key_word + '\) = (.*?) A.U. '
				
				
                		pattern = re.compile(regex)
				
                		results  = re.findall(pattern,energy_text)
		
#				print results  
                		binding_energy = 627.5*(float(results[0]) - float(results[1]) - float(results[2]))

                		print  fn + '  : ' +  str(round(binding_energy,2) )
        		except:
                		print "functional " + fn + " is failed"
			count += 1 

print str(count) + ' Jobs in the process ' 
print "Normal Termination"
         
