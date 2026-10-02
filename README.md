## 🔗 Live Demo

[Try the app here](https://ai-review-analyzer-am9leylaqrmrgnhxd4gswg.streamlit.app/)

# 📝 AI Review Analyzer

An AI-powered tool that analyzes product/service reviews and extracts **summary, sentiment, key themes, pros, and cons** — built using **LangChain**, **Google Gemini**, and **Streamlit**.

## 🚀 Features

- Paste any review text and get instant structured analysis
- Automatic summary generation
- Sentiment detection (Positive / Negative / Neutral) with color-coded display
- Key themes extraction
- Pros and cons breakdown, side by side
- Clean, light-themed UI

## 🛠️ Tech Stack

- **Python**
- **LangChain** (Structured Output with TypedDict schema)
- **Google Gemini API** (via `langchain-google-genai`)
- **Streamlit** (UI)

## 📸 How it works

1. Paste a review in the text box
2. Click **Analyze Review**
3. Gemini processes the review and returns structured output (not free text)
4. Results are displayed as: Summary, Sentiment, Key Themes, Pros, and Cons

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShubhamArya-shub/ai-review-analyzer.git
   cd ai-review-analyzer
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```


## 👤 Author

**Shubham Kumar**
[GitHub](https://github.com/ShubhamArya-shub) | [LinkedIn](https://linkedin.com/in/shubham-arya-1706b7391)
