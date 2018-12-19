#https://medium.com/@naveenkumarspa/using-python-for-your-desktop-wallpaper-collection-focused-on-beginners-a66451d25660

import requests
url = 'https://www.reddit.com/r/earthporn.json'
response = requests.get(url, headers={'User-agent': 'your-bot-name 0.1'})
if not response.ok:
    print("Error", response.status_code)
    exit()
data = response.json()['data']['children']
file = open('data.txt', mode='r')
links = map(str.strip, file.readlines())
file.close()
file = open('data.txt', mode='ab')
    
for i in range(len(data)):
    item = data[i]
    image_url = item['data']['url']
    if '.jpg' in image_url or '.jpeg' in image_url or '.png' in image_url:
        if image_url in links:
            print("Link already exists: ", image_url)
        else:
            file.write(image_url)

file.close()
