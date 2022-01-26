from enum import Enum


class CCPARequestType(str, Enum):
	delete = "request-to-delete"
	know = "request-to-know"
	optout ="request-to-opt-out"
