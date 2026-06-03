print("Привет, это мой калькулятор!")
import requests
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()
kurs_rub = data["rates"]["RUB"]
rubles = float(input("Сколько ты хочешь перевести?"))*kurs_rub
print("Итого:", round(rubles), "рублей")
