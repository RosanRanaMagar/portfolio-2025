from twilio.rest import Client

def sendsms():
    account_sid = 'AC2e001aca9af31cef248d6e51b3b12791'
    auth_token = '4e844366149e084092193b90e5de167a'
    client = Client(account_sid, auth_token)
    
    message = client.messages \
                    .create(
                    body="sucessfully sent...!",
                    from_='+18312499917',
                    to='+9779814578091',
                  )

    print('message sent successfully...!')