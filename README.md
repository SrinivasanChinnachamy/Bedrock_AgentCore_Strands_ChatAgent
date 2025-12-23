# Strands ChatAgent on Amazon Bedrock AgentCore

A conversational AI agent built with Strands Agents framework and hosted on Amazon Bedrock AgentCore Runtime. This agent provides multiple specialized tools for calculations, weather information, text processing, and unit conversions.

## 🏗️ Architecture

This project demonstrates how to:
- Build an agent using the Strands Agents framework
- Integrate with Amazon Bedrock models (Claude 3 Haiku)
- Deploy and host on Amazon Bedrock AgentCore Runtime
- Create a Streamlit web interface for user interaction

## 🛠️ Features

### Available Tools
- **📊 Calculator**: Mathematical calculations and operations
- **🌤️ Weather**: Current weather conditions
- **⏰ Time**: Current date and time in IST (GMT+5:30)
- **🔢 Random Number**: Generate random numbers within ranges
- **🎨 Random Color**: Pick random color names
- **📝 Text Length**: Count characters in text strings
- **🔄 Reverse Text**: Reverse character order in text

## 📋 Prerequisites

- Python 3.8+
- AWS Account with Bedrock access
- AWS CLI configured with appropriate permissions
- Amazon Bedrock AgentCore Runtime setup

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Bedrock_AgentCore_Strands_ChatAgent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials**
   ```bash
   aws configure
   ```

## 🏃‍♂️ Usage

### Running the Agent Locally

```bash
python agents/strands_chatagent.py
```

### Running the Streamlit Web Interface

```bash
streamlit run streamlit_app.py
```

The web interface will be available at `http://localhost:8501`

### Example Interactions

- **Math**: "Calculate 15 + 25 * 3"
- **Weather**: "What's the weather like?"
- **Time**: "What time is it?"
- **Text Processing**: "What's the length of 'Hello World'?"
- **Random**: "Give me a random number between 1 and 100"

## 📁 Project Structure

```
Bedrock_AgentCore_Strands_ChatAgent/
├── agents/
│   └── strands_chatagent.py    # Main agent implementation
├── tools/
│   ├── __init__.py
│   ├── random_tools.py         # Random generation tools
│   ├── text_tools.py          # Text processing tools
│   ├── time_tool.py           # Time-related tools
│   └── weather.py             # Weather information tool
├── streamlit_app.py           # Web interface
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Configuration

### Agent Runtime ARN
Update the `agentRuntimeArn` in `streamlit_app.py` with your deployed agent's ARN:

```python
agentRuntimeArn="arn:aws:bedrock-agentcore:us-east-1:YOUR_ACCOUNT:runtime/YOUR_RUNTIME_ID"
```

### Model Configuration
The agent uses Anthropic Claude 3 Haiku by default. To change the model, update the `model_id` in `agents/strands_chatagent.py`:

```python
model_id = "anthropic.claude-3-haiku-20240307-v1:0"
```

## 🚀 Deployment

1. **Package the agent**
   ```bash
   zip -r agent.zip agents/ tools/ requirements.txt
   ```

2. **Deploy to Bedrock AgentCore**
   Use the AWS CLI or Console to deploy your agent package to Bedrock AgentCore Runtime.

3. **Update the Streamlit app**
   Replace the `agentRuntimeArn` with your deployed agent's ARN.

## 🧪 Testing

Test individual tools:

```python
from tools.weather import weather
from tools.time_tool import get_time
from strands_tools import calculator

# Test weather tool
print(weather())

# Test time tool
print(get_time())

# Test calculator
print(calculator("15 + 25"))
```

## 📊 Performance

- **Response Time**: Typically 1-3 seconds
- **Model**: Claude 3 Haiku (fast and cost-effective)
- **Concurrent Users**: Supports multiple simultaneous conversations

## 🔒 Security

- Uses AWS IAM for authentication and authorization
- All communications encrypted in transit
- No sensitive data stored locally
- Tools designed with safety constraints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your tools in the `tools/` directory
4. Update the agent configuration
5. Test thoroughly
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Agent Runtime Not Found**
   - Verify the `agentRuntimeArn` is correct
   - Ensure the runtime is deployed and active

2. **Permission Denied**
   - Check AWS credentials and permissions
   - Verify Bedrock access is enabled

3. **Tool Import Errors**
   - Ensure all dependencies are installed
   - Check Python path configuration

### Debug Mode

Enable debug logging in the agent:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Support

For issues and questions:
- Check the troubleshooting section
- Review AWS Bedrock AgentCore documentation
- Open an issue in the repository

---

*Built with ❤️ using Strands Agents and Amazon Bedrock AgentCore*
