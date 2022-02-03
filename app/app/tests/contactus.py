import requests
from app.models.contact import ContactUs
ContactUsPyDantic= ContactUs.get_pydantic(exclude ={'ip_address':...,'hit':...,'created_date':...,'id':...})
message  = ContactUsPyDantic( email_address = "hamik112@gmail.com",
                   first_name= "Hamik",
                   last_name= "Khan",
                   message= "Hello World").dict()

url = 'http://127.0.0.1:5000/contact/create'
headers= {'Content-Type': 'text/plain;charset=UTF-8','Accept': '*/*','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate','Origin': 'http://localhost:1234',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
          'Referer': 'http://localhost:1234/'
}
session = requests.session()
d = session.post(url,json = message,headers = headers).text
print(d)

