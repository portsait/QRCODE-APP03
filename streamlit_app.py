import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# QR코드 생성 함수
def generate_qr_code(data: str, scale_factor: float = 0.5):
    # 1. QR코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # 2. QR코드 이미지를 생성
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # 3. 이미지 크기 축소
    original_size = qr_image.size
    new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
    qr_image = qr_image.resize(new_size, Image.ANTIALIAS)

    return qr_image

# Streamlit 애플리케이션
def main():
    st.title("QR코드 생성기")
    st.write("텍스트를 입력하고 QR코드를 생성합니다. 이미지는 자동으로 2배로 축소됩니다.")
    
    # 사용자 입력
    data = st.text_input("QR코드에 포함할 텍스트 또는 URL:", "https://example.com")
    
    # QR코드 생성 버튼
    if st.button("QR코드 생성"):
        if data.strip():
            # QR코드 생성
            qr_image = generate_qr_code(data)
            
            # 이미지 출력
            st.image(qr_image, caption="2배 축소된 QR코드", use_column_width=False)
            
            # 다운로드 버튼
            buffer = BytesIO()
            qr_image.save(buffer, format="PNG")
            buffer.seek(0)
            st.download_button(
                label="QR코드 다운로드",
                data=buffer,
                file_name="qrcode_scaled.png",
                mime="image/png",
            )
        else:
            st.warning("텍스트를 입력하세요.")

if __name__ == "__main__":
    main()
