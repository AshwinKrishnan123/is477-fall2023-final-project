import hashlib
import requests

url ='https://archive.ics.uci.edu/static/public/862/turkish+music+emotion.zip'
response = requests.get(url)

with open ('turkish+music+emotion.zip', mode='wb') as f:
    f.write(response.content)

filename= 'turkish+music+emotion.zip'
with open (filename, mode='rb') as f:
    data=f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    uci_iris = 'cde69ba13c7968200e5dc904c863b0a41c3e309977a8c60966d4ac57cd9247cc'
if (uci_iris !=sha256hash):
    print('Computed hash does not match expected hash')
else:
    print('Computed hash matches expected hash')
