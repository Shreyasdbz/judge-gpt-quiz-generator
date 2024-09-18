import os

from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if GITHUB_TOKEN is None:
    raise ValueError(
    '''
    [headline_generation] API key is not set. 
    Please set the GITHUB_TOKEN environment variable.
    '''
    )

_client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(GITHUB_TOKEN),
    model="model-should-be-specified-with-each-call")

def get_client(): return _client;