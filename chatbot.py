import gradio as gr

# ---- Bot Reply Function ----
def customLLMBot(message, history):
    # You can modify this logic later to use a real AI model
    return f"You asked: {message}. I am here to help with hospital and healthcare questions."

# ---- Chat Interface ----
iface = gr.ChatInterface(
    fn=customLLMBot,
    chatbot=gr.Chatbot(height=300, type="messages"),  # Updated format
    textbox=gr.Textbox(placeholder="Ask me any healthcare or hospital-related question"),
    title="🏥 Hospital Assistance ChatBot",
    description="🤖 Chatbot for hospital guidance, medical information, and healthcare support.",
    theme="soft",
    examples=[
        "Hi",
        "What are the duties of a nurse?",
        "How do I get a medical certificate?",
        "What is informed consent in hospitals?",
        "When should a patient be admitted to ICU?"
    ]
)

# ---- Run the App ----
iface.launch()
