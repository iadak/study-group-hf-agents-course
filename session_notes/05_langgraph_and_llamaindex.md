# HF Agents Course Study Group: LangGraph and LlamaIndex - July 05

> Notes are generated using Fathom

---
## Meeting Purpose

Review LangGraph and LlamaIndex implementations and discuss progress on course projects.

## Key Takeaways

  - LangGraph provides more control and structure for production AI applications compared to smolagents
  - Multiple participants still working through course units; some have completed projects
  - Group will spend one more week on current course before moving to MCP for ~3 weeks
  - Additional resources available: LangChain Academy courses, GitHub repo with example code

## Topics

### Course Progress Updates

  - Gayathri: Completed project using LangMindex, got ~6-7 questions correct
  - Pravin & Roshan: On Unit 2, still working through Small Agents section
  - Ramya: First time joining, hasn't started course materials yet
  - Project deadline for certification passed on June 30th, but course still accessible

### LlamaIndex Overview

  - Requires installing multiple granular packages vs. single install for other frameworks
  - Known for strong document parsing capabilities
  - Example demonstrated:
      - Loading dataset into local directory
      - Creating ingestion pipeline (sentence splitter, embeddings)
      - Storing in ChromaDB vector database
      - Querying data store with SQL engine

### LangGraph Deep Dive

  - Uses directed graph structure to define workflow
  - Key components: nodes (Python functions), edges (connections), state (info passed between nodes)
  - Provides more control than free-form agents, useful for production applications
  - Example walkthrough:
      - Email processing system (classify spam/legitimate, draft responses)
      - Image processing and calculation agent using LLM-bound tools

### Framework Comparisons

  - Small Agents: Minimalistic, good for simple agents where LLM controls flow
  - LlamaIndex: More mature, but complex setup with many packages
  - LangGraph: Most intuitive for production use, offers workflow control

## Next Steps

  - Participants to continue working on course units/projects
  - Review bonus units and share project progress next week
  - Wrap up current course next week
  - Move to MCP course for ~3 weeks after
  - Explore additional resources: LangChain Academy courses, example code in shared GitHub repo
