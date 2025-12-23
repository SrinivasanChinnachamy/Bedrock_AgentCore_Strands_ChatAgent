from strands import Agent
from strands_tools import calculator # Import the calculator tool
import argparse
import json
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel

# Import custom tools
from tools.weather import weather
from tools.time_tool import get_time
from tools.random_tools import random_number, random_color
from tools.text_tools import text_length, reverse_text
#from tools.conversion_tools import celsius_to_fahrenheit, kilometers_to_miles

app = BedrockAgentCoreApp()

model_id = "anthropic.claude-3-haiku-20240307-v1:0"
model = BedrockModel(
    model_id=model_id,
)
agent = Agent(
    model=model,
    tools=[
        calculator,
        weather,
        get_time,
        random_number,
        text_length,
        reverse_text,
        celsius_to_fahrenheit,
        kilometers_to_miles,
        random_color
    ],
    system_prompt="""You are a helpful AI assistant equipped with multiple specialized tools to assist users with various tasks.

Available Tools:

📊 CALCULATIONS & MATH:
- calculator: Perform mathematical calculations (addition, subtraction, multiplication, division, etc.)
- random_number: Generate random numbers within specified ranges

🌤️ WEATHER & TIME:
- weather: Get current weather conditions and temperature
- get_time: Retrieve current date and time in IST (GMT+5:30) in IST (GMT+5:30)

📝 TEXT PROCESSING:
- text_length: Count characters in any text string
- reverse_text: Reverse the order of characters in text

🔄 UNIT CONVERSIONS:
- celsius_to_fahrenheit: Convert temperature from Celsius to Fahrenheit
- kilometers_to_miles: Convert distance from kilometers to miles

🔐 UTILITIES:
- random_color: Pick random color names for creative projects

When you use tools to answer questions, please provide a complete and helpful response first, then mention which tool(s) you used at the end in the format: "[Tool used: tool_name]".

I'm ready to help you with calculations, weather checks, time queries, text manipulation, unit conversions, and more. Just ask me what you need!"""
)

@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    try:
        user_input = payload.get("prompt")
        if not user_input:
            return "Please provide a prompt"
        
        print("User input:", user_input)
        response = agent(user_input)
        return response.message['content'][0]['text']
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return f"Sorry, I encountered an error: {str(e)}"

if __name__ == "__main__":
    app.run()

#if __name__ == "__main__":
#   parser = argparse.ArgumentParser()
#   parser.add_argument("payload", type=str)
#   args = parser.parse_args()
#   response = strands_agent_bedrock(json.loads(args.payload))
