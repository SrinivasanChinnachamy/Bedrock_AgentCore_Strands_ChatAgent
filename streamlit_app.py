import streamlit as st
import boto3
import json
import time

# Page configuration
st.set_page_config(
    page_title="Strands Chat Agent built on Bedrock Agentcore",
    page_icon="🤖",
    layout="centered"
)

# Initialize the agent runtime
@st.cache_resource
def init_agent():
    return boto3.client('bedrock-agentcore', region_name='us-east-1')

# App title
st.title("🤖 Strands Chat Agent built on Bedrock Agentcore")
st.write("Ask your agent for simple math calculations, text processing, and unit conversions")

# Initialize agent
try:
    agentcore_runtime = init_agent()
    st.success("✅ Agent connected successfully!")
except Exception as e:
    st.error(f"❌ Failed to connect to agent: {str(e)}")
    st.stop()

# Initialize session state
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if 'last_response' not in st.session_state:
    st.session_state.last_response = None
if 'response_time' not in st.session_state:
    st.session_state.response_time = None

# Check for query parameters from example buttons
query_params = st.query_params
example_prompt = query_params.get("prompt", "")

# Input field - clear if flag is set
input_value = "" if st.session_state.clear_input else example_prompt
if st.session_state.clear_input:
    st.session_state.clear_input = False

user_prompt = st.text_input(
    "Enter your prompt:",
    value=input_value,
    placeholder="e.g., Calculate 15 + 25 or What's the weather?",
    key="user_input"
)

# Auto-submit if triggered by example button
auto_submit = query_params.get("auto_submit", "") == "true"
if auto_submit:
    # Clear the auto_submit flag
    st.query_params.pop("auto_submit", None)
    submit_clicked = True
else:
    submit_clicked = False

# Submit button
if st.button("Send", type="primary") or submit_clicked:
    if user_prompt:
        with st.spinner("🤔 Agent is thinking..."):
            try:
                # Start timing
                start_time = time.time()
                
                # Call the agent
                response = agentcore_runtime.invoke_agent_runtime(
                    agentRuntimeArn="arn:aws:bedrock-agentcore:us-east-1:154594000270:runtime/strands_claude_getting_started-2YB1UD8sbu",
                    #agentRuntimeArn="arn:aws:bedrock-agentcore:us-east-1:154594000270:runtime/hosted_agent_akljv-tDq6YRD9Ht",
                    payload=json.dumps({"prompt": user_prompt}).encode('utf-8')
                )
                
                # End timing
                end_time = time.time()
                response_time = end_time - start_time
                
                # Read the streaming response body
                response_body = response['response'].read().decode('utf-8')
                
                # Debug: Show raw response
                st.write("Raw response body:", response_body)
                
                try:
                    # Try to parse as JSON
                    response_data = json.loads(response_body)
                    if isinstance(response_data, dict) and 'response' in response_data:
                        agent_response = response_data['response'][0].strip()
                    else:
                        agent_response = str(response_data)
                except json.JSONDecodeError:
                    # If it's not JSON, use the raw response
                    agent_response = response_body.strip()
                
                # Store response and timing in session state
                st.session_state.last_response = agent_response
                st.session_state.response_time = response_time
                st.session_state.clear_input = True
                st.query_params.pop("prompt", None)
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a prompt first!")

# Display last response if available
if st.session_state.last_response:
    # Display response time
    if st.session_state.response_time:
        st.success(f"🎉 Response received in {st.session_state.response_time:.2f} seconds!")
    else:
        st.success("🎉 Response received!")
    
    st.text_area(
        "Agent Response:",
        value=st.session_state.last_response,
        height=150,
        disabled=True
    )
    
    # Display timing details
    if st.session_state.response_time:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Response Time", f"{st.session_state.response_time:.2f}s")
        with col2:
            if st.session_state.response_time < 2:
                st.metric("Performance", "⚡ Fast")
            elif st.session_state.response_time < 5:
                st.metric("Performance", "✅ Good")
            else:
                st.metric("Performance", "⏳ Slow")
# Footer
st.markdown("---")
st.markdown("*Powered by Amazon Bedrock AgentCore Runtime & Strands Agents*")