from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()



client = OpenAI(api_key = os.getenv('API_KEY'))



budget = input('what is your budget: ')

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role" : "system",
            "content" : "In response to the user, we will display a list of about 10-20 guitars that fit within the given budget."
        },
        {
            "role": "user",
            "content": f"Can you recommend me a begginer guitar with a budget of {budget}",
        }
    ],
    model="gpt-4o-mini",
)


print(chat_completion.choices[0].message)
    


