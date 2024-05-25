import openai
from app.settings import Settings


def generate_recommendations(season: str, country: str) -> list[str]:
    client = openai.Client(api_key=Settings().model_dump()['OPENAI_API_KEY'])
    response = client.chat.completions.create(
        max_tokens=250,
        messages=[
        {
            "role": "user",
            "content": f'Recommend me 3 things to do in {country} during {season} season.',
        }
    ],
    model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content.split('\n\n')

