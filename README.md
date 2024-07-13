# llm-Zoomcamp

## docker commands to run elastic search and ollama in local

```yml

    docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3


    docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama

```

## code snippet to create openAI client for ollama or any other LLM

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
```

## Code to pull phi3 model from ollama service

```bash

ollama start
ollama pull phi3
ollama run phi3

```
