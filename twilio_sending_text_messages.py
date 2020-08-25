from twilio.rest import Client
accountSID = 'AC10d54f2f47ecc376b1e5815926bd8065'
authToken = '7ada697e4d7abaaf96f069c96a6e7552'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+14242275505'
myCellPhone = '+919004958912'
message = twilioCli.messages.create(body='Mr. Love Kush Tak', from_= myTwilioNumber, to= myCellPhone)
print(message)
print(message.body)
print(message.from_)
print(message.to)
'''It may seem odd that the status attribute is set to 'queued'
and the date_sent attribute is set to None when you’ve already received the
text message. This is because you captured the Message object in the message
variable before the text was actually sent. You will need to refetch the Message
object in order to see its most up-to-date status and date_sent.'''
print(message.status)
print(message.date_created)
print(message.date_sent==None)
print(message.sid)
updatedMessage = twilioCLi.messages.get(message.sid)
print(updatedMessage.status)
print(updatedMessage.date_sent)
