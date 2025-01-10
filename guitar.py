from openai import OpenAI
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)



client = OpenAI(api_key = os.getenv('API_KEY'))

@app.route('/', methods=['GET','POST'])
def index():
    guitars = []

    if request.method == 'POST':
        min_budget = request.form.get('min-budget')
        max_budget = request.form.get('max-budget')
        genre = request.form.get('Genre/Tone')
        shape = request.form.get('shape')


        chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "In response to the user, we will display a list of about 10-20 guitars that fit within the given budget."
                    },
                    {
                        "role": "user",
                        "content": f"Can you recommend me a beginner guitar with a budget range of {min_budget} to {max_budget}, "
                                f"for playing {genre} music, and with a preferred shape of '{shape}'?"
                    }
                ],
                model="gpt-4o-mini",
            )

        guitars = chat_completion.choices[0].message.content.split('\n')


    return render_template('index.html', guitars=guitars)

if __name__ == '__main__':
    app.run(debug=True)
    


