import requests
data = {
    "referer":"https://yahoo.com",
    "s1":"",
    "s2":"",
}
url = 'http://localhost:1234/track/create'
headers= {'Content-Type': 'text/plain;charset=UTF-8',
             'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
             'Origin': 'http://localhost:1234',
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
             'Referer': 'http://localhost:1234/'
}
session = requests.session()
d = session.get('http://127.0.0.1:5000/track/create',headers = headers,data = data )
print(d.cookies['hit'])

d = session.get('http://127.0.0.1:5000/track/create',headers = headers,data = data )
print(d.cookies['hit'])