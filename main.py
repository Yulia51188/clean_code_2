from dotenv import load_dotenv
import pygame
import os
import requests
from alive_progress import alive_bar
import time


BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
}
MORSE_ALPHABET = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
    'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
    'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
    'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
    'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '.--.-.', 'ы': '-.--',
    'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', '1': '.----',
    '0': '-----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', ';': '-.-.-.', ':': '---...',
    "'": '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.-', ')': '-.--.-',
    ' ': '|', '_': '..--.-'
}


def establish_connection_to_robot(address):
    response = requests.get(address)
    message = 'Проверка связи с роботом...'
    print(message)
    with alive_bar(len(message), bar='brackets', spinner='radioactive') as bar:
        for _ in range(len(message)):
            time.sleep(0.06)
            bar()
    os.system('cls||clear')
    if response.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')
    print()


def play_symbol_sound(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def play_morze_message(morse_message):
    print()
    with alive_bar(len(morse_message), bar='brackets',
                   spinner='dots_waves2') as bar:
        for symbol in morse_message:
            if symbol == '.':
                play_symbol_sound(pygame.mixer.Sound('dot.ogg'))
            elif symbol == '-':
                play_symbol_sound(pygame.mixer.Sound('dash.ogg'))
            elif symbol == '|':
                play_symbol_sound(pygame.mixer.Sound('long_silence.ogg'))
            bar()
    print()


def encode_message_to_morse(message, morse_alphabet):
    encoded_message = ''
    for letter in message.lower():
        encoded_message += morse_alphabet.get(letter, letter)
    return encoded_message


def send_command_to_robot(address, morse_command):
    print('Отправка сообщения роботу...')
    response = requests.post(address, morse_command.encode('utf-8'))
    if response.status_code == 200:
        print('Команда принята.')
        time.sleep(1)
        print('Бегу к вам!')
    elif response.status_code == 501:
        print('Команда принята. Продолжаю выполнять прежнюю инструкцию.')
    else:
        print('Команда не принята. Не понял вас!')


if __name__ == '__main__':
    load_dotenv()
    pygame.init()
    os.system('cls||clear')
    pygame.mixer.init(BUFFER)
    command = os.getenv('komanda', default='По-умолчанию')
    address = 'http://195.161.68.58'
    morse_command = encode_message_to_morse(command, MORSE_ALPHABET)
    establish_connection_to_robot(address)
    send_command_to_robot(address, morse_command)
    play_morze_message(morse_command)
