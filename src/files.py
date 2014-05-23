from src import preprocessing
from src import data_output  

def in_decomposition( f_type , file_stack ):

    if f_type == "gausum":
        text_stack , detail_stack  = preprocessing.GauSun_file_split(file_stack)
        return text_stack , detail_stack

    elif f_type == "gaussian":
     	preprocessing.Gaussian_file_split(file_stack)



def data_save( out_cmds, data ):
	if out_cmds['output_file_mrg'] == 'on':
		mrg = 1 
	elif out_cmds['output_file_mrg'] == 'off':
		mrg = 0 
	if out_cmds['output_file_formate'] == 'excel':
		data_output.excel_sheet( out_cmds['output_number_of_files'] , mrg, data) 


def image_save(data):
	data_output.image(data)

