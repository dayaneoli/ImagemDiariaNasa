import requests
from PIL import Image
import shutil

imagemNasa = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
print(imagemNasa.status_code)

respostaNasa = imagemNasa.json()
print(respostaNasa)

my_url = 'https://apod.nasa.gov/apod/image/2301/CrabNebula_Hubble_960.jpg'
response = requests.get(my_url, stream=True)
with open('my_image.png', 'wb') as file:
    shutil.copyfileobj(response.raw, file)
del response

img = Image.open('my_image.png')
img.show()