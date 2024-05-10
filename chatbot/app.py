# Just runs .complete to make sure the LLM is listening
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

llm = Ollama(model="cniongolo/biomistral:latest")

response = llm.complete("Write an essey about corona virus of 5000 words.")
print(response)