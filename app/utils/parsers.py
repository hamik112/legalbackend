from httpx import Response
from app.models.lead import Lead
from app.core.config import config
from app.enums.px import Gender,EntranceExists,Ownership,SquareFootage,ProInstallation,SecurityType,SecurityUsage,InstallationTimeFrame,HasSystem

def generate_pingpost_request(url: str, method: str, headers: dict, payload: str, vendor: str):
	return {
		'url'    : url,
		'method' : method,
		'headers': headers,
		'payload': payload,
		'vendor' : vendor,
	}


def generate_pingpost_response_json(vendor: str, response: Response):
	return {
		'response': response.text,
		'vendor'  : vendor
	}

def ping(lead: Lead):
	payload = {
		"ApiToken"     : config.PX_API_TOKEN,
		"Vertical"     : "HomeSecurity",
		"SubId"        : config.PX_SUB_ID,
		"OriginalUrl"  : lead.original_url,
		"Source"       : config.PX_SOURCE,
		"JornayaLeadId":  lead.universal_leadid,
		"SessionLength": lead.session_length,
		"TcpaText"     :lead.tcpa_text,
		"VerifyAddress": False,
		"ContactData"  : {
			"State"    : lead.state,
			"ZipCode"  : lead.zip_code,
			"IpAddress": lead.hit.ip_address
		},
		"Person"       : {
			"BirthDate": lead.dob,
			"Gender"   : lead.gender
		},
		"Home"         : {
			"Ownership"                   : lead.ownership,
			"EntrancesExits"              : lead.entrances_exits,
			"HasSystem"                   : lead.has_system,
			"CurrentSecuritySystemCompany": lead.,
			"SqFootage"                   : lead.square_footage,
			"SecuritySystem"              : {
				"ProInstall"            : lead.pro_install,
				"SecurityType"          :lead.security_usage,
				"SecurityUsage"         : lead.security_usage,
				"InstallationType"      : lead.pro_install,
				"InstallationTimeFrame" : lead.installation_time_frame,
			}
		}
	}

def post(transaction_id : str , lead: Lead):
	payload = {
		"ApiToken"     : config.PX_API_TOKEN,
		"Vertical"     : "HomeSecurity",
		"SubId"        : config.PX_SUB_ID,
		"OriginalUrl"  : lead.original_url,
		"Source"       : config.PX_SOURCE,
		"JornayaLeadId":  lead.universal_leadid,
		"SessionLength": lead.session_length,
		"TcpaText"     :lead.tcpa_text,
		"VerifyAddress": False,
		"ContactData"  : {
			"FirstName"     : lead.first_name,
			"LastName"      : lead.last_name,
			"Address"       : lead.street_address,
			"City"          : lead.city,
			"State"         : lead.state,
			"ZipCode"       :lead.zip_code,
			"EmailAddress"  : lead.email,
			"PhoneNumber"   : lead.phone_number,
			"DayPhoneNumber": lead.phone_number,
			"IpAddress"     : lead.hit.ip_address
		},
		"Person"       : {
			"BirthDate": lead.dob,
			"Gender"   : lead.gender,
		},
		"Home"         :
			{
				"Ownership"                   : lead.ownership,
				"EntrancesExits"              : lead.entrances_exits,
				"HasSystem"                   : lead.has_system,
				"SqFootage"                   : lead.square_footage,
				"SecuritySystem"              : {
					"ProInstall"            : lead.pro_install,
			"SecurityType"          : lead.security_type,
			"SecurityUsage"         : lead.security_usage,
			"InstallationType"      : lead.installation_time_frame,
			"InstallationTimeFrame" : lead.installation_time_frame,
		}
	}
	}


# url = "https://leadapi.px.com/api/lead/ping"
# post_url = "https://leadapi.px.com/api/lead/post"


post = {
	"ApiToken"     : config.PX_API_TOKEN,
	"Vertical"     : "HomeSecurity",
	"SubId"        : config.PX_SUB_ID,
	"OriginalUrl"  : lead.original_url,
	"Source"       : config.PX_SOURCE,
	"JornayaLeadId":  lead.universal_leadid,
	"SessionLength": "38",
	"TcpaText"     : lead.tcpa_text,
	"VerifyAddress": False,
	"TransactionId": "CB9C6CB6-2BB2-4E31-ADA9-0C527BDAA0E7",
	"ContactData"  : {
		"FirstName"     : "John",
		"LastName"      : "Doe",
		"Address"       : "1 Little West 12th",
		"City"          : "New York",
		"State"         : "AL",
		"ZipCode"       : "10014",
		"CompanyName"   : "string",
		"EmailAddress"  : "testlead@somedomain.com",
		"PhoneNumber"   : "6467171795",
		"DayPhoneNumber": "6467171795",
		"IpAddress"     : "255.255.255.255"
	},
	"Person"       : {
		"BirthDate": "1980-07-27",
		"Gender"   : "Male"
	},

	"Home"         : {
		"Ownership"                   : "Own",
		"EntrancesExits"              : "1",
		"HasSystem"                   : "No",
		"CurrentSecuritySystemCompany": "Other",
		"SqFootage"                   : "Less than 1,000",
		"SecuritySystem"              : {
			"ProInstall"            : "Yes",
			"PreWired"              : "Yes",
			"SecurityType"          : "Only burglar/intrusion",
			"SecurityUsage"         : "Residental",
			"InstallationType"      : "No Preference",
			"InstallationTimeFrame" : "Immediately",
			"InterestReason"        : "Peace of mind",
			"AdditionalRequirements": "string"
		}
	}
}
