import requests
import gradio as gr

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_ollama(model, prompt):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    result = response.json()
    return result.get("response", "")

def chat_with_model(prompt, model):
    return query_ollama(model, prompt)

with gr.Blocks(title="Ollama Chatbot") as demo:
    gr.Markdown("## 🤖 Ollama Chatbot (Gradio UI)")

    model = gr.Textbox(
        value="tinyllama",
        label="Model Name",
        placeholder="Enter your Ollama model name"
    )

    user_input = gr.Textbox(
        label="Your Question",
        placeholder="Ask something...",
        lines=3
    )

    output = gr.Textbox(
        label="Model Response",
        lines=6
    )

    submit_btn = gr.Button("Submit")

    submit_btn.click(
        fn=chat_with_model,
        inputs=[user_input, model],
        outputs=output
    )

demo.launch()
