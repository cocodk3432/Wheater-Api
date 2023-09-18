import requests 
import json

Display = '''

⋆⋆  🎀  𝒲𝒽𝑒𝒶𝓉𝒽𝑒𝓇 𝒸𝒽𝑒𝒸𝓀𝑒𝓇  🎀  ⋆⋆

'''
print(Display)
Api_key = ''  # get your api key from https://www.weatherapi.com/
state = input("Enter your state/city: ")
url = 'http://api.weatherapi.com/v1/current.json?key={Api_key}&q={state}&aqi=no'

r = requests.post(url)
data = r.json()


xxx = json.dumps(data)

print(xxx)
