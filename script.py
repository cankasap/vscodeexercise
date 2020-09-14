import requests

r = requests.get("http://www.cyclonemfg.com/")

print(r.status_code)
print(r.ok)
