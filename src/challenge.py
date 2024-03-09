from getdata import getdata
from getdata import getdata
from unzip import unzip_file
from q1_memory import q1_memory
import q1_time
import q2_memory
import q2_time
import q3_memory
import q3_time


if __name__ == "__main__":
    """" lee el directorio data y verifica la existencia del archivo .zip """
    directory = 'data/'
    name = 'tweets.json.zip'
    path = directory+name
    if getdata(directory, name):
        """" descomprime el archivo procede a leerlo y hacer el challenge"""
        jfile = unzip_file(path, directory)
        q1_memory(directory+jfile[0].filename)

    else:
        """" si no existe proporciona el link de descarga"""
        print('Go to https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing in order to download file')
