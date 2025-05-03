import openai

# Замените на ваши значения
openai.api_key = "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"
proxy_host = "13.38.176.104"       # Например, "127.0.0.1"
proxy_port = "3128"       # Например, "8080"


# Настройка прокси для OpenAI
openai.proxy = {
    "http": f"http://{proxy_host}:{proxy_port}",
    "https": f"https://{proxy_host}:{proxy_port}",
}


def get_openai_response(prompt):
    try:
        completion = openai.Completion.create(
            engine="gpt-4o",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return completion.choices[0].text.strip()
    except Exception as e:
        print(f"Ошибка при запросе к OpenAI: {e}")
        return None


if __name__ == "__main__":
    user_message = input("Вы: ")
    response = get_openai_response(user_message)
    if response:
        print("Chat: " + response)