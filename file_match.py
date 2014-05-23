#! /usr/bin/env python 
import numpy as np 
import subprocess 
import os 

def coordinate_exame( opt_log_file , counterpoise_input_file , n):
#	file = 'd_mea_nh3_M06-L_Opt.log'
#	print opt_log_file , counterpoise_input_file 
	key_word = 'Standard orientation'
	key_word_2 = 'Input orientation'
	number_of_atoms = n 
	unit_line = number_of_atoms + 4 
	try:
		raw_text = subprocess.check_output(['grep','-A',str(unit_line), key_word , opt_log_file])
	except:
        	raw_text = subprocess.check_output(['grep','-A',str(unit_line), key_word_2 , opt_log_file]) 

	text =  raw_text.split('---')[-1]
	new_text = text.split('\n')
	new_text.pop(0) , new_text.pop()

#	print new_text 
	a = [] 

	for t in new_text:
		 a.append(t.split('          ')[1]) #+   
	 	 a = a + t.split('          ')[-1].split('   ')[-3:] 

	coord_1 = np.array(a)
#	print len(coord_1) 
	coord_1.shape = number_of_atoms , 4
#	file_2 = 'MEA_NH3_CAM-B3LYP_CounterPoise.com'
	fp = open(counterpoise_input_file)
	file_text = fp.read()
	text =   file_text.split('\n')[8:-2] 
#	print text 
	b = []
	try:
		for t in  text:
#			print t 
			new_t =  t.split('\t') 
#			print new_t 
			new_t.pop()
#			print new_t 
	 
			if   new_t[0] == 'O':
				new_t[0] = '8'
			elif new_t[0] == 'H':
				new_t[0] = '1' 
			elif new_t[0] == 'C':
				new_t[0] = '6' 
			elif new_t[0] == 'N':
				new_t[0] = '7'
			b = b + new_t
		   
	except:
		new_list = []
		for t in text:
			new_t = t.split(' ')
#	       		print new_t 
			new_t.pop() 
#			print new_t
			for i in new_t:
				if i:
					if   i == 'O':
						i = '8'
					elif i == 'N':
						i = '7' 
					elif i == 'C':
						i = '6' 
					elif i == 'H':
						i = '1' 
					new_list.append( i )  
				else:
					continue 
		if  new_list[-1]:
			pass 
		else:
			new_list.pop()	
		b =  new_list 
			
	new_b = []	 	
	for e in range(len(b)):
		if b[e]:
			new_b.append(b[e])
		else:
			continue
	b = new_b 	
#	print b 
	coord_2 = np.array(b)
	coord_2.shape = number_of_atoms ,4 

#	print coord_1 	
#	print coord_2 

	total_sum = 0 
	for i in range(len(coord_2)): 
		raw_sum = 0 
		for j in range(4):
			diff = float(coord_1[i][j]) - float(coord_2[i][j])
#			print diff 
			raw_sum += diff 
		total_sum += raw_sum 
	
	if total_sum == 0:
		print  opt_log_file.split('/')[-1] , counterpoise_input_file.split('/')[-1]  + '\t' +'Two files are totally matched' 
	else:
		if total_sum < 10**(-5):
	                print  opt_log_file.split('/')[-1] , counterpoise_input_file.split('/')[-1]  + '\t' +'Two files are totally matched'
		else:
			print  opt_log_file.split('/')[-1] , counterpoise_input_file.split('/')[-1]  + '\t' +'Something must be wrong, Total Sum: ' + str( total_sum )  

def label_to_number( label ):
	number = ''
	if   label == 'a':
		number = 3 + 3 
	elif label == 'b':
                number = 3 + 4 
	elif label == 'c':
                number = 11 + 3
	elif label == 'd':
                number = 11 + 4
	elif label == 'e':
                number = 18 + 3
	elif label == 'f':
                number = 18 + 4
	elif label == 'g':
                number = 11 + 11
	elif label == 'h':
                number = 11 + 18
	elif label == 'i':
                number = 18 + 18
	elif label == 'j':
                number = 4 + 3
	elif label == 'k':
                number = 11 + 3
	elif label == 'l':
		number = 18 + 3
	return number 

def examine_the_convergance( log_file ):
	try:
		text = subprocess.check_output(['tail', log_file ]).split('\n')[-2]
	 
		if text.split(' ')[1] != 'Normal':
        		print fp + ' is not normal termination '
        	else:
        		print text
	except:
		print "error"
	

if __name__ == '__main__':
	file_name = 'table.txt'
	fp = open(file_name)
	file_text = fp.read()
	text_list = file_text.split('\n')
	text_list.pop()
	
	src_dir = './'
	targ_dir = os.path.join(src_dir,'Optimized_Geom_Counterpoise')
	
	counter = 0 
	number_of_atoms = label_to_number(text_list[0][0][0])  
	for f in  text_list :
        	files_pair =  f.split(',') 
	      	src = src_dir + files_pair[0] 
		targ =  targ_dir + '/' + files_pair[1]
	        
	#	print src , targ 
		try:
			coordinate_exame( src , targ ,number_of_atoms )
			examine_the_convergance( src )
			counter += 1 
#			break 
		except:
			print files_pair
			continue 
#			break 
	
	print "Total " + str(counter) + " Jobs are in processes "
