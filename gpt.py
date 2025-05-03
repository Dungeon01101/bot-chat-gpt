import openai

# Замените на ваш API-ключ OpenAI
openai.api_key = "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"

proxy_host = "13.36.104.85"       # Например, "127.0.0.1"
proxy_port = "80"       # Например, "8080"


# Настройка прокси для OpenAI
openai.proxy = {
    "http": f"http://{proxy_host}:{proxy_port}",
    "https": f"http://{proxy_host}:{proxy_port}",
}

def get_openai_response(prompt):
    """
    Отправляет запрос в OpenAI и получает ответ.

    Args:
        prompt: Текст запроса (сообщения пользователя).

    Returns:
        Текст ответа от OpenAI или None в случае ошибки.
    """
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",  # Выберите подходящую модель (см. ниже)
            prompt=prompt,
            max_tokens=200,  # Максимальная длина ответа (можно настроить)
            n=1,             # Количество ответов (обычно 1)
            stop=None,       # Символы, при которых генерация прекращается (None - нет)
            temperature=0.7,   # "Творческость" ответа (от 0 до 1, можно настраивать)
        )
        return completion.choices[0].text.strip()
    except Exception as e:
        print(f"Ошибка при запросе к OpenAI: {e}")
        return None


if __name__ == "__main__":
    while True:
        user_message = input("Вы: ")  # Получаем сообщение от пользователя
        if user_message.lower() == "exit":
            break

        response = get_openai_response(user_message)

        if response:
            print("ChatGPT: " + response)
        else:
            print("Не удалось получить ответ от OpenAI.")