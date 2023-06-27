import requests
import json

print("Cписок питомцев")
status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status=available", headers={'accept': 'application/json'})
print("Статус-код ответа:")
print(res.status_code)
# print(res.text)
print("Данные ответа:")
print(res.json())
print(type(res.json()))


print("Добавление питомца")
new_pit = {"id": 0, "category": {"id": 1, "name": "dog"}, "name": "Pusik", "photoUrls": ["no"],
            "tags": [{"id": 3, "name": "pups"}], "status": "available"}

res = requests.post("https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json',
                                                                   'Content-Type': 'application/json'},
                   data=json.dumps(new_pit, ensure_ascii=False))
print("Статус-код ответа:")
print(res.status_code)
print(res.text)
print("Данные ответа:")
print(res.json())
print(type(res.json()))


id = res.json().get("id")
print(f"ID нового питомца: {id}")


print("Обновление данных")
up_pit = {"id": id, "category": {"id": 1, "name": "cat"}, "name": "Pusik", "photoUrls": ["no"],
               "tags": [{"id": 3, "name": "new pups"}], "status": "available"}
res = requests.put("https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json',
                                                                  'Content-Type': 'application/json'},
                   data=json.dumps(up_pit, ensure_ascii=False))
print("Статус-код ответа:")
print(res.status_code)
print(res.text)
print("Данные ответа:")
print(res.json())
print(type(res.json()))

print(" Удаление питомца")
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{id}", headers={'accept': 'application/json'})
print("Статус-код ответа:")
print(res.status_code)
print(res.text)
print("Данные ответа:")
print(res.json())
print(type(res.json()))

