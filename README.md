# Chatbot

This is a AI chatbot built using [Streamlit](https://streamlit.io/) and powered by the Together API (Meta LLaMA 3 model).

## 🛠️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/streamlit-chatbot.git
   cd streamlit-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Together API key in a `.env` file:
   ```env
   TOGETHER_API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   streamlit run chatbot.py
   ```

## 🧠 Technologies Used

- Python 🐍
- Streamlit 📺
- Together API (LLaMA 3) 🧠


## ✨ Customization

- Modify welcome messages in chatbot.py using the `welcome_variants` list
- Update styling in the `<style>` section for colors, fonts, and layout
- You can change the LLM model in the Together API call


## 📦 Requirements

Create a file called `requirements.txt` and include:
```txt
streamlit
python-dotenv
together
```



