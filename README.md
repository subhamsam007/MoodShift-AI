# 🧠 MoodShift AI — Emotion-Aware Chatbot

An AI-powered chatbot built with **Python, Streamlit, LangChain, and Groq** to deliver interactive and engaging AI conversations.

MoodShift AI aims to make conversations more personalized and engaging through an intuitive chat interface powered by large language models.

## 🚀 Live Demo

🔗 **Try MoodShift AI:** [Click here to access the live app](https://moodshift-aichat.streamlit.app/)


---

## 📸 Project Preview

<!-- Add your project screenshot here -->

![MoodShift AI Project Screenshot](images/project-screenshot.png)

> **How to add your screenshot:**
> 1. Create a folder named `images` in your project directory.
> 2. Add your application screenshot to that folder.
> 3. Name the image `project-screenshot.png`.
> 4. Push the image to GitHub.

---

## ✨ Features

- 💬 **AI-Powered Chat:** Interact with an AI assistant through a conversational interface.
- 🧠 **Mood-Aware Conversations:** Designed to support mood-oriented interactions.
- ⚡ **Fast Responses:** Uses Groq-powered language models.
- 🔗 **LangChain Integration:** Uses LangChain to connect with language models and build AI workflows.
- 🎨 **Interactive Interface:** A user-friendly web interface built with Streamlit.
- 🔐 **Secure API Configuration:** Supports environment variables for local development and secrets for deployment.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface |
| Groq | Language model inference |
| LangChain | LLM integration and application workflow |
| python-dotenv | Local environment variable management |
| uv | Python package and environment management |
| Git & GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
MoodShift-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
├── images/
│   └── project-screenshot.png
└── README.md
```

> This is an example structure. Adjust filenames and folders to match your actual project. Never upload your `.env` file or API keys to GitHub.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/subhamsam007/MoodShift-AI.git
cd MoodShift-AI
```

### 2. Create a Virtual Environment

This project uses `uv` for Python environment and package management.

If you haven't installed `uv`, follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

Create a virtual environment:

```bash
uv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual API key.

**Security reminder:** Never commit your `.env` file or publish your API key. Ensure `.env` is included in your `.gitignore` file.

### 6. Run the Application

If your main Python file is named `app.py`, run:

```bash
uv run streamlit run app.py
```

Your application should open in your browser.

> If your main Python file has a different name, replace `app.py` with the correct filename.

---

## ☁️ Deployment

MoodShift AI can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

### Deployment Steps

1. Push your project code to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in using your GitHub account.
4. Create a new app.
5. Select the `subhamsam007/MoodShift-AI` repository.
6. Choose the correct branch and main Python file.
7. Open **Advanced settings → Secrets**.
8. Add your Groq API key:

```toml
GROQ_API_KEY = "your_actual_groq_api_key"
```

9. Click **Deploy**.
10. Once deployment succeeds, copy your public application URL and replace the live demo placeholder at the top of this README.

---

## 🔒 Security

- Never expose API keys, passwords, or access tokens.
- Keep `.env` out of version control.
- Use Streamlit Secrets to configure API keys in the deployed application.
- If an API key is accidentally published, revoke it and generate a new one.

---

## 🔮 Future Improvements

- Enhance mood-aware response generation.
- Improve conversation history and memory.
- Add more personalization options.
- Improve the user interface and overall experience.
- Introduce additional AI-powered features.

---

## 👨‍💻 Author

**Subham Sam**

- GitHub: [@subhamsam007](https://github.com/subhamsam007)
- Project Repository: [MoodShift AI](https://github.com/subhamsam007/MoodShift-AI)

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

**Made with ❤️ using Python, Streamlit, LangChain, and Groq.**
