import Algorithmia
from Credentials.algorithmia_credential import api_key



def robot(content):
    print(f'Recebi com sucesso o content: {content}')

def fechContentFromWikipedia(content):
    input = {
        "articleName": content,
        "lang": "en"
    }
    client = Algorithmia.client(api_key)
    algo = client.algo('web/WikipediaParser/0.1.2')
    algo.set_options(timeout=300)  # optional
    # print(algo.pipe(input).result)
    sourceContentOriginal = (algo.pipe(input).result)
