#! /usr/bin/env python 
file = "mea_8_co2_1_hb_record.txt"
t_file = "mea_8_co2_1_hb_record_tmp.txt"
fp = open(file)
fp_1 = open(t_file,"w")
text = fp.read().split('\n')
count = 0 
for t in text:
	new_t = t.split(',')
	try:
		fp_1.write( str(count) + ' , ' + str(new_t[1]) + "\n")  
	except:
		continue 
	count +=1 

	
