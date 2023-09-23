import qrcode
qr = qrcode.QRCode(version = 15, box_size = 5, border = 5)
data = ("https://github.com/MoonLight022")  # data can be anything like: URLs or other information that link directly to text, emails, websites, phone numbers
qr.add_data(data)
qr.make(fit = True)
qr_img = qr.make_image(fill = "black", back_color = "white")
qr_img.save("ImageName.png")
