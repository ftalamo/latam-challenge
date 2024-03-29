import os
from modules.getdata import getdata
from modules.unzip import unzip_file
from q1_memory import q1_memory
from q1_time import q1_time
from q2_memory import q2_memory
from q2_time import q2_time
from q3_memory import q3_memory
from q3_time import q3_time


if __name__ == "__main__":
    """" define los datos para enviar a google drive y descargar la data """
    credentials = 'credentials_module.json'
    data_dir = 'data/'
    file_id = '1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis'

    '''verifica que exista el archivo antes de ir a buscarlo en drive'''
    datafile = 'data/farmers-protest-tweets-2021-2-4.json'
    if os.path.exists(datafile):
        '''si existe el archivo copia el nombre'''
        jdfile_name = datafile
    else:
        '''descarga el archivo y lo descomprime desde drive'''
        try:
            datafile = getdata(file_id, credentials, data_dir)
            jsondatafile = unzip_file(data_dir + datafile, data_dir)
            jdfile_name = data_dir + jsondatafile[0].filename
        except Exception as e:
            print(f"error: {e}")
            print('Por favor ve al link https://drive.usercontent.google.com/download?id=1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis&export=download&authuser=0 y descarga de forma manual el archivo')

    q1_memory_optimize = q1_memory(jdfile_name)
    print(f"q1_memory result: {q1_memory_optimize}")
    q1_time_optimize = q1_time(jdfile_name)
    print(f"q1_time result: {q1_time_optimize}")
    q2_memory_optimize = q2_memory(jdfile_name)
    print(f"q2_memory result: {q2_memory_optimize}")
    q2_time_optimize = q2_time(jdfile_name)
    print(f"q2_time result: {q2_time_optimize}")
    q3_memory_optimize = q3_memory(jdfile_name)
    print(f"q3_memory result: {q3_memory_optimize}")
    q3_time_optimize = q3_time(jdfile_name)
    print(f"q3_time result: {q3_time_optimize}")




