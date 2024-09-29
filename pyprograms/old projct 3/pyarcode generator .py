import pyqrcode


link = input("inter the link that you want qr of ")

tl = pyqrcode.create(link)

tl.svg("tl.svg", scale=8)
tl.eps('uca-url.eps', scale=2)
print(tl)
