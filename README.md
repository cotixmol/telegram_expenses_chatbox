# 🤖 Telegram Expenses Chatbot

**Welcome to the Telegram Expenses Chatbot!** This bot interacts with the Node.js connector to process user messages through a Language Learning Model (LLM) and return responses. 🌟

🔗 **Node.js Connector Repository**
You can find the Node.js connector here: [Node Telegram Connector](https://github.com/cotixmol/telegram_expenses_chatbox)

## 📜 Overview

This bot performs the following steps:

1. **Receive Message**: Takes a message in the format:
    ```json
    {
        "user_id": 7133185151,
        "first_name": "Constancio",
        "last_name": "Molinengo",
        "text": "Barbacue Chips $4"
    }
    ```

2. **Authorize User**: Verifies the user using `user_id` saved in a Supabase database.

3. **Process Message**: Uses the LLM to process the message.

4. **Save Output**: Stores the structured JSON output from the LLM to the Supabase database.

5. **Return Response to Node.js App**: Sends a response back to the Node.js app in the following format:
    ```json
    {
    "status": 200,
    "message": {
        "user_id": int,
        "content": str
    }
}
    ```

### 📦 Installation

1. **Install Poetry**: Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

2. **Add Packages**: Run the following command to install dependencies:
    ```sh
    poetry install
    ```

### 🚀 Running the Bot

1. **Set Environment Variables**: Configure your environment variables in a `.env` file.
    ```sh
    SUPABASE_URI=
    OPEN_AI_APIKEY=
    OPEN_AI_MODEL=
    ```

2. **Start the Bot**: Use the Makefile to run the bot:
    ```sh
    make start-app
    ```

### 🛠️ Testing

You can test the bot's functionality by sending a formatted message through the Node.js connector and verifying the response.