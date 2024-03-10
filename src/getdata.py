from Oauth import Oauth


def getdata(file_id, credentials, destination):

    service = Oauth(credentials)
    service = service.login()

    # Descargar el archivo zip
    file = service.CreateFile({'id':file_id})
    file_name = file['title']
    file.GetContentFile(destination+file_name)
    return file_name

