# for web
import streamlit as st
# for QR code create
import qrcode
#for Image 
from PIL import Image
# for Download
import io

# Input URL
url = st.text_input("Enter URL:")

# Generate QR code
if url:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    # Display QR code
    st.image("qr_code.png")

    # Download QR code
    img = Image.open("qr_code.png")
    img_io = io.BytesIO()
    # img.save(img_io, "PNG")
    st.download_button("Download QR Code", img_io, "qr_code.png", "image/png")