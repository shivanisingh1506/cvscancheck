mport
urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json

data = {

    "Inputs": {

        "input1":
            {
                "ColumnNames": ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
                                "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
                                "hours-per-week", "native-country"],
                "Values": [["0", "value", "0", "value", "0", "value", "value", "value", "value", "value", "0", "0", "0",
                            "value"],
                           ["0", "value", "0", "value", "0", "value", "value", "value", "value", "value", "0", "0", "0",
                            "value"], ]
            }, },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/e0b033d1d5784a24803a211855379793/services/5c83569cfe5244388e2ea7c37c040d9f/execute?api-version=2.0&details=true'
api_key = 'abc123'  # Replace this with the API key for the web service
headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
R
library("RCurl")
library("rjson")

# Accept SSL certificates issued by public Certificate Authorities
options(RCurlOptions=list(cainfo=system.file("CurlSSL", "cacert.pem", package="RCurl")))

h = basicTextGatherer()
hdr = basicHeaderGatherer()

req = list(

    Inputs=list(

        "input1" = list(
    "ColumnNames" = list("age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
                         "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week",
                         "native-country"),
                    "Values" = list(
    list("0", "value", "0", "value", "0", "value", "value", "value", "value", "value", "0", "0", "0", "value"),
    list("0", "value", "0", "value", "0", "value", "value", "value", "value", "value", "0", "0", "0", "value"))
)                ),
GlobalParameters = setNames(fromJSON('{}'), character(0))
)

body = enc2utf8(toJSON(req))
api_key = "abc123"  # Replace this with the API key for the web service
authz_hdr = paste('Bearer', api_key, sep=' ')

h$reset()
curlPerform(
    url="https://ussouthcentral.services.azureml.net/workspaces/e0b033d1d5784a24803a211855379793/services/5c83569cfe5244388e2ea7c37c040d9f/execute?api-version=2.0&details=true",
    httpheader=c('Content-Type' = "application/json", 'Authorization' = authz_hdr),
postfields = body,
