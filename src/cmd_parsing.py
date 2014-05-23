import sys 

standard_input = { 0 : 'input_file_number',
                   1 : 'input_formate',
                   2 : 'input_type'                           
                 }

standard_output = { 0 : 'output_file_formate',
                    1 : 'output_file_mrg',
                    2 : 'output_number_of_files',                        
                 }

def cmd_split( file_name ):
    fp = open(file_name)
    cmd_stack = []
    count = 0
    try:
        while True:
            line_text = fp.readline()
            if not line_text:
                break
            else:
                cmd_stack.append(line_text)
                count += 1
                if count > 200:
                    break

                else:
                    continue 
    except:
        print "Eorr"
    return cmd_stack 

def variable_dict(in_file ,out_file, file_stack):
    stack = [in_file,out_file]
    return_dict = []
    for parts in stack:
        tmp_array = []
        for i in range(len(parts)):
            try:
                tmp_array.append((parts[i].split('=')[0][1:].lower(),parts[i].split('=')[1].lower()))
            except:
                continue 
        return_dict.append(dict(tmp_array))
        tmp_array[:] = [] 
    return return_dict
    
def command_indentifyer(cmd_stack, standard_dict):
    try:
        num_standard_input = len(standard_dict)
        num_cmd_stack = len(cmd_stack)
        if num_standard_input != num_cmd_stack:
            print "Commands Error 1 "
        else:
            new_cmd_stack = sorted(cmd_stack)
            for i_cmd in range(len(new_cmd_stack)):
                if new_cmd_stack[i_cmd].split('=')[0].lower()[1:] != standard_dict[i_cmd]:
                    print "Commands Error 2 "
                    return 1
                else:
                    continue
        return 0 
    except:
        print "Error"

def resolve_cmd( cmd_stack ):
    new_cmd_stack = []
    record = [] 
    space_count = 0 
    for i in range(len(cmd_stack)):
        if cmd_stack[i] == '\n':
            record.append(i)
            space_count += 1
        new_cmd = cmd_stack[i].strip().replace(" ", "") 
        new_cmd_stack.append(new_cmd)
     
    input_part  =  new_cmd_stack[:record[0]]
    output_part =  new_cmd_stack[record[0]+ 1:record[1]]
    file_stack  =  new_cmd_stack[record[1]+ 1:]

    for i in range(len(input_part)):
        if input_part[i].split('=')[0][0] != '%':
            print "Input Error: Line: "  + str(i+1) + " without % symbol" 
        else:
            continue
        
    for i in range(len(output_part)):
        if output_part[i].split('=')[0][0] != '%':
            print "Input Error: Line: "  + str(i+1) + " without % symbol" 
        else:
            continue
    
    for trg in range(len([input_part,output_part])):
        if trg == 0:
            t = command_indentifyer(input_part,standard_input)
            if t == 1:
                raise SystemExit("Error")
        elif trg == 1:
            command_indentifyer(output_part,standard_output)
            
    input_dict , output_dict = variable_dict(input_part,output_part, file_stack )

    return (input_dict , output_dict, file_stack)  
 
        
if __name__ == '__main__':
    cmd_file = 'cmd_file.txt'
    fp = open(cmd_file)
    cmd_stack = []
    count = 0
    try:
        while True:
            line_text = fp.readline()
            if not line_text:
                break
            else:
                cmd_stack.append(line_text)
                count += 1
                if count > 200:
                    break
                else:
                    continue 
    except:
        print "Eorr"

    resolve_cmd(cmd_stack)
