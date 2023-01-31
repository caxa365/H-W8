import requests
import os
from config import TOKEN

class YaUploader:
    
    host = 'https://cloud-api.yandex.net/'
    
    def __init__(self, token):
        self.token = token
        
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, disk_file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{disk_file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href'] 

    def upload_from_pc(self, path, disk_file_name):
        upload_link = self.get_upload_link(disk_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(path, 'rb'))
        print(response.status_code)

    def upload(self, path):
        self.upload_from_pc(path, disk_file_name)
                
if __name__ == '__main__':
    path = 'D:\Image.jpg'
    disk_file_name = os.path.basename(path).split('.')[0]
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path)