#! /usr/bin/env python 
import subprocess 

def identify_fragment_condition(beginning , end , number_of_atoms):
	number_of_atoms = int(number_of_atoms)
	number_of_fragment = number_of_atoms + 2 
	beginning = int(beginning)
	end = int(end) 
	end = end - beginning  
	number_of_lines = ( end + 1 ) * number_of_fragment 
	if end % 500 != 0:
		mode = end % 500 
		end = end - mode  
		if beginning % 500 == 0:
			start = (end + 1 ) * number_of_fragment + 1   
		else:
			start = (end  ) * number_of_fragment + 1 
	return [start , number_of_lines ]

file_stack = ['MEA_8_Bulk_NVT_BLYP-D_400K-pos-1.xyz.1','MEA_8_Bulk_NVT_BLYP-D_400K-pos-1.xyz.2','MEA_8_Bulk_NVT_BLYP-D_400K-pos-1.xyz.3','MEA_8_Bulk_NVT_BLYP-D_400K-pos-1.xyz.4']
 
for f in file_stack:
	try:
		print f 
		get_number_of_atoms = subprocess.check_output(['head','-n 1',f])
		get_text_i = subprocess.check_output(['grep','i',f])
		get_beggining_element =  get_text_i.split('\n')[0].split(',')[0].split(' ')[-1]  
		get_end_element = get_text_i.split('\n')[-2].split(',')[0].split(' ')[-1] 
		arange = identify_fragment_condition(get_beggining_element,get_end_element,get_number_of_atoms)
		cmd =   str(arange[0]) + ',' + str(arange[1]) + 'd' 
		fp = open('test.xyz','w')
		slice_file = subprocess.check_output([ 'sed', '-i', cmd , f ]) 
		fp.write(slice_file)
		fp.close() 
	except:
		print "error"
 
