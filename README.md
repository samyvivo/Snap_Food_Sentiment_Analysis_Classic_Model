SnapFood Sentiment Analysis (in Persian) 🍔

 Over the past few days, I worked on a machine learning project to analyze user sentiment in Farsi (Persian) based on SnapFood app reviews.

🗂 Dataset:
 I used a public Persian dataset from PNLPhub on Hugging Face, containing thousands of labeled reviews (positive/negative).

🔧 Key Steps:
📌 1. Text Cleaning & Normalization:
 Using custom functions and libraries like hazm, I removed:
• HTML tags, links, brackets
• Stopwords and punctuation
• Normalized Persian text

📌 2. Tokenization & Vectorization:
 •I converted the cleaned reviews into numerical features using:
• TF-IDF Vectorizer with n-grams (uni & bi)
• Max features = 10,000
•Custom preprocessor included lemmatization

📌 3. Model Training:
• I compared multiple ML classifiers:
• PassiveAggressiveClassifier
• LogisticRegression
• RandomForest
The best model was PassiveAggressiveClassifier, which achieved accuracy > 85% on test data!

📌 4. Hyperparameter Tuning:
• Used GridSearchCV to tune:
• C, max_iter, and loss for PassiveAggressiveClassifier

📌 5. Evaluation:
 Generated classification report and confusion matrix. Model showed high precision and recall on both positive and negative reviews.

🌐 Deployment:
 I deployed the final model as an interactive web app that supporting:
• Farsi input with RTL support
• Word cloud generation from real reviews
• Persian font (B-NAZANIN.TTF)
• Interactive sentiment predictions

🖼 Sample output includes:
Farsi user review → sentiment = 😊 مثبت or 😠 منفی
Word cloud with reshaped & bidi-adjusted Farsi text


 تحلیل احساسات کاربران اسنپ‌فود (زبان فارسی) 🍔

چند روز گذشته رو روی پروژه‌ای کار کردم که با استفاده از یادگیری ماشین، احساسات کاربران اسنپ‌فود رو از روی نظراتشون (مثبت یا منفی) تحلیل می‌کنه — اونم به زبان فارسی! 

🔍 مراحل انجام پروژه:

📦 ۱. داده‌ها:
از دیتاست فارسی موجود در Hugging Face - PNLPhub استفاده کردم که شامل هزاران نظر کاربران به همراه برچسب‌های مثبت و منفی بود.

🧹 ۲. پاک‌سازی و پیش‌پردازش متن:
با استفاده از توابع سفارشی و کتابخانه‌هایی مثل hazm متن‌ها رو پاک‌سازی و نرمال کردم:

• حذف لینک، تگ HTML، علائم نگارشی

• تبدیل حروف به شکل استاندارد

• حذف کلمات توقف (Stop words) 
ُ
🔢 ۳. تبدیل متن به عدد:
از TF-IDF استفاده کردم (با uni-gram و bi-gram) برای بردار کردن متن‌ها با 52 هزار فیچر.

🤖 ۴. مدل‌سازی:
مدل‌های مختلف رو تست کردم:

• Passive Aggressive Classifier 

• Logistic Regression ✅ (بهترین عملکرد)

• Random Forest

مدل نهایی دقت بالای 85 ٪ داشت.

⚙️ ۵. تنظیم هایپرپارامترها:
با GridSearchCV مقادیری مثل C و max_iter رو برای بهترین عملکرد تنظیم کردم.

📊 ۶. ارزیابی مدل:
از confusion matrix و classification report برای بررسی Accuracy ، F1 و Roc/Auc استفاده شد — و نتایج خوب بود.

🌐 ۷. پیاده‌سازی به عنوان اپلیکیشن وب:

یه اپلیکیشن ساده و فارسی‌ساز ساختم که:

• از ورودی‌های فارسی پشتیبانی می‌کنه (راست‌به‌چپ)

• فونت فارسی (B Nazanin) داره

• پیش‌بینی احساس نظر رو نشون می‌ده

یک ابرکلمات فارسی از کل نظرات تولید می‌کنه ✨
