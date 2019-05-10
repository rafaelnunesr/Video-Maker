import re
import Algorithmia
from Credentials.algorithmia_credential import api_key


def robot(content_user):
    print(f'Recebi com sucesso o content: {content_user}')

def fech_content_from_wikipedia(content_user):
    input = {
        "articleName": content_user,
        "lang": "en"
    }
    client = Algorithmia.client(api_key)
    algo = client.algo('web/WikipediaParser/0.1.2')
    algo.set_options(timeout=300)  # optional
    source_content_complete = (algo.pipe(input).result)
    source_content_original = source_content_complete['content']


    return source_content_original

def __header(content):

    head = content[:content.find('==')]
    return head

def __clean_dates(content):

    open_parentheses = content.find('(')
    close_parentheses = content.find(')') + 1
    new_content = ''.join(content[:open_parentheses]
                          + content[close_parentheses:])
    return new_content

def __remove_doble_spaces(content):

    new_content = content.replace('  ', ' ')
    return new_content


def sanitize_content_from_wikipedia(source_original_str):

    just_head = __header(source_original_str)
    head_cleaned = __clean_dates(just_head)
    no_doble_spaces = __remove_doble_spaces(head_cleaned)
    return no_doble_spaces

def make_sentences(content):

    sentence_endings = re.compile('[.!?]')
    sentences = sentence_endings.split(content)

    temp_sentence = []

    for sentence in sentences:
        temp_sentence.append(sentence.strip())

    sentences = temp_sentence


    return sentences











