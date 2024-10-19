import string
import random

def decode_indexed_cipher(text: str, shifts: list) -> str:
    """
    Дешифрует текст, сдвигая каждую букву обратно на соответсвующее количество позиций.
    :param encode_text: Зашфрованная строка текста.
    :param shifts: Список сдвигов для дешифрования.
    :return: Дешифрованный текст
    """
    decode_text = []

    for index, letter in enumerate(text):
        if letter.islower():
            alphabet = string.ascii_lowercase
        elif letter.isupper():
            alphabet = string.ascii_uppercase
        else:
            decode_text.append(letter) # Усли это не буква добавляем символ как есть
            continue # Переходим к следующему символу
        # Находим индекс буквы и применяем  обратный сдвиг
        index_shift = (alphabet.index(letter) - shifts[index]) % len(alphabet)
        decode_text.append(alphabet[index_shift])
    return ''.join(decode_text)

if __name__ == "__main__":
    text = "Yjmt kx uki oixwbhi vs iqetig!"
    dec_msg = decode_indexed_cipher(text, [5, 2, 4, 1, 1, 2, 5, 3, 1, 3, 4, 1, 2, 4, 5, 4, 1, 1, 4, 5, 2, 4, 1, 4, 3, 2, 5, 5, 2, 5])
    print(f"This is decoded message: {dec_msg}")