from requests import get

script = get("https://raw.githubusercontent.com/Sutanshu/404Labs/master/requestsVersion.py")
print(script.text)
