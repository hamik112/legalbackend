
JSON_HEADERS = {'Content-Type': 'application/json'}

BASE_URL="https://api.entitledtojustice.com"
CCPA_URL=f"{BASE_URL}/ccpa/create"
LEAD_URL=f"{BASE_URL}/lead/create"
CONTACTUS_URL=f"{BASE_URL}/ccpa/create"
HIT_URL=f"{BASE_URL}/track/create"

CONTACT_US_PAYLOAD = {"email_address" : "hamik112@gmail.com","first_name" : "Hamik","last_name" : "Khan","message" : "Hello World"}
CCPA_US_PAYLOAD = {"email_address" : "hamik112@gmail.com",
					  "first_name" : "Hamik",
					  "last_name" : "Khan",
					 "phone_number" : "1234567890",
					 "request_type" : "request-to-know"}
