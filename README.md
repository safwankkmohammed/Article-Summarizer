 🌟 Article Summarizer

A simple and user-friendly web application that summarizes long articles into concise summaries using **Streamlit**, **Newspaper3k**, and **Hugging Face Transformers**.

---

🚀 Features

- Summarizes long web articles or pasted text into short summaries.
- Supports input via URL or raw text.
- Handles long articles by automatically splitting them into manageable chunks.
- Fast and easy to use with a colorful, interactive interface.
- Built with Streamlit for easy deployment.

---

⚙️ Technologies Used

- Streamlit – For the interactive web interface.
- Newspaper3k – To extract article text from web URLs.
- Hugging Face Transformers – Using the `sshleifer/distilbart-cnn-12-6` model for fast summarization.

---

 📋 Requirements

- Python 3.7+
- Streamlit
- Transformers
- Newspaper3k

---

 ✅ How to Run Locally

1️⃣ Clone the repository or download the source code.

2️⃣ Install dependencies:
bash
pip install -r requirements.txt

3️⃣ Run the Streamlit app:
bash
streamlit run app.py

🌐 Sample Article URL to Test
You can try the app with this article link:
https://www.bbc.com/news/technology-66799605

🎨 Demo Preview
App Screenshot
![App Screenshot](https://github.com/safwankkmohammed/Article-Summarizer/blob/main/article_summarizer.png)

⚡ Notes
Summary speed depends on the article length and your machine’s CPU performance.
Cached summaries are stored using Streamlit’s cache mechanism for faster repeat use.

📢 Thank You!
Feel free to ⭐ the repository if you found it useful!
Open to contributions and suggestions.

🌈 Happy Summarizing! 🚀

📚 Project Structure
```bash
article-summarizer/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project description
└── .gitignore           # To ignore __pycache__, etc.

```bash

👉 **Optional Tip:**  
Add a `.gitignore` file to avoid uploading unwanted files:
```gitignore
__pycache__/
*.pyc
.env




