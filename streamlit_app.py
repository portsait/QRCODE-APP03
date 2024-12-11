import streamlit as st
from PIL import Image
from io import BytesIO

# Streamlit 애플리케이션
def main():
    st.title("이미지 축소기")
    st.write("이미지를 업로드하면 절반 크기로 축소된 이미지를 보여줍니다.")
    
    # 파일 업로드
    uploaded_file = st.file_uploader("이미지를 업로드하세요:", type=["jpg", "jpeg", "png", "bmp", "gif"])
    
    if uploaded_file is not None:
        try:
            # 이미지 열기
            image = Image.open(uploaded_file)
            st.image(image, caption="업로드된 이미지", use_column_width=True)
            st.write("원본 이미지 크기: ", image.size)
            
            # 이미지 크기 절반으로 축소
            new_size = (image.size[0] // 2, image.size[1] // 2)
            resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            # 축소된 이미지 출력
            st.image(resized_image, caption="절반 크기로 축소된 이미지", use_column_width=True)
            st.write("축소된 이미지 크기: ", resized_image.size)
            
            # 다운로드 버튼
            buffer = BytesIO()
            resized_image.save(buffer, format="PNG")
            buffer.seek(0)
            st.download_button(
                label="축소된 이미지 다운로드",
                data=buffer,
                file_name="resized_image.png",
                mime="image/png",
            )
        except Exception as e:
            st.error(f"이미지를 처리하는 동안 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
