import warnings
import logging

warnings.filterwarnings("ignore")
logging.getLogger("google_genai").setLevel(logging.ERROR)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
import streamlit as st

load_dotenv()

# ---------------- Page Config ----------------
st.set_page_config(page_title="Review Analyzer AI", page_icon="🤖", layout="wide")

# ---------------- Robotic Dark Theme CSS ----------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700;900&display=swap');

    .stApp {
        background-color: #05070a;
        background-image:
            radial-gradient(circle at 20% 20%, rgba(0,255,170,0.06) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(124,58,237,0.08) 0%, transparent 40%),
            linear-gradient(rgba(0,255,170,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,170,0.04) 1px, transparent 1px);
        background-size: auto, auto, 28px 28px, 28px 28px;
        color: #d6ffe9;
        font-family: 'Share Tech Mono', monospace;
    }

    h1 {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        color: #00ffb3;
        text-shadow: 0 0 18px rgba(0,255,179,0.7);
        letter-spacing: 3px;
        font-size: 42px !important;
    }

    .subtitle {
        text-align: center;
        color: #5fd9b4;
        font-family: 'Share Tech Mono', monospace;
        margin-bottom: 35px;
        font-size: 15px;
        letter-spacing: 1px;
    }

    .stTextArea textarea {
        background-color: #0b0f14 !important;
        color: #00ffb3 !important;
        border: 1px solid #00ffb3 !important;
        border-radius: 8px !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 15px !important;
    }

    .stButton button {
        background-color: #001f16;
        color: #00ffb3;
        border: 1px solid #00ffb3;
        border-radius: 8px;
        font-weight: 700;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
        padding: 14px 0;
        box-shadow: 0 0 12px rgba(0,255,179,0.25);
        width: 100%;
    }
    .stButton button:hover {
        background-color: #00ffb3;
        color: #05070a;
        box-shadow: 0 0 25px rgba(0,255,179,0.8);
    }

    .panel {
        background-color: #0b0f14;
        border: 1px solid #1d2b26;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(0,255,179,0.06);
        height: 100%;
    }

    .panel-glow-green {
        border: 1px solid #00ffb3;
        box-shadow: 0 0 20px rgba(0,255,179,0.2);
    }
    .panel-glow-red {
        border: 1px solid #ff3b5c;
        box-shadow: 0 0 20px rgba(255,59,92,0.2);
    }
    .panel-glow-purple {
        border: 1px solid #a855f7;
        box-shadow: 0 0 20px rgba(168,85,247,0.2);
    }

    .panel-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 15px;
        color: #00ffb3;
        letter-spacing: 2px;
        margin-bottom: 14px;
        border-bottom: 1px solid #1d2b26;
        padding-bottom: 10px;
    }

    .panel-body {
        font-family: 'Share Tech Mono', monospace;
        font-size: 14.5px;
        line-height: 1.8;
        color: #d6ffe9;
    }

    .sentiment-badge {
        display: inline-block;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 20px;
        letter-spacing: 2px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .sentiment-positive {
        color: #00ffb3;
        background-color: rgba(0,255,179,0.08);
        border: 1px solid #00ffb3;
        text-shadow: 0 0 10px rgba(0,255,179,0.6);
    }
    .sentiment-negative {
        color: #ff3b5c;
        background-color: rgba(255,59,92,0.08);
        border: 1px solid #ff3b5c;
        text-shadow: 0 0 10px rgba(255,59,92,0.6);
    }
    .sentiment-neutral {
        color: #ffd166;
        background-color: rgba(255,209,102,0.08);
        border: 1px solid #ffd166;
        text-shadow: 0 0 10px rgba(255,209,102,0.6);
    }

    .status-line {
        font-family: 'Share Tech Mono', monospace;
        color: #5fd9b4;
        font-size: 13px;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤖 REVIEW ANALYZER AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>&gt; NEURAL SENTIMENT ENGINE // STRUCTURED EXTRACTION MODULE ONLINE_</p>", unsafe_allow_html=True)

# ---------------- Model ----------------
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.7
)


# ---------------- Schema ----------------
class Review(TypedDict):
    key_themes: Annotated[list[str], "write down all the key theme discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]


structured_model = model.with_structured_output(Review)

# ---------------- Input ----------------
col_input, col_btn = st.columns([4, 1])

with col_input:
    review_text = st.text_area("INPUT REVIEW DATA >", height=160, placeholder="Paste review text here for analysis...")

with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_clicked = st.button("ANALYZE", use_container_width=True)

# ---------------- Analyze ----------------
if analyze_clicked:
    if review_text.strip() == "":
        st.warning("> ERROR: NO INPUT DATA DETECTED")
    else:
        with st.spinner("SCANNING REVIEW // RUNNING INFERENCE..."):
            result = structured_model.invoke(review_text)

        st.markdown("<p class='status-line'>&gt; ANALYSIS COMPLETE // RESULTS BELOW</p>", unsafe_allow_html=True)
        st.markdown("---")

        # ---------------- Top row: Sentiment + Summary ----------------
        top1, top2 = st.columns([1, 2])

        with top1:
            sentiment = result["sentiment"].lower()
            glow_class = {
                "positive": "panel-glow-green",
                "negative": "panel-glow-red",
                "neutral": "panel-glow-purple"
            }.get(sentiment, "")
            st.markdown(f"""
                <div class='panel {glow_class}' style='text-align:center;'>
                    <div class='panel-title'>SENTIMENT</div>
                    <span class='sentiment-badge sentiment-{sentiment}'>{result['sentiment'].upper()}</span>
                </div>
            """, unsafe_allow_html=True)

        with top2:
            st.markdown(f"""
                <div class='panel panel-glow-green'>
                    <div class='panel-title'>📌 SUMMARY</div>
                    <div class='panel-body'>{result['summary']}</div>
                </div>
            """, unsafe_allow_html=True)

        # ---------------- Key Themes ----------------
        themes_html = "".join([f"<div>▸ {theme}</div>" for theme in result['key_themes']])
        st.markdown(f"""
            <div class='panel panel-glow-purple'>
                <div class='panel-title'>🔑 KEY THEMES</div>
                <div class='panel-body'>{themes_html}</div>
            </div>
        """, unsafe_allow_html=True)

        # ---------------- Pros & Cons ----------------
        bottom1, bottom2 = st.columns(2)

        with bottom1:
            pros_html = "".join([f"<div>✔ {p}</div>" for p in result['pros']]) if result['pros'] else "<div>NO PROS DETECTED</div>"
            st.markdown(f"""
                <div class='panel panel-glow-green'>
                    <div class='panel-title'>✅ PROS</div>
                    <div class='panel-body'>{pros_html}</div>
                </div>
            """, unsafe_allow_html=True)

        with bottom2:
            cons_html = "".join([f"<div>✘ {c}</div>" for c in result['cons']]) if result['cons'] else "<div>NO CONS DETECTED</div>"
            st.markdown(f"""
                <div class='panel panel-glow-red'>
                    <div class='panel-title'>❌ CONS</div>
                    <div class='panel-body'>{cons_html}</div>
                </div>
            """, unsafe_allow_html=True)