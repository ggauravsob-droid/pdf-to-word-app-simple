import streamlit as st
from pdf2docx import Converter
import tempfile
import os

st.set_page_config(page_title="PDF to Word (Exact Layout)", page_icon="📄")
st.title("📄 PDF to Word (Format & Tables Preserved)")
st.write("Apni PDF upload karein. Yeh app PDF ki tables, formatting aur layout ko Word file mein exact copy karega.")

uploaded_file = st.file_uploader("Apni PDF file yahan drag & drop karein", type=["pdf"])

if uploaded_file is not None:
    if st.button("Start Conversion 🚀"):
        with st.spinner("PDF ko Word mein badla ja raha hai... Format save ho raha hai..."):
            try:
                # PDF ko temporarily save karna
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf.write(uploaded_file.read())
                    pdf_path = temp_pdf.name
                
                # Word file ka path
                word_path = pdf_path.replace('.pdf', '.docx')
                
                # Conversion process (Jo tables aur design bacha ke rakhega)
                cv = Converter(pdf_path)
                cv.convert(word_path) # Pura PDF convert karega
                cv.close()
                
                st.success("✅ Conversion poora ho gaya! Tables aur format copy ho gaye hain.")
                
                # Download Button
                with open(word_path, "rb") as file:
                    st.download_button(
                        label="📥 Download Word File",
                        data=file,
                        file_name=uploaded_file.name.replace('.pdf', '_Formatted.docx'),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                
                # Safai (Temp files delete karna)
                os.remove(pdf_path)
                os.remove(word_path)
                    
            except Exception as e:
                st.error(f"Ek error aa gaya: {e}")
