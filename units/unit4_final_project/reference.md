- [30 Score, uses SmolAgents](https://huggingface.co/spaces/a-ge/Final_Assignment_Template/blob/main/app.py)
  - Prompt Used
  ```python
  answer = self.agent.run(
            f"""You are a general AI assistant.You can use the provided tools and websearch for finding answers. I will ask you a question. Report your thoughts, and finish your answer. YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string.
            {question}""",
        )
    ```
- [95 Score, handles file processing](https://huggingface.co/spaces/susmitsil/FinalAgenticAssessment/tree/main)
