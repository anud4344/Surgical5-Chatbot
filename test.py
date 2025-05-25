import ollama
import streamlit as st
from utilities.icon import page_icon

st.set_page_config(
    page_title="Chat playground",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

def extract_model_names(models_info) -> tuple:
    """
    Extract model names from a list or tuple of Model objects returned by ollama.list().
    """
    return tuple(getattr(model, "model", str(model)) for model in models_info)

def main():
    page_icon("💬")
    st.subheader("Ollama Playground", divider="red", anchor=False)

    try:
        # models_info = ollama.list()  # Returns list or tuple of Model objects
        models_info = ollama.list().get("models", [])
        available_models = extract_model_names(models_info)
    except Exception as e:
        st.error(f"Failed to list models: {e}")
        return

    if available_models:
        selected_model = st.selectbox(
            "Pick a model available locally on your system ↓", available_models
        )
    else:
        st.warning("You have not pulled any model from Ollama yet!", icon="⚠️")
        if st.button("Go to settings to download a model"):
            st.switch_page("pages/setup.py")
        return

    message_container = st.container(height=500, border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter a prompt here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        message_container.chat_message("user", avatar="😎").markdown(prompt)

        try:
            with message_container.chat_message("assistant", avatar="🤖"):
                with st.spinner("Model working..."):
                    response = ollama.chat(
                        model=selected_model,
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ]
                    )
                    answer = response["message"]["content"]
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"Error from model: {str(e)}", icon="⛔️")

if __name__ == "__main__":
    main()
