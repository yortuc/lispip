import urllib.request, json 

def get_json(url_string):
    print(f'>> get-json {url_string}')
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
        return data

ctx = {
    'get-json': get_json
}
