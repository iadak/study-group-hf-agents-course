import argparse

from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool
from retriever import GuestInfoRetrieverTool, generate_docs
from tools import WeatherInfoTool, HubStatsTool


def parse_args():
    parser = argparse.ArgumentParser(description="Run the agentic RAG application")
    parser.add_argument("--prompt", type=str, default="Tell me about our guest named 'Lady Ada Lovelace'.", help="Prompt to use")
    parser.add_argument("--multiple_steps", type=bool, default=False, help="Whether to use multiple steps")
    return parser.parse_args()

model = LiteLLMModel(
    model_id="ollama_chat/qwen2.5-coder:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

# Init Guest Info Retriever Tool
docs = generate_docs()
guest_info_tool = GuestInfoRetrieverTool(docs)

# Init Other tools
search_tool = DuckDuckGoSearchTool()
weather_info_tool = WeatherInfoTool()
hub_stats_tool = HubStatsTool()

alfred = CodeAgent(
    name="Alfred",
    description="A helpful assistant that can retrieve information about our guests and answer questions about them.",
    model=model,
    tools=[
        guest_info_tool,
        search_tool,
        weather_info_tool,
        hub_stats_tool
    ],
    add_base_tools=True,
    planning_interval=3,
    max_steps=3,
    verbosity_level=2,
)

if __name__ == "__main__":
    args = parse_args()
    print(f"Starting agentic RAG application with prompt: {args.prompt}")
    response = alfred.run(args.prompt)
    print("🎩 Alfred's Response:")
    print(response)
    if args.multiple_steps:
        while True:
            user_input = input("Enter a new prompt (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                break
            response = alfred.run(user_input, reset=False)
            print("🎩 Alfred's Response:")
            print(response)
