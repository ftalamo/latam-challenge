import os
from getdata import getdata
from unzip import unzip_file
from q1_memory import q1_memory
from q1_time import q1_time
from q2_memory import q2_memory
from q2_time import q2_time


if __name__ == "__main__":
    """" define los datos para enviar a google drive y descargar la data """
    credentials = 'credentials_module.json'
    data_dir = 'data/'
    file_id = '1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis'

    datafile = 'data/farmers-protest-tweets-2021-2-4.json'

    if os.path.exists(datafile):
        '''si existe el archivo copia el nombre'''
        jdfile_name = datafile
    else:
        '''descarga el archivo y lo descomprime desde drive'''
        datafile = getdata(file_id, credentials, data_dir)
        jsondatafile = unzip_file(data_dir + datafile, data_dir)
        jdfile_name = data_dir + jsondatafile[0].filename

    #q1_memory_optimize = q1_memory(jdfile_name)
    #print(q1_memory_optimize)
    #q1_time_optimize = q1_time(jdfile_name)
    #print(q1_time_optimize)
    q2_memory_optimize = q2_memory(jdfile_name)
    print (q2_memory_optimize)
    q2_time_optimize = q2_time(jdfile_name)
    print(q2_time_optimize)



