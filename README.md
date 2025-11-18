# 🤖chatbot-langchain+python
A minimal example chat client that uses Google's Gemini models via the `langchain-google-genai` integration. The app wraps a LangChain chat model and a simple message history to send user messages to the Gemini model and print responses.

**Project structure**
- `app.py` - main application script
- `.env` - environment file (not committed) containing `GEMINI_API_KEY`
- `venv/` - Python virtual environment (created locally)

**Prerequisites**
- Python 3.11 or 3.12 recommended. Python 3.14 may show compatibility warnings from dependencies (see Troubleshooting).
- A Google Gemini API key with access to the model you intend to use.

**Environment variables**
Create a `.env` file in the project root with the following content:

```
GEMINI_API_KEY=your_api_key_here
```

**Install & Setup (PowerShell)**

1. Create a virtual environment (if you haven't already):

```powershell
cd "C:\Users\Admin\OneDrive\Desktop\ChatbotGemini"
python -m venv venv
```

2. Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install python-dotenv google-generativeai langchain-google-genai langchain-community
```

(Optional) To freeze the environment to a `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

**Run**

With the virtual environment activated and `.env` configured:

```powershell
python app.py
```

Type messages at the prompt. Type `exit` to quit.

**Default settings and where to change them**
- The default model is set in `app.py` in the `build_chatbot` function. By default it uses `gemini-2.0-flash`. To change models edit the `modelName` default or pass a different value when calling `build_chatbot`.

Example (in `app.py`):
```python
chat_model, message_history = build_chatbot(modelName='gemini-2.0-flash', temperature=0.7)
```

**Troubleshooting**
- "UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater":
  - This is a warning emitted by `langchain_core`/`pydantic` when running on Python 3.14+. The app may still run, but you can avoid the warning by using Python 3.11 or 3.12 if you prefer.

- "models/<model> is not found" (404 NotFound):
  - The chosen model may not be available on the API version used by the client. Change the `modelName` in `build_chatbot` to a supported model (for example `gemini-2.0-flash`), or call the cloud API's ListModels method to see available models and their supported methods.

- `ChatGoogleGenerativeAI` parameter errors:
  - If you see warnings about `model_name`, use `model=` keyword instead of `model_name=` (the code already uses `model=`).
