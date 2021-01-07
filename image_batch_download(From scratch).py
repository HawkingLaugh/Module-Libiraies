import requests

i = 1

def download(url):
    global i
    global temp_number
    print('Processing {0} url:{1}'.format(i,url))
    img = open('{}.jpg'.format(i),'wb')
    respone = requests.get(url, stream=True).content
    img.write(respone)
    i += 1
    img.close()