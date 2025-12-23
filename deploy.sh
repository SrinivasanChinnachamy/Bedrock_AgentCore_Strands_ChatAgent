#!/usr/bin/env python3

# Deployment script for Strands Agent with Bedrock AgentCore
print("🚀 Starting deployment process...")

# Importing necessary libraries and establishing session
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session

boto_session = Session()
region = boto_session.region_name
agentcore_runtime = Runtime()

# Begin AgentCore Configuration
agent_name = "strands_chat_agent"
configuration = agentcore_runtime.configure(
    entrypoint="agents/strands_chat_agent.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    agent_name=agent_name
)
print(configuration)

# Trigger AgentCore deployment and Launch Runtime
launch_agent = agentcore_runtime.launch()
print(f"Agent launched: {launch_agent}")