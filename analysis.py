#! /usr/bin/env python 
import numpy as np 

def average(array,total_num):
	total = 0 
	for i in np.arange(len(array)):
		total += array[i] 
	avg = float(total) / total_num
	return avg 

def error_bar(array,avg,total_num):
	new_array = []
	total = 0  
	for e in np.arange(len(array)):
		diff = array[e] - avg
		new_array.append(diff**2)
	for e in np.arange(len(new_array)):
		total += new_array[e] 

	error_rms = np.sqrt(total/(total_num-1))
	return error_rms

file_stack = ["mea_8_co2_1_hb_record.txt", "mea_8_co2_2_hb_record.txt" , "mea_8_co2_4_hb_record.txt" ]
for f in file_stack:
	count = 0 
	fp = open(f)
	text = [] 
	try:
		while True:
		        line_text = fp.readline().split('\n')[0]
			if not line_text:
				break 
			else:
                        	try:
                                	data = line_text.split(',')[1] 
                                	text.append(float(data)) 
                                	count +=1
                        	except:
					continue 
	except:
		print "error"	 
	avg =  average(text,count)
	error = error_bar(text,avg,count)
	print f +  " the average number of HB is: " + str(round(avg,4)) + " +- " + str(round(error,4))
