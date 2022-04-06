import pyqrcode
s = "https://terraria.wiki.gg/wiki/Terraria_Wiki"
url = pyqrcode.create(s)
url.svg("myqr.jpg, scale = 8")

