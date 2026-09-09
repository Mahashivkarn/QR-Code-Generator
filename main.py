'''
We are going to ues a Python library like qrcode and convert url to qr
'''
import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)