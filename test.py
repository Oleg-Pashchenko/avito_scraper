import json
import dataclasses
import pandas as pd

@dataclasses.dataclass
class Item:
    city_name: str
    car_name: str
    medium_price: int


items = []
cars = ['Chery Tiggo 4', 'Geely Coolray', 'Haval Jolion', 'Москвич 3', 'Chery Tiggo 7',
        'Geely Atlas Pro', 'Haval F7', 'Jac J7', 'FAW Bestune NAT', 'Evolute i-Pro']
for car in cars:
    data = json.load(open(f'{car}.json'))
    for k, v in data.items():
        items.append(
            Item(
                city_name=k,
                car_name=car,
                medium_price=int(sum(v) / len(v))
            )
        )

df = pd.DataFrame([vars(item) for item in items])
df = df.pivot(index='car_name', columns='city_name', values='medium_price')
df.to_excel("items_data.xlsx")