import string
import random

def index_cipher_shifts(text: str) -> tuple:
    """
    Шифрует текст, сдвигая каждую букву на случайное количесвто позиций
    и возвращает зашифрованный текст вместе со списком сдвигов.
    :param text: Строка текста для шифования.
    :return: Кортеж, содержащий зашифрованный текст и список сдвигов.
    """
    # Генерируем случайные сдвиги
    shifts = [random.randint(1, 5) for i in range(len(text))]
    encode_text = []

    for index, letter in enumerate(text):
        if letter.islower():
            alphabet = string.ascii_lowercase
        elif letter.isupper():
            alphabet = string.ascii_uppercase
        else:
            encode_text.append(letter) # Если это не буква , добавляем символ как есть
            continue # Переходим к следующему символу
            # Находим индекс букв и применяем сдвиг
        index_shift = (alphabet.index(letter) + shifts[index]) % len(alphabet) 
        encode_text.append(alphabet[index_shift])
    return ''.join(encode_text), shifts

if __name__ == "__main__":
    text = input("Please insert the message to encode:\n")
    encode_text, shifts = index_cipher_shifts(text)
    print(f"Master key: {shifts}")
    print(f"Encode text: {encode_text}")