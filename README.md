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
