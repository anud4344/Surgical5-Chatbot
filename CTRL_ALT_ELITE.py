import ollama
import streamlit as st
from utilities.icon import page_icon
from base64 import b64encode

st.set_page_config(
    page_title="CTRL-ALT-Elite playground",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

page_bg_color = """
<style>
  
   [data-testid="stAppViewContainer"] {
      background-color: #387fd6;
     }

    div[data-testid="stChatMessageList"] {
    background-color: black;
    border-radius: 10px;
    paddi/ng: 10px;
    max-height: 500px;
    overflow-y: auto;
    margin-top: 16px;
    }

   
   div[data-testid="stChatInput"] {
    #   margin-left: -1rem  !important;
    #   margin-right: -1rem !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    width: 100% !important;
    }


    div[data-testid="stChatInput"] textarea {

      background-color: #d40003;
    #   background-color: white; 
      color: white !important;
      border-radius: 8px !important;
      padding: 8px 12px !important;
      width: 100% !important;
      box-sizing: border-box;
      min-height: 40px !important;
      height: auto;
      resize: none !important;
      font-size: 16px !important;
      
    }

    div[data-testid="stChatInput"] textarea::placeholder {
      color: black !important;  
    }

    .chatbot-response {
    font-size: 23px !important;
}
</style>
"""

st.markdown(page_bg_color, unsafe_allow_html=True)
           

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()
    
img = get_base64_image("surgical5_logo.jpg")

def extract_model_names(models_info) -> tuple:
    """
    Extract model names from a list or tuple of Model objects returned by ollama.list().
    """
    return tuple(getattr(model, "model", str(model)) for model in models_info)

def main():

    page_icon("🩺")

    
    st.markdown(
       f"""
         <div style="text-align: center; margin-bottom: 50px;">
             <img src = "{img}" style = "width: 250px; height: 250px">
              <h2> Surgic@l5 - Medical AI chatbot </h2>
              <p style = "font-size: 20px;">Your AI-powered chatbot for medical diagnostics and assistance.</p>
         </div>
       """,
       unsafe_allow_html = True
     )
    
   
    try:
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
    
    
   
    message_container = st.container(height=500, border = True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "You are a medical assistant" else "😎"
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
                    # st.markdown(answer)
                    st.markdown(
    f"""
    <div class="chatbot-response">
        <p style="white-space: pre-wrap;">{answer}</p>
    </div>
    """,
    unsafe_allow_html=True
)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"Error from model: {str(e)}", icon="⛔️")
            
    st.sidebar.title("Navigation")
    if st.sidebar.button("Show README"):
        st.session_state.show_readme = not st.session_state.get("show_readme", False)

    if st.session_state.get("show_readme"):
        st.markdown("---") # Separator for better visual
        st.header("About This App")
        try:
            # Assuming README.md is in the same directory as your app.py
            with open("README.md", "r", encoding="utf-8") as f:
                readme_content = f.read()
            st.markdown(readme_content, unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning("README.md not found in the current directory.")
        st.markdown("---") # Separator
    

if __name__ == "__main__":
    main()