import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_translator():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-zh-en",
    )


st.title("Chinese to English Translator")
st.write("Enter Chinese text below to translate it into English.")

with st.form("translation_form"):
    text = st.text_area("Chinese text", value="你好，我的狗很可爱")
    submitted = st.form_submit_button("Translate")

if submitted:
    if not text.strip():
        st.warning("Enter some Chinese text to translate.")
    else:
        with st.spinner("Translating..."):
            translator = load_translator()
            result = translator(text, max_length=50)
        st.subheader("English translation")
        st.write(result[0]["translation_text"])
