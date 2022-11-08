import requests

def transform_c(x):
    return f'{x - 273:.2f}'


api_key = '149a6a6ca97a571a2900e814de8c13db'
city = 'Curitiba'

link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

rq = requests.get(link)
rq_base = rq.json()
desc = rq_base['weather'][0]['description']
temp = rq_base['main']['temp']
temp_min = rq_base['main']['temp_min']
temp_max = rq_base['main']['temp_max']
feels_like = rq_base['main']['feels_like']

print(transform_c(temp))