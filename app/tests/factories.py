from dataclasses import dataclass


@dataclass
class Content:
    content: str


@dataclass
class Message:
    message: Content


@dataclass
class OpenAIResponse:
    choices: list[Message]


DEFAULT_RECOMMENDATIONS = ['Visit the beach',
                           'Visit the mountains', 'Visit the forest']


def create_fake_openai_response(
    items: list[str] = DEFAULT_RECOMMENDATIONS,
):
    return OpenAIResponse(choices=[Message(message=Content(content='\n\n'.join(items)))])
