from twilio.rest import Client
accountSID = 'AC10d54f2f47ecc376b1e5815926bd8065'
authToken ='7ada697e4d7abaaf96f069c96a6e7552'
myNumber ='+14242275505'
twilioNumber = '+919004958912'
def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
