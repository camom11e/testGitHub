import random
import time

greetings = [
    "Привет, GitHub!",
    "Здравствуй, GitHub!",
    "Приветствую, GitHub!",
    "Приветики, GitHub!",
    "Как дела, GitHub!",
]

message_parts = [
    "Инициализация соединения...",
    "Доступ к GitHub...",
    "Получение приветствия...",
    "Успешное подключение!",
]

for part in message_parts:
    print(part)
    time.sleep(1)

message = random.choice(greetings)
for char in message:
    print(char, end="", flush=True)
    time.sleep(0.1)
print()

print("Добро пожаловать на GitHub!")
