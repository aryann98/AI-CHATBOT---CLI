import requests as rt
from dotenv import load_dotenv
import os
from colorama import Fore, Style

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

api_url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-3.5-flash-lite:generateContent"
    )
while True:

    user_input = input(
        Fore.RED + Style.BRIGHT + "What you want to ask? "
        + Style.RESET_ALL
    )

    print(
        Fore.GREEN + Style.BRIGHT
        + "👤 You: " + user_input
        + Style.RESET_ALL
    )
    

    header = {
        "x-goog-api-key": api_key
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ]
    }
    try:
        response = rt.post(
        api_url,
        headers=header,
        json=payload,
        timeout=10
        )
    except rt.exceptions.RequestException:
        print(Fore.RED + Style.BRIGHT + "🌐 Internet connection failed!" + Style.RESET_ALL)
        break

    data_in_return = response.json()
    response.raise_for_status()
    

    data_of_candidate = data_in_return["candidates"]
    data_of_content = data_of_candidate[0]

    dict_of_content = data_of_content["content"]
    data_of_parts = dict_of_content["parts"][0]

    end_content = data_of_parts["text"]

    print(
        Fore.WHITE + Style.BRIGHT
        + "🤖 AI:\n"
        + end_content
        + Style.RESET_ALL
    )