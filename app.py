import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import string
import arabic_reshaper
from bidi.algorithm import get_display 
import base64

# Load model and data
model = joblib.load("best_model.pkl")
df = pd.read_csv("snappfood_sentiment_train.csv")

# Helper: Persian text cleaner
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    return text



st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Vazirmatn', sans-serif;
    }

    h1, h2, h3, h4, h5, h6, p, div, span {
        font-family: 'Vazirmatn', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)


st.image("snapfood_icon.png", width=100)
st.markdown("<h1 style='text-align: center;'>تحلیل احساسات کاربران اسنپ‌فود</h1>", unsafe_allow_html=True)

st.markdown("<div dir='rtl' style='text-align: center'>لطفاً متن نظر خود را وارد کنید تا احساس آن (مثبت یا منفی) تشخیص داده شود.</div>", unsafe_allow_html=True)

# Input text
user_input = st.text_area("متن نظر شما", height=150)

# Prediction
if st.button("تحلیل احساس"):
    if user_input.strip() == "":
        st.warning("لطفاً یک متن وارد کنید.")
    else:
        prediction = model.predict([user_input])[0]
        sentiment = "😊 مثبت" if prediction == 1 else "😠 منفی"
        st.success(f"نتیجه تحلیل احساس: {sentiment}")

# Optional: Show word cloud
if st.checkbox("نمایش ابر کلمات نظرات کاربران"):
    with st.spinner("در حال تولید ابر کلمات..."):
        # Clean and reshape text for RTL display
        df["cleaned_comment"] = df["comment"].astype(str).apply(clean)
        reshaped_words = [
            get_display(arabic_reshaper.reshape(word))
            for word in df["cleaned_comment"]
        ]
        all_text = " ".join(reshaped_words)

        font_path = "B-NAZANIN.TTF"

        wordcloud = WordCloud(
            font_path=font_path,
            width=800,
            height=400,
            background_color='white',
            max_font_size=120
        ).generate(all_text)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

