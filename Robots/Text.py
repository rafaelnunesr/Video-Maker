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


    print(source_content_original)
