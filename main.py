from listen import listen
from commands import greating, commands_dict

from thefuzz import process


while True:
    query = listen()

    for k, v in commands_dict['commands'].items():
        if process.extractOne(query, v)[1] >= 50:
            print(globals()[k]())
