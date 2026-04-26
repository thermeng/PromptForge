import streamlit as st
from agent_runner import stream_agent

st.set_page_config(page_title="PromptForge", layout="wide")

st.title("🤖 PromptForge")

# -------------------------------
# Sidebar - Model Selection
# -------------------------------
st.sidebar.header("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Select Model",
    [
        "google/gemma-3-27b-it",
        "nvidia/nemotron-3-super-120b-a12b:free"
    ]
)

# -------------------------------
# Session State
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Clear Chat Button
# -------------------------------
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# -------------------------------
# Display chat history
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Type your message...")

# -------------------------------
# Handle Input
# -------------------------------
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_output = ""

        try:
            stream = stream_agent(user_input, model_name)

            for chunk in stream:
                full_output = chunk
                placeholder.markdown(full_output + "▌")

            placeholder.markdown(full_output)

        except Exception as e:
            full_output = f"❌ Error: {str(e)}"
            placeholder.markdown(full_output)

    # Save response
    st.session_state.messages.append(
        {"role": "assistant", "content": full_output}
    )