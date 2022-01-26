from datetime import datetime,timedelta
import random
from app.enums.px import Gender

def generate_datetime(start_age=30,end_age=60):
	age = random.randint(start_age,end_age)
	return datetime.now() - timedelta(days=age*365)

def generate_gender():
	return random.choice([Gender.male,Gender.female])