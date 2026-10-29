import qrcode
url = input("Enter the URL: ").strip()
filename = input("Enter the filename: ").strip()
if not filename.lower().endswith(".png"):
    filename += ".png"
pic = qrcode.make(url)
pic.save(filename)
print("QR code saved as ", filename)