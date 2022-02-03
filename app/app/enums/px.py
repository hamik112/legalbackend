

from enum import Enum


class YesNo(str, Enum):
    yes = "Yes"
    no = "No"

class Education(str,Enum):
    bachelors = "Bachelors Degree"
    masters = "Masters Degree"
    some_college = "Some College"

class Gender(str,Enum):
    male='Male'
    female = 'Female'
    non_binary = 'Non-Binary'

class Condition(str,Enum):
    alzheimer ='Alzheimer'
    cancer ='Cancer'
    diabetes = 'Diabetes'
    heartdisease='HeartDisease'
    kidneydisease='KidneyDisease'
    livedisease='LiverDisease'
    stroke='Stroke'
    noneofabove ='noneofabove'

class HouseHoldSize(str,Enum):
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven ='7'
    eight = '8'
    nine = '9'
    ten = '10'

class HouseHoldIncome(str,Enum):
    twenty_thousand = '20000'
    thirty_thousand = '30000'
    fourty_thousand = '40000'
    fifty_thousand = '50000'
    sixty_thousand = '60000'
    seventy_thousand = '70000'
    eighty_thousand = '80000'
    ninety_thousand = '90000'
    hundred_thousand = '100000'
    hundred_twenty_five_thousand = '125000'
    one_hundred_fifty_thousand = '150,000'
    two_hundred_thousand = '200000'
    two_hundred_fifty_thousand = '250,000'




class UnsoldReason(str,Enum):
    ping_error = 'Error on Ping'
    post_error = 'Error on Post'
    unknown_error = 'Unknown'
    no_state_coverage='Non-Eligable State'
    no_buyers = 'No Buyer'

class HasSystem(str,Enum):
    Yes = 'Yes'
    No = 'No'

class Ownership(str,Enum):
    Own="Own"
    Rented="Rented"


class InstallationTimeFrame(str,Enum):
    Immediately= "Immediately"
    OneMonth = "In one month"
    TwoMonths  = "In two months"
    MoreThanTwoMonths = "More than two months"

class SecurityUsage(str,Enum):
    Residential = "Residential"
    Business = "Business"

class SecurityType(str,Enum):
    OnlyBurglar = "Only burglar/intrusion"
    OnlyFireDetection = "Only fire detection"
    BurglarAndFireDetection = "Both burglar and fire detection"

class ProInstallation(str,Enum):
    Yes = "Yes"
    No = "No, i will install myself"
    NotSure = "Not sure"

class SquareFootage(str,Enum):
    LessThanThousand = "less than 1000"
    OneThousandToTwoThousandFiveHundred ="1001 to 2500"
    TwoThousandFiveHundredToFiveThousand = "2501 to 5000"
    FiveThousandPlus = "5000+"

class EntranceExists(str,Enum):
    One = "1"
    Two ="2 to 4"
    Five ="5"
    MoreThanFive="5+"


