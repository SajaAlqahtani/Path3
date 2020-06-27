import requests
response = requests.get("https://www.python.org/")
print(response.text)
file = open("url Data.txt","w")
file.write(response.text)
file.close()