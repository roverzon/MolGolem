#! /usr/bin/env python 

file_name = "mea_8_co2_4_hb_record.txt"
fp = open(file_name)
file_text = fp.read().split('\n')
x = [] 
y = [] 
for f in file_text:
	new_f = f.split(',')
	try:
		x.append( new_f[0] ) , y.append( new_f[1] )
	except:
#		continue 
		len_x = len(x) 
		len_y = len(y)
		if len_x != len_y:
			if len_x < len_y:
				x.append(0)
			elif len_y < len_x:
				y.append(0)  
 
	
print x 
print y 
print len(x), len(y) 

 

