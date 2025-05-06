import os
import requests

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
gitea_status = os.getenv("gitea_status")
TIME_TAKEN = os.getenv("Time_Taken")
COMMIT = os.getenv("Commit")
REPO = os.getenv("Repo")
EVENT_NAME = os.getenv("EVENT_NAME")
ACTOR = os.getenv("ACTOR")
FULL_BRANCH_NAME = os.getenv("BRANCH")
BRANCH = FULL_BRANCH_NAME.split("/")
COMMIT_MESSAGE = os.getenv("COMMIT_MESSAGE") 
BUILD_NO = os.getenv("BUILD_NO")
BUILD_START = os.getenv("BUILD_START")

print(BUILD_START)
if not WEBHOOK_URL:
    print("Error: WEBHOOK_URL is not set.")
    exit(1)

message_card = {
                "type": "message",
                "attachments":
                [
                    {
                        "contentType": "application/vnd.microsoft.card.adaptive",
                        "content":
                        {
                            "type": "AdaptiveCard",
                            "body":
                            [
                                {
                                    "type": "TextBlock",
                                    "text": f"{ACTOR} made changes",
                                    "size": "large",
                                    "weight": "bolder"
                                },
                                {
                                    "type":"TextBlock",
                                    "text": f"Status: {'✅ Success' if gitea_status == 'success' else '❌ Failure'}",
                                    "size": "large",
                                    "weight": "bolder"
                                },
                                {
                                    "type":"TextBlock",
                                    "text": f"The workflow was triggered by {EVENT_NAME}"

                                },
                                {
                                    "type":"TextBlock",
                                    "text": f"Time Taken: {TIME_TAKEN} sec"
                                },
                                {
                                    "type":"TextBlock",
                                    "text": f"Build Start Time: {BUILD_START}"   
                                },
                                {
                                    "type":"TextBlock",
                                    "text":f"Commit Message: [{COMMIT_MESSAGE}](http://localhost:3000/{REPO}/commit/{COMMIT})"
                                },
                                {
                                    "type":"TextBlock",
                                    "text": f"[View Commit](http://localhost:3000/{REPO}/commit/{COMMIT})"
                                },
                                {
                                    "type":"TextBlock",
                                    "text":f"Repo: [{REPO}](http://localhost:3000/{REPO}) and The Branch is {BRANCH[-1]}"
                                }
                            ],
                            "actions":
                            [
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "Commit Link",
                                    "url": f"http://localhost:3000/{REPO}/commit/{COMMIT}",
                                    "role": "button"
                                },
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "Repo Link",
                                    "url": f"http://localhost:3000/{REPO}",
                                    "role": "button"
                                },
                                {
                                    "type": "Action.OpenUrl",
                                    "title": "BUILD Link",
                                    "url": f"http://localhost:3000/{REPO}/actions/runs/{BUILD_NO}",
                                    "role": "button"
                                }
                            ],
                            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                            "version": "1.5"
                        }
                    }
                ]
            }

response = requests.post(WEBHOOK_URL, json=message_card)

if response.status_code == 202:
    print("Message sent successfully!")
else:
    print(f"Error {response.status_code}: {response.text}")