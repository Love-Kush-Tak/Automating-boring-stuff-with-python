import json
stringer = '{"name":"Zophie", "isCat":true, "miceCaught":0, "felineIQ":null}'
stringerAsPython = json.loads(stringer)
print(stringerAsPython)
