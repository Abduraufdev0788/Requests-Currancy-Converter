import requests

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

jsonfile = requests.get(url)
datas = jsonfile.json()





class Money :
    def __init__(self, dollar, sum:int):
        self.dollar = dollar
        self.sum = sum
    
    @classmethod
    def UZS(cls,sum):
        for data in datas:
            if data['Ccy'] == "USD":
                result = sum / float(data['Rate'])
                print(f"{result:,.2f} $")

    @classmethod
    def from_Usd(cls,dollar):
        for data in datas:
            if data["Ccy"] == "USD":
                result = dollar * float(data['Rate'])
                print(f"{result:,.2f} so'm")

