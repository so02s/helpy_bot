from openai import OpenAI


def ask_deepseek(message: str, api_key: str) -> str:

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{
                "role": "user",
                "content": message
            }],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return e

print(ask_deepseek("hello", ""))
