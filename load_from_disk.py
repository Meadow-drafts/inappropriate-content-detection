import requests
import json

params = {
  'models': 'nudity-2.0,wad,gore',
  'api_user': '237804346',
  'api_secret': 'kWeFeFWok62AaLNhiG22'
}
files = {'media': open('/full/path/to/image.jpg', 'rb')}
r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)

output = json.loads(r.text)