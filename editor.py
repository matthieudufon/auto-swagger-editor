import json

with open('swagger\openapi.json', 'r') as file:
    data = json.load(file)

with open('templates\headerAuthorization.json', 'r') as auth:
    headerAuthorization = json.load(auth)

for ressource in data["paths"]:
    for verb in data["paths"][ressource]:
        if "parameters" not in data["paths"][ressource][verb]:
            data["paths"][ressource][verb].update({"parameters": []})
        data["paths"][ressource][verb]["parameters"].append(headerAuthorization)

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)