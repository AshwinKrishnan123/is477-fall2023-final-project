import hashlib
import requests

url ='https://archive.ics.uci.edu/static/public/53/iris.zip'
response = requests.get(url)

with open ('iris.zip', mode='wb') as f:
    f.write(response.content)

filename= 'iris.zip'
with open (filename, mode='rb') as f:
    data=f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    uci_iris = '4ba9ff91a7586a37383329548823a4584298716a51f786c55a273c1c201571c2'
if (uci_iris !=sha256hash):
    print('Computed hash does not match expected hash')
else:
    print('Computed hash matches expected hash')