


# import gradio as gr
# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL = "phi3"

# def chat(message, history):
#     try:
#         response = requests.post(
#             OLLAMA_URL,
#             json={"model": MODEL, "prompt": message, "stream": False},
#             timeout=180
#         )
#         data = response.json()
#         return data.get("response", "⚠ No reply from model")
#     except Exception as e:
#         return f"❌ Error: {str(e)}"


# with gr.Blocks() as app:

#     # Top title
#     gr.Markdown("<h2 style='text-align:center; margin-bottom:20px;'>🤖 AI Chatbot</h2>")

#     # Column for chat interface
#     with gr.Column(elem_classes="chat-container"):

#         # Chat interface
#         chatbot = gr.ChatInterface(fn=chat)

#         # Clear button
#         clear_btn = gr.Button("🗑 Clear Conversation", elem_classes="clear-btn")
#         clear_btn.click(lambda: None, None, chatbot.chatbot)

#         # Footer text immediately after the button
#         gr.Markdown("Developed by Sakshi Bute | Local AI Chatbot", elem_classes="footer-text")


# # Launch with theme and CSS
# app.launch(
#     theme=gr.themes.Soft(),
#     css="""
#     footer {visibility: hidden;}
    
#     /* Chat container styling */
#     .chat-container {
#         width: 700px;          
#         height: 650px;         
#         margin: 0 auto;        /* horizontal center */
#         margin-top: 5px;     /* 1 inch space below title */
#         border-radius: 20px;   
#         box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
#         padding: 10px;
#     }

#     /* Clear button styling */
#     .clear-btn {
#         display: block;
#         margin: 10px auto;
#         background-color: red;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 8px 20px;
#         font-weight: bold;
#         cursor: pointer;
#     }
#     .clear-btn:hover {
#         background-color: darkred;
#     }

#     /* Footer text */
#     .footer-text {
#         text-align: center;
#         font-weight: 400;
#         font-size: 16px;
#         margin-top: 5px;
#     }
#     """
# )
















import gradio as gr
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

def chat(message, history):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": message,
                "stream": False
            },
            timeout=180
        )

        data = response.json()
        return data.get("response", "⚠ No reply from model")

    except Exception as e:
        return f"❌ Error: {str(e)}"


with gr.Blocks() as app:

    # 🔹 Centered Title
    gr.Markdown(
        "<h2 style='text-align:center; margin-bottom:20px;'>🤖 AI Chatbot</h2>"
    )

    # 🔹 Chat Container
    with gr.Column(elem_classes="chat-container"):

        chatbot = gr.ChatInterface(fn=chat)

        # 🔹 Clear Button
        clear_btn = gr.Button(
            "🗑 Clear Conversation",
            elem_classes="clear-btn"
        )

        clear_btn.click(lambda: None, None, chatbot.chatbot)

        # 🔹 Footer
        gr.Markdown(
            "Developed by Sakshi Bute | Local AI Chatbot",
            elem_classes="footer-text"
        )


# 🔹 Launch App
app.launch(
    theme=gr.themes.Soft(),
    css="""
    footer {visibility: hidden;}

    /* Hide ONLY the time taken text (keep spinner & processing) */
    .status-bar span:last-child {
        display: none !important;
    }

    /* Chat container styling */
    .chat-container {
        width: 700px;
        height: 650px;
        margin: 0 auto;
        margin-top: 15px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        padding: 10px;
    }

    /* Clear button styling */
    .clear-btn {
        display: block;
        margin: 10px auto;
        background-color: red;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: bold;
        cursor: pointer;
    }

    .clear-btn:hover {
        background-color: darkred;
    }

    /* Footer text */
    .footer-text {
        text-align: center;
        font-weight: 400;
        font-size: 16px;
        margin-top: 5px;
    }
    """
)



















