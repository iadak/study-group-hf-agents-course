# Hugging Face Agents Course Study Group

This repo contains the resources for the Hugging Face Agents Course Study Group conducted by Batch 6 of the Advance DL Course to continue the learning of the participants after the course completion.

# Tentitive Plan

This plan covers the course content for the until unit 4 by using one of the Agentic Frameworks. Rest of the course plan will decided after completion of unit 4 and based on the interest of the participants.
| Unit | Date | Description | Session Notes |
|------|------|-------------|-------|
|Study Group Kickoff | 2025-06-01 | Participant Introduction, Course Overview, Discuss Tentitive Plan | [Session Notes](session_notes/01_kickoff.md)|
|[Unit 1. Introduction to Agents](https://huggingface.co/learn/agents-course/unit1/introduction)| 2025-06-07 | Understanding Agents, The Role of LLMs in Agents, Tools and Actions, The Agent Workflow | [Session Notes](session_notes/02_unit1_discussion.md)|
| [Unit 2. Introduction to Agentic Frameworks](https://huggingface.co/learn/agents-course/unit2/introduction) | 2025-06-14 | - [SmolAgents](https://huggingface.co/docs/smolagents/en/index), [LlamaIndex](https://www.llamaindex.ai/), [LangGraph](https://www.langchain.com/langgraph) | NA |
| [Unit 3. Use Case for Agentic RAG](https://huggingface.co/learn/agents-course/unit3/agentic-rag/introduction) | 2025-06-21 | - RAG, Agentic RAG, Agentic RAG with smolagents | [Session Notes](session_notes/03_unit_2_and_3_discussion.md)|
| [Unit 4. Final Unit Project](https://huggingface.co/learn/agents-course/unit4/introduction) | 2025-06-28 |  |

# Local Setup

## Environment Setup
```bash
uv venv --python 3.11
source .venv/bin/activate
pip install -r requirements.txt
```

Refer [uv](https://docs.astral.sh/uv/) for more details on the uv package manager.

## Generate Hugging Face API Token

- Go to [Hugging Face](https://huggingface.co/) and login with your GitHub account.
- Go to [API Tokens](https://huggingface.co/settings/tokens) and generate a new token.
- Copy the token and paste it in the `.env` file in the root of the project.

```bash
echo "HF_TOKEN=hf_..." >> .env
```

# Resources

- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/)
- [Hugging Face Agents Course Github Repo](https://github.com/huggingface/agents-course)
- [smolagents](https://huggingface.co/docs/smolagents/en/index)
