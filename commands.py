import webbrowser

from random import choice

from actions import EXIT, NO_RECOGNIZE
from listen_say import listen, say

system_dict = {
    'commands': {
        'greating': ('привет', 'хай', 'здравствуйте'),
        'close_bot': ('пока', 'до свидания', 'ещё увидимся'),
        'open_browser': ('браузер', 'интеренет'),
        'open_youtube': ('ютуб', 'youtube'),
        'find_in_internet': ('найди', 'поищи')
    },
    'alias': ('олег', 'олегушка', 'олежа', 'олегушка'),
    'tbr': ('скажи',  'покажи', 'расскажи', 'сколько', 'произнеси', 'открой')
}

answers_dict = {
    'greating': (
        'привет друг', 'здравствуй', 'здравствуйте', 'приветствую',
        'приветствую вас', 'хай друг', 'привет, давно не виделись'
    ),
    'close_bot': (
        'пока', 'пока друг!', 'до свидания', 'ещё увидимся'
    ),
    'open_browser': (
        'открываю браузер', 'даю доступ в интернет'
    ),
}


def greating():
    """Greating func"""

    return (choice(answers_dict['greating']), None)


def close_bot():
    return (choice(answers_dict['close_bot']), EXIT)


def open_browser():
    webbrowser.open('https://www.google.com/')
    return (choice(answers_dict['open_browser']), None)


def open_youtube():
    webbrowser.open('https://www.youtube.com/')
    return ('Открываю ютуб', None)


def find_in_internet():
    say('Что вы хотите найти')
    search = listen()
    if search == NO_RECOGNIZE:
        return ('Не смог распознать ваш запрос', None)

    webbrowser.open(search)
    return ('Ищу информацию в интернете по запросу ' + search, None)
