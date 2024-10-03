import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_cover_letter_from_openai(vacancy_description=None):
    api_key = os.getenv("API_KEY", "default_token")
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    if vacancy_description is not None:
        payload = {
            "model": "gpt-4-1106-preview",
            "messages": [
                {
                    "role": "system",
                    "content": "Imagine that you are a Senior IT Recruiter. You received such a job description and such specialist skills. Please compose a short text of one paragraph in which you write that I have all the necessary competencies (list them) and can be helpful to the company.",
                },
                {"role": "user", "content": f"{vacancy_description}"},
            ],
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
        )

        if response.status_code != 200:
            print("Ошибка API:", response.status_code)
            print("Содержимое ответа:", response.text)
        else:
            return json.loads(response.text)["choices"][0]["message"]["content"]
