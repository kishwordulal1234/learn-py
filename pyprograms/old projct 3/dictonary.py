info = {
    "name": "kishwor",
    "age": 16,
    "religion": "hindhu",
    "home town": "sindhupalchol"
}

print(info.get("name"))
print(info["name"])

info["name"] = "rahul"

print(info)
print(info.values())
print(info.keys())
print(info.items())
info.update({"city":"pplit"})

kkl = {"bbl":"ccl"}
info.update(kkl)
print(info)