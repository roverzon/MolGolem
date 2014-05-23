#! /usr/bin/env python 

file_name = "test.xyz"
fp = open(file_name)
count = 0
text_stack = [] 
while True:
	file_text = fp.readline()
	if not file_text:
		break 
	else:
		text_stack.append(file_text.split('\n')[0].split('       '))
		count += 1 
		if count % 99 == 0:
			print text_stack[2:] 
			print "Operation" , len(text_stack[2:])  
			text_stack[:] = [] 
#print text_stack 
