from notion.client import NotionClient
import os

secret_code = os.environ('')

client = NotionClient(token_v2=secret_code)
