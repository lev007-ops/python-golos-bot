from thefuzz import process

from actions import EXIT, NO_RECOGNIZE
from commands import (close_bot, find_in_internet, greating, open_browser,
                      open_youtube, system_dict)
from listen_say import listen, say

while True:
    query = listen()
    if query == NO_RECOGNIZE:
        print('[INFO] Не могу распознать голос')
    else:
        print(f'[INFO] Распознано: {query}')

        if query.startswith(system_dict['alias']):

            # clear command
            for x in system_dict['alias']:
                query = query.replace(x, '').strip()

            for x in system_dict['tbr']:
                query = query.replace(x, '').strip()

            for k, v in system_dict['commands'].items():

                if process.extractOne(query, v)[1] >= 70:
                    func = globals()[k]()
                    say(func[0])
                    if func[1] == EXIT:
                        exit()
                    break
