import requests
import os.path

def read_token(file):
    with open(file, 'r') as f:
        token = f.readline()
    return token

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        file = os.path.basename(file_path)
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        res = requests.get(f'{url}/upload?path={file}&overwrite={True}', headers=headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res['href'], files={'file':f})
            except:
                print(res)
                
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = read_token('token.txt')
    uploader = YaUploader(token)
    files_list = ['task_2.txt'] #списком имена передаваемых файлов файлы
    for name in files_list:
        result = uploader.upload(os.path.abspath(name))