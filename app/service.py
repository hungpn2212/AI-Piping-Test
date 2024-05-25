import openai

from app.settings import MODEL_NAME, OPENAI_API_KEY

client = openai.Client(api_key=OPENAI_API_KEY)


def generate_recommendations(season: str, country: str) -> list[str]:
    response = client.chat.completions.create(
        max_tokens=250,
        messages=[
            {
                'role': 'user',
                'content': f'Recommend me 3 things to do in {country} during {season} season.',
            }
        ],
        model=MODEL_NAME,
    )
    return response.choices[0].message.content.split('\n\n')
