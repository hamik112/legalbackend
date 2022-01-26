import requests
data = {
	"city": "La Crescenta",
	"email": "hamik112gmail.com",
	"first_name": "hamik",
	"installation": "selfinstall",
	"last_name": "akhverdyan",
	"phone_number": "8187263197",
	"propertytype": "rental",
	"servicetype": "reactivateexisting",
	"session_length": 22,
    "state": "CA",
    "street_address": "2505 Foothill Blvd",
    "tcpa_text": "By clicking Get My  Security Quotes, I agree to the Terms of Service and  Privacy  Policy and  and provide consent to receive  pre-recorde…",
    "universal_leadid": "0045FFBF-6D80-82FF-7A3B-63D53F43BBBE",
    "zip_code": "91214"
}
headers= {'Content-Type': 'text/plain;charset=UTF-8',
             'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
             'Origin': 'http://localhost:1234',
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
             'Referer': 'http://localhost:1234/'
}

d = requests.post('http://127.0.0.1:5000/lead/create',headers = headers,json = data ).json()
print(d)