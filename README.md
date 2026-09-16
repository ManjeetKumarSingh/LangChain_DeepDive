

<p align="center">

### LangChain Enterprise AI
<strong>Author: Manjeet KUMAR</strong><br>
<em>AI & Cloud Architect</em>

<img src="https://img.shields.io/badge/LangChain-Agentic%20AI-1C3C3C?style=for-the-badge">
<img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white">

</p>

```bash
pip install \
  langchain \
  langchain-core \
  langgraph \
  langchain-community \
  langchain-text-splitters \
  pydantic \
  pydantic-settings \
  fastapi \
  uvicorn[standard] \
  boto3 \
  langchain-aws \
  python-dotenv \
  httpx \
  tenacity
```
### How to install these packages using the requirements.txt file 

* `python3 -m pip install -r requirements.txt`


### Details of the packages need to be installed 

1. `langchain`     Main LangChain framework

2. `langchain-core`  Messages, runnables, prompts, tools

3. `langgraph`      Agent/workflow orchestration

4. `langchain-community`  Community integrations

5. `langchain-text-splitters`   Document chunking

6. `pydantic`  Data/schema validation

7. `pydantic-settings`  Configuration management

8. `fastapi` Production API

9. `uvicorn` ASGI server

10. `boto3`  AWS SDK

11. `langchain-aws` Bedrock/AWS LangChain integration

12. `python-dotenv` Local environment variables

13. `httpx` Async HTTP calls

14. `tenacity` Retry policies


### How to get all the list of dependecy it got installed 

* `pip list` 

```json
Package                  Version
------------------------ -----------
aiohappyeyeballs         2.7.1
aiohttp                  3.14.3
aiosignal                1.4.0
annotated-doc            0.0.5
annotated-types          0.8.0
anyio                    3.7.1
attrs                    26.1.0
boto3                    1.43.96
botocore                 1.43.96
certifi                  2026.7.22
charset-normalizer       3.5.1
click                    8.5.0
dataclasses-json         0.6.7
distro                   1.9.0
fastapi                  0.141.1
frozenlist               1.8.0
h11                      0.12.0
httpcore                 0.15.0
httpx                    0.23.0
httpx-sse                0.4.3
idna                     3.19
jmespath                 1.1.0
jsonpatch                1.33
jsonpointer              3.1.1
langchain                0.3.30
langchain-aws            0.2.35
langchain-community      0.3.31
langchain-core           0.3.86
langchain-text-splitters 0.3.11
langgraph                0.2.35
langgraph-checkpoint     2.1.2
langsmith                0.11.2
marshmallow              3.26.2
multidict                6.8.0
mypy_extensions          1.1.0
numpy                    2.5.3
orjson                   3.12.0
ormsgpack                1.12.2
packaging                25.0
pip                      26.2.1
propcache                0.5.4
pydantic                 2.13.5
pydantic_core            2.46.5
pydantic-settings        2.15.0
python-dateutil          2.9.0.post0
python-dotenv            1.2.3
PyYAML                   6.0.3
requests                 2.34.2
requests-toolbelt        1.0.0
rfc3986                  1.5.0
s3transfer               0.19.2
six                      1.17.0
sniffio                  1.3.1
SQLAlchemy               2.0.54
starlette                1.6.0
tenacity                 9.1.4
typing_extensions        4.16.0
typing-inspect           0.9.0
typing-inspection        0.4.4
urllib3                  2.8.0
uuid_utils               0.17.1
uvicorn                  0.53.0
websockets               17.1
xxhash                   4.0.1
yarl                     1.25.1
zstandard                0.25.0
```

### Important topics we need to learn about the Langchain is :

```text
Runnable
   │
   ├── RunnableSequence
   ├── RunnableParallel
   ├── RunnableLambda
   ├── RunnablePassthrough
   └── RunnableBranch

Chain
   │
   ├── Chain
   ├── LLMChain
   ├── MemoryChain
   ├── SequentialChain
   ├── ParallelChain
   ├── EventChain
   ├── EventLoopChain
   ├── EventLoopChainWithCallback
   ├── EventLoopChainWithQueue
   ├── EventLoopChainWithQueueAndCallback
   ├── EventLoopChainWithQueueAndCallbackWithTimeout
   ├── EventLoopChainWithQueueAndCallbackWithTimeoutAndRetry
   ├── EventLoopChainWithQueueAndCallbackWithTimeoutAndRetryAndConcurrency
   ├── EventLoopChainWithQueueAndCallbackWithTimeoutAndRetryAndConcurrencyAndMaxConcurrency
   ├── EventLoopChainWithQueueAndCallbackWithTimeoutAndRetryAndConcurrencyAndMaxConcurrencyAndMaxQueueSiz

   ```

### Langchain chaining concepts
*LCEL / Runnable*
This is one of the most important LangChain concepts.
`chains/basic_chain.py`

```python
from app.models.chat_model import model
from app.prompts.chat_prompts import chat_prompt

chain = chat_prompt | model
      
response = chain.invoke({
"question": "What is RAG?"
})

```

