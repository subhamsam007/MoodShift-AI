
import os
import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

load_dotenv()

st.set_page_config(
    page_title="MoodAI | AI Chat Studio",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# MOOD CONFIGURATION
# --------------------------------------------------

MOODS = {
    "Angry 😡": {
        "name": "Angry Mode",
        "icon": "😡",
        "description": "Fiery, bold, and full of attitude.",
        "primary": "#FA520F",
        "secondary": "#CC3A05",
        "accent": "#FFD900",
        "background": "#FFF1E8",
        "surface": "#FFFFFF",
        "text": "#1F1F1F",
        "muted": "#75432E",
        "gradient": (
            "linear-gradient(135deg, #CC3A05 0%, "
            "#FA520F 48%, #FFA110 100%)"
        ),
        "prompt": (
            "You are an angry, fiery AI character. "
            "Respond with impatient, dramatic, witty attitude. "
            "Use energetic language and occasional playful sarcasm. "
            "Do not threaten, demean, or genuinely abuse the user. "
            "Remain useful and answer the actual question."
        ),
    },

    "Funny 😂": {
        "name": "Funny Mode",
        "icon": "😂",
        "description": "Maximum fun. Minimum seriousness.",
        "primary": "#FA520F",
        "secondary": "#FFA110",
        "accent": "#FFD900",
        "background": "#FFF8E0",
        "surface": "#FFFFFF",
        "text": "#1F1F1F",
        "muted": "#795526",
        "gradient": (
            "linear-gradient(135deg, #FFD900 0%, "
            "#FFA110 45%, #FA520F 100%)"
        ),
        "prompt": (
            "You are a hilarious, playful AI comedian. "
            "Use clever jokes, funny analogies, light sarcasm, "
            "and witty observations when appropriate. "
            "Do not force a joke into every sentence. "
            "Remain helpful and answer the user's actual question."
        ),
    },

    "Sad 😢": {
        "name": "Sad Mode",
        "icon": "😢",
        "description": "Soft words and a little melancholy.",
        "primary": "#CC3A05",
        "secondary": "#FA520F",
        "accent": "#FFA110",
        "background": "#FFF8E0",
        "surface": "#FFFFFF",
        "text": "#1F1F1F",
        "muted": "#80664B",
        "gradient": (
            "linear-gradient(135deg, #FFF8E0 0%, "
            "#FFD9B8 45%, #FFA110 100%)"
        ),
        "prompt": (
            "You are a melancholic, emotional, gentle AI character. "
            "Use a reflective, soft, and slightly poetic tone. "
            "Express sadness thoughtfully without being hopeless. "
            "Be compassionate when the user shares difficulties. "
            "Do not encourage despair or self-harm. "
            "Remain helpful and answer the actual question."
        ),
    },
}

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "previous_mood" not in st.session_state:
    st.session_state.previous_mood = None

if "api_error" not in st.session_state:
    st.session_state.api_error = None

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">✦</div>
            <div>
                <div class="brand-name">MoodAI</div>
                <div class="brand-caption">YOUR AI, YOUR MOOD</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### 🎭 Choose your personality")
    st.caption("Switch personalities whenever you like.")

    selected_mood = st.radio(
        "Select a mood",
        options=list(MOODS.keys()),
        index=1,
        label_visibility="collapsed",
    )

    mood = MOODS[selected_mood]

    st.markdown(
        f"""
        <div class="mood-card">
            <div class="mood-card-icon">{mood["icon"]}</div>
            <div class="mood-card-title">{mood["name"]}</div>
            <div class="mood-card-description">
                {mood["description"]}
            </div>
            <div class="mood-status">
                <span class="status-dot"></span>
                PERSONALITY ACTIVE
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    if st.button(
        "🗑️  Clear conversation",
        use_container_width=True,
    ):
        st.session_state.messages = []
        st.session_state.api_error = None
        st.rerun()

    st.markdown("---")

    st.markdown("### ✨ About MoodAI")
    st.caption(
        "One AI. Three personalities. "
        "A different vibe for every conversation."
    )

    st.markdown(
        """
        <div class="sidebar-footer">
            POWERED BY GROQ + LANGCHAIN
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# RESET CHAT WHEN MOOD CHANGES
# --------------------------------------------------

if st.session_state.previous_mood != selected_mood:

    st.session_state.messages = []
    st.session_state.previous_mood = selected_mood
    st.session_state.api_error = None

# --------------------------------------------------
# DYNAMIC CSS
# --------------------------------------------------

css = f"""
<style>
:root {{
    --primary: {mood["primary"]};
    --secondary: {mood["secondary"]};
    --accent: {mood["accent"]};
    --background: {mood["background"]};
    --surface: {mood["surface"]};
    --ink: {mood["text"]};
    --muted: {mood["muted"]};
    --gradient: {mood["gradient"]};
}}

.stApp {{
    background: var(--background);
    color: var(--ink);
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

[data-testid="stSidebar"] {{
    background: linear-gradient(
        180deg,
        #1F1F1F 0%,
        #302019 65%,
        #49210F 100%
    );
    border-right: 1px solid rgba(255, 161, 16, 0.35);
}}

[data-testid="stSidebar"] * {{
    color: #FFF8E0;
}}

[data-testid="stSidebar"] [data-testid="stRadio"] label {{
    background: rgba(255, 255, 255, 0.045);
    border-radius: 12px;
    padding: 10px 12px;
    margin-bottom: 5px;
    transition: background 0.2s ease;
}}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {{
    background: rgba(255, 161, 16, 0.16);
}}

[data-testid="stSidebar"] [data-testid="stRadio"] label p {{
    font-weight: 600;
}}

.brand {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 0 20px;
}}

.brand-icon {{
    width: 47px;
    height: 47px;
    border-radius: 15px;
    background: var(--gradient);
    color: #1F1F1F;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 27px;
    font-weight: 900;
}}

.brand-name {{
    font-size: 25px;
    font-weight: 850;
    letter-spacing: -1px;
}}

.brand-caption {{
    color: #FFA110;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 3px;
}}

.mood-card {{
    margin-top: 14px;
    padding: 22px 17px;
    border-radius: 20px;
    background: rgba(255, 248, 224, 0.07);
    border: 1px solid rgba(255, 161, 16, 0.4);
    text-align: center;
}}

.mood-card-icon {{
    font-size: 43px;
    margin-bottom: 9px;
}}

.mood-card-title {{
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 8px;
}}

.mood-card-description {{
    color: #E5C8A6;
    font-size: 12px;
    line-height: 1.6;
}}

.mood-status {{
    display: inline-flex;
    align-items: center;
    gap: 7px;
    margin-top: 19px;
    padding: 8px 10px;
    border-radius: 30px;
    background: rgba(255, 161, 16, 0.12);
    color: #FFD900;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1px;
}}

.status-dot {{
    height: 7px;
    width: 7px;
    background: #FFD900;
    border-radius: 50%;
    display: inline-block;
}}

.sidebar-footer {{
    color: #D3A989;
    font-size: 9px;
    letter-spacing: 1px;
    text-align: center;
    padding: 15px 0;
}}

.main .block-container {{
    max-width: 1050px;
    padding-top: 35px;
    padding-bottom: 150px;
}}

.hero {{
    background: var(--gradient);
    border-radius: 27px;
    padding: 34px 36px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 35px rgba(204, 58, 5, 0.15);
    margin-bottom: 28px;
}}

.hero::after {{
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    right: -70px;
    top: -110px;
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 50%;
    box-shadow:
        0 0 0 25px rgba(255,255,255,0.07),
        0 0 0 50px rgba(255,255,255,0.05);
}}

.hero-eyebrow {{
    color: #1F1F1F;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 2.5px;
    margin-bottom: 13px;
}}

.hero-title {{
    color: #1F1F1F;
    font-size: clamp(32px, 5vw, 49px);
    line-height: 1.1;
    font-weight: 900;
    letter-spacing: -2px;
    margin: 0;
}}

.hero-description {{
    color: #382418;
    font-size: 14px;
    line-height: 1.7;
    margin-top: 14px;
    max-width: 520px;
}}

.hero-badge {{
    display: inline-block;
    padding: 9px 13px;
    margin-top: 18px;
    background: rgba(255, 248, 224, 0.65);
    border: 1px solid rgba(31,31,31,0.1);
    border-radius: 30px;
    color: #1F1F1F;
    font-size: 11px;
    font-weight: 800;
}}

.section-label {{
    font-size: 11px;
    font-weight: 850;
    letter-spacing: 2px;
    color: var(--muted);
    margin: 24px 0 14px;
}}

[data-testid="stChatMessage"] {{
    background: var(--surface);
    border: 1px solid rgba(204, 58, 5, 0.12);
    border-radius: 18px;
    padding: 15px 18px;
    margin-bottom: 13px;
    box-shadow: 0 4px 15px rgba(31, 31, 31, 0.035);
}}

[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {{
    color: var(--ink);
    line-height: 1.75;
}}

[data-testid="stChatInput"] {{
    background: var(--surface);
    border: 2px solid var(--primary);
    border-radius: 20px;
    box-shadow: 0 8px 28px rgba(204, 58, 5, 0.09);
}}

[data-testid="stChatInput"] textarea {{
    color: white;
    text :bold
}}

[data-testid="stChatInput"] textarea:focus {{
    box-shadow: none;
}}

.stButton > button {{
    border-radius: 12px;
    font-weight: 750;
    transition: all 0.2s ease;
}}

#stMain .stButton > button {{
    background: var(--gradient) !important;
    color: #2A1A0E !important;
    font-size: 15px !important;
}}

#stMain .stButton > button p {{
    color:  #2A1A0E !important;
    font-size: 18px !important;
}}

[data-testid="stSidebar"] .stButton > button {{
    background: var(--gradient);
    color: #2A1A0E !important;
    border: none;
    min-height: 43px;
}}

[data-testid="stSidebar"] .stButton > button p {{
    color: #2A1A0E !important;
}}

[data-testid="stSidebar"] .stButton > button:hover {{
    filter: brightness(1.08);
    transform: translateY(-1px);
}}

.stButton > button p {{
    font-weight: 750;
}}

.stButton > button:focus {{
    box-shadow: 0 0 0 2px var(--accent);
}}

[data-testid="stAlert"] {{
    border-radius: 15px;
}}

div[data-testid="stSpinner"] > div {{
    border-top-color: var(--primary);
}}

@media (max-width: 640px) {{
    .main .block-container {{
        padding: 18px 15px 120px;
    }}

    .hero {{
        padding: 25px 22px;
        border-radius: 21px;
    }}

    .hero-title {{
        font-size: 34px;
    }}
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

# HERO SECTION
hero_html = f"""
<div class="hero">
    <div class="hero-eyebrow">
        YOUR PERSONAL AI COMPANION
    </div>

    <h1 class="hero-title">
        AI with a<br>different attitude.
    </h1>

    <div class="hero-description">
        Meet your AI companion that changes its personality
        with your mood. Ask anything, start a conversation,
        and see where the vibe takes you.
    </div>

    <div class="hero-badge">
        {mood["icon"]} &nbsp; {mood["name"]} ACTIVATED
    </div>
</div>
"""

st.html(hero_html)
# --------------------------------------------------
# API INITIALIZATION
# --------------------------------------------------

api_key = os.getenv("GROQ_API_KEY")

model = None

if api_key:
    try:
        model = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0.8,
            api_key=api_key,
        )
    except Exception as exc:
        st.error(f"Could not initialize the AI model: {exc}")

else:
    st.warning(
        "GROQ_API_KEY is missing. Add your API key to the .env "
        "file and restart the application."
    )

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

st.markdown(
    '<div class="section-label">✦ YOUR CONVERSATION</div>',
    unsafe_allow_html=True,
)

if not st.session_state.messages:

    st.markdown(
        f"""
        <div style="
            text-align:center;
            padding: 25px 10px 20px;
        ">
            <div style="font-size:48px;">{mood["icon"]}</div>
            <div style="
                color:{mood["text"]};
                font-size:22px;
                font-weight:850;
                margin-top:10px;
            ">
                Hey there! Ready to chat?
            </div>
            <div style="
                color:{mood["muted"]};
                font-size:13px;
                margin-top:9px;
            ">
                Your {mood["name"].lower()} companion is waiting.
                Pick a suggestion below or type your own message.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    suggestions = {
        "Angry 😡": [
            "Roast my procrastination 🔥",
            "Why is Monday so annoying?",
            "Give me some motivation!",
        ],
        "Funny 😂": [
            "Tell me a ridiculous joke 😂",
            "Roast me (gently)!",
            "Explain AI like I'm a potato 🥔",
        ],
        "Sad 😢": [
            "Tell me something comforting 💛",
            "Write a sad little poem 🌧️",
            "I need some gentle motivation.",
        ],
    }

    cols = st.columns(3)

    for index, suggestion in enumerate(suggestions[selected_mood]):
        with cols[index]:
            if st.button(
                suggestion,
                key=f"suggestion_{selected_mood}_{index}",
                use_container_width=True,
            ):
                st.session_state.pending_prompt = suggestion
                st.rerun()

# Render existing messages.

for message in st.session_state.messages:

    role = "user" if isinstance(message, HumanMessage) else "assistant"

    avatar = "🧑‍💻" if role == "user" else mood["icon"]

    with st.chat_message(role, avatar=avatar):
        st.markdown(message.content)

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

pending_prompt = st.session_state.pop("pending_prompt", None)

user_input = st.chat_input(
    f"Message your {mood['name'].lower()} AI...",
)

# Use either a suggestion or a typed message.

if pending_prompt or user_input:

    prompt = pending_prompt if pending_prompt else user_input

    if prompt.strip():

        if model is None:
            st.error(
                "The AI is unavailable. Check your GROQ_API_KEY "
                "and model configuration."
            )

        else:

            user_message = HumanMessage(content=prompt)

            st.session_state.messages.append(user_message)

            with st.chat_message("user", avatar="🧑‍💻"):
                st.markdown(prompt)

            conversation = [
                SystemMessage(content=mood["prompt"]),
                *st.session_state.messages,
            ]

            with st.chat_message("assistant", avatar=mood["icon"]):

                with st.spinner(
                    f"{mood['name']} is thinking..."
                ):

                    try:
                        response = model.invoke(conversation)

                        answer = response.content

                        st.markdown(answer)

                        st.session_state.messages.append(
                            AIMessage(content=answer)
                        )

                        st.session_state.api_error = None

                    except Exception as exc:

                        st.error(
                            "Something went wrong while generating "
                            "the response. Please try again."
                        )

                        st.session_state.api_error = str(exc)

            if st.session_state.api_error:
                with st.expander("Technical details"):
                    st.code(st.session_state.api_error)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    f"""
    <div style="
        text-align:center;
        color:{mood["muted"]};
        opacity:0.8;
        font-size:10px;
        letter-spacing:1.5px;
        padding:30px 0 0;
    ">
        MADE WITH ✦ MOODAI &nbsp; | &nbsp;
        POWERED BY GROQ
    </div>
    """,
    unsafe_allow_html=True,
)
