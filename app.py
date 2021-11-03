from notion.client import NotionClient
import os

secret_code = os.environ('NOTION_TOKEN_V2')

client = NotionClient(token_v2=secret_code)

print("Welcome to NotionPy!")
print("Warning: This project is currently a work-in-progress. To be sure that you don't accidentally edit the wrong page, please be sure to update your tokens to match your page.")
learnTokenReg = input("Do you know how to find / change your Notion token?")
if learnTokenReg.lower() == "yes":
    pass
else:
    print("To find your Notion token, head to where you can see your browser cookies (on Chrome, open Settings, then open Privacy & Security, then navigate to: Cookies -> See All Cookies -> notion.so, after which you'll want to find your \"token_v2\" token. Copy / paste that into your .ENV file as \"NOTION_TOKEN_V2\".)")
    pass
