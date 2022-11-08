import requests
from tkinter import *

def transform_c(x):
    return f'{x - 273.15:.2f}'

#Making a window
window = Tk()
window.geometry('500x200')
window.title('Weather APP')
window.configure(background='#dde')

text = Label(window, text='Insert your city!')
text.place(x=210, y=30)

entry = Entry(window, width=60)
entry.place(x=75,y=60)


window.mainloop()

#API Parameters
api_key = '149a6a6ca97a571a2900e814de8c13db'
city = entry.get()
lang = 'pt_br'

#API Connection
link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}'
rq = requests.get(link)
rq_base = rq.json()

#Weather information
desc = rq_base['weather'][0]['description']
temp = transform_c(rq_base['main']['temp'])
temp_min = transform_c(rq_base['main']['temp_min'])
temp_max = transform_c(rq_base['main']['temp_max'])
feels_like = transform_c(rq_base['main']['feels_like'])



print(desc)