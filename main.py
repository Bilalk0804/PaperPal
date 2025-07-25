from dotenv import load_dotenv
import os
from langchain_ollama import OllamaLLM

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.chat_models import init_chat_model
from langchain.agents import create_tool_calling_agent,AgentExecutor
#from langchain_huggingface import HuggingFaceEndpoint
from pydantic import BaseModel
#from tools import search_tool,wiki_tool, save_tool
load_dotenv()
llm = init_chat_model("mistralai/mixtral-8x7b-instruct-v0.1", model_provider="Nvidia", api_key=os.getenv("NVIDIA_API_KEY"))

'''Experimental code to use HuggingFaceEndpoint, currently not working due to custom tooling.'''
# llm = HuggingFaceEndpoint(
#     #repo_id="HuggingFaceH4/zephyr-7b-beta",
#     temperature=0.5,
#     huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
#     model='HuggingFaceH4/zephyr-7b-beta')
'''Test run to check if the LLM is working correctly.'''
# prompt="Tell me how is an agent different from a tool in the context of LLMs"
# response = llm.invoke(prompt)
# for chunk in llm.stream(prompt):
#    print(chunk.content, end='')

# prompt="I know you are a model but I still like you"
# print(llm.invoke(prompt))

"""Main model working is beggining from here we will be working with 2 models acutally embeddings and the LLM."""
model=OllamaLLM(model="deepseek-r1:latest")

template="""You are an AI assistant designed for answering queries using Retrieval-Augmented Generation (RAG). You will process user questions by first searching      
through the provided documents (PDFs or emails) to retrieve relevant information, then generate a concise and accurate response based on that context.      
If no matching content is found, state explicitly that you cannot answer from the documents and provide reasoning."  

---

**User Prompt Format:**  
```  
Documents: [Insert list of PDF/emails here]  
Query: {user_question}  
```

---

### **Example Workflow**  
1. **Human Input (PDF):** "What is the company's revenue growth in 2023?"  
   - System retrieves relevant data from all uploaded PDFs containing financial reports or summaries.  

2. **Human Input (Email):** "I need to know the details of Project Alpha mentioned in this email."  
   - System scans emails for keywords like "Project Alpha" and extracts key points.  

---

### **Prompt Template**  
```  
## Role: RAG Assistant  
- Task 1: Retrieve relevant passages from the provided documents (PDFs or emails) based on the user's query.  
- Task 2: Use ONLY the retrieved context to answer accurately, citing sources if possible.  

## Instructions:  
{%- if documents -%}  
If any documents are provided, search them for content directly related to the query and prioritize exact matches or summaries.  
{%- else -%}  
No documents are available—answer based on your training data only (if applicable) and explicitly state this limitation.  
{%- endif %}  

## Documents Provided:  
{{#documents}}  
### Document {{@index + 1}}:  
{{this}}  
{% if multi_doc == true then more formatting for list view %}  
{%- endif %}  

## Query:
{{input}}

## Response Format:
Answer concisely. If multiple sources are relevant, summarize key points from each and cite by document title/section (if known). Example structure:

**Answer:** [Your synthesized response here]
**Sources:** [List relevant documents or sections in bullet points if needed.]
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model
print(chain.invoke({"question": "What is the capital of France?", "document_list": "Paris is the capital of France."}))
