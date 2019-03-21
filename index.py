from Robots.Text import robot, fech_content_from_wikipedia

def start():

    def ask_and_return_seach_term():
        return input('Type a Wikipedia term: ')

    def ask_and_return_prefix():
        prefixes = ['Who is', 'What is', 'The History of']

        for i, p in enumerate(prefixes):
            print(f'[{i+1}] -> {p}')

        ask_prefix = int(input('Choose one option:'))

        try:
            return prefixes[ask_prefix-1]

        except IndexError:
            return 'Invalid option'



    search_term = ask_and_return_seach_term()
    prefix_term = ask_and_return_prefix()
    robot(search_term)
    fech_content_from_wikipedia(search_term)

start()
