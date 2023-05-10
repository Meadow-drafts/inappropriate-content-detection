import requests
import json

params = {
  'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQhrc30veQ9H7Y0T3duaHzgjI0vHhAl2fcbA&usqp=CAU',
  'models': 'nudity-2.0,gore, wad,offensive,tobacco',
  'api_user': '98565146',
  'api_secret': 'PXmk485MeyrpP4w6jUdL'
}
r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)

output = json.loads(r.text)


nudityData = output["nudity"]
weaponsData = output["weapon"]
drugsData = output["drugs"]
medicsData = output["medical_drugs"]
offensiveData = output['offensive']['prob']
tobaccoData = output["tobacco"]["prob"]


accuracyProbability = {
    "Nudity Results":nudityData,
    "Weapon Results":weaponsData,
    "Drugs Results":drugsData,
    "Medical Drugs Results":medicsData,
    "Offensive Results":offensiveData,
    "Tobacco Results":tobaccoData

}

for key, val in accuracyProbability.items():
    print(f'{key}:{val}')






    # drugs
    # "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQhrc30veQ9H7Y0T3duaHzgjI0vHhAl2fcbA&usqp=CAU
 
    # nudity simple
    # "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzT1GAl2962RPP4A27C8er2DB0cBUJt1f2aA&usqp=CAU"
    # weaponsData
    #     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFMRvGO5VaqzjKlq1HE8Y3_8aCN3u3Rj_npA&usqp=CAU"
    # tobacco
    # "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnbS5qNp3-_AwudwsSs1rv86YGp8wPc96qGA&usqp=CAU"
  
    # nudity bikini
    # "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQXkvTeG4gTIoLEPnxBAzn_wTC-X6yyKB9Bg&usqp=CAU"
    # proper
    # https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBnwi8GXUbys5WQa9KDZLpZ4AhcKeo39GyVw&usqp=CAU