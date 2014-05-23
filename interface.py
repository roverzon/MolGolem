import os
import sys 
from src import cmd_parsing
from src import files
from src import uv_spectrum_analyst
from src import data_output

current_path = os.getcwd()
sys.path.append(current_path)

cmd_file = 'cmd_file.txt'
cmd_stack = cmd_parsing.cmd_split(cmd_file)
input_cmds, output_cmds, file_names = cmd_parsing.resolve_cmd(cmd_stack)
##f_stack , residual_detail =
files.in_decomposition(input_cmds['input_formate'],file_names)
##selected_data = uv_spectrum_analyst.peak_selecting(f_stack)
##uv_data = uv_spectrum_analyst.uv_spectrum(f_stack)
##data = data_output.data_intergrat(file_names,residual_detail,selected_data)
##files.data_save(output_cmds,data)
##files.image_save(uv_data)
