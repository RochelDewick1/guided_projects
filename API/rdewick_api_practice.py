import requests
from pandas import json_normalize
import json
def ocr_space_file(filename, overlay=False, api_key='K81283206488957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          verify=False,
                          )
    return r.content.decode()

test_file = ocr_space_file(filename='life_is_short.jpg')
result = json.loads(test_file)
df = json_normalize(result['ParsedResults'])
text = df['ParsedText'].str.replace('\r', '').str.replace('\n', ' ')
print(text[0])