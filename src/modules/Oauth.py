from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class Oauth:

    def __init__(self, creds_module):
        self.creds_module = creds_module

    def login(self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(self.creds_module)
        if gauth.access_token_expired:
            gauth.Refresh()
            gauth.SaveCredentialsFile(self.creds_module)
        else:
            gauth.Authorize()

        return GoogleDrive(gauth)


