from getdata import getdata
from getdata import getdata
from unzip import unzip_file
from q1_memory import q1_memory
import q1_time
import q2_time
from q2_memory import q2_memory
from q3_memory import q3_memory
import q3_time


if __name__ == "__main__":
    """" define los datos para enviar a google drive y descargar la data """
    credentials = 'credentials_module.json'
    data_dir = 'data/'
    file_id = '1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis'

    datafile = getdata (file_id, credentials, data_dir)

    if datafile:
        """" descomprime el archivo procede a leerlo y hacer el challenge"""
        jsondatafile = unzip_file(data_dir+datafile, data_dir)
        jdfile_name = data_dir+jsondatafile[0].filename
        q1_memory_optimize = q1_memory(jdfile_name)
        print(q1_memory_optimize)
      #  q2_memory(jdfile_name)
      #  q3_memory(jdfile_name)

    else:
        """" si no existe proporciona el link de descarga"""
        print('Go to https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing in order to download file')
