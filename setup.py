# pages/setup.py
import streamlit as st
import ollama
from time import sleep
from utilities.icon import page_icon

st.set_page_config(
    page_title="Model Management",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    page_icon("⚙️")
    st.subheader("Model Management", divider="red", anchor=False)

    st.subheader("Download Models", anchor=False)
    model_name = st.text_input("Enter model name ↓", placeholder="mistral")
    if st.button(f"📥 :green[Download] :red[{model_name}]"):
        if model_name:
            try:
                ollama.pull(model_name)
                st.success(f"Downloaded: {model_name}", icon="🎉")
                st.balloons()
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Download failed: {e}", icon="😳")
        else:
            st.warning("Enter a model name.", icon="⚠️")

    st.divider()

    st.subheader("Create Model", anchor=False)
    modelfile = st.text_area("Enter modelfile", height=100, placeholder="FROM mistral\nSYSTEM You are mario...")
    create_name = st.text_input("Model name to create", placeholder="mario")
    if st.button("🆕 Create Model"):
        if create_name and modelfile:
            try:
                ollama.create(model=create_name, modelfile=modelfile)
                st.success(f"Created: {create_name}", icon="✅")
                st.balloons()
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Create failed: {e}", icon="😳")
        else:
            st.warning("Enter both model name and modelfile.", icon="⚠️")

    st.divider()

    st.subheader("Delete Models", anchor=False)
    try:
        available_models = [m.model for m in ollama.list().models]
    except Exception as e:
        st.error(f"Failed to list models: {e}", icon="🛑")
        return

    if available_models:
        selected = st.multiselect("Select models to delete", available_models)
        if st.button("🗑️ :red[Delete Selected]"):
            for model in selected:
                try:
                    ollama.delete(model)
                    st.success(f"Deleted: {model}", icon="🎉")
                    st.balloons()
                    sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Delete failed: {e}", icon="😳")
    else:
        st.info("No models found.", icon="🦗")

if __name__ == "__main__":
    main()
