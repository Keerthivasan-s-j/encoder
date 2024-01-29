# Importing libraries
import streamlit as st
import qrcode
from io import BytesIO

# Function to generate QR code
def generate_qr_code(data):
    qr_img = qrcode.make(data)
    return qr_img

# Streamlit app
def main():
    st.title("QR Code Generator")

    # Get data input from the user
    data = st.text_input("Enter data to encode into QR code:")

    if st.button("Generate QR Code"):
        # Generate QR code
        qr_img = generate_qr_code(data)

        # Convert the QR code image to bytes
        img_byte_array = BytesIO()
        qr_img.save(img_byte_array, format='PNG')
        img_byte_array = img_byte_array.getvalue()
        print(img_byte_array)

        # Display the QR code directly using Streamlit
        st.image(img_byte_array, caption="QR Code", use_column_width=True)

if __name__ == "__main__":
    main()
