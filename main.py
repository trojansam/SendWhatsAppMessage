import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)
# client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'

# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+14155238887'


url = 'https://pebc.ca/online_applications/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.select_one("#content > section > div > div > div.right-sidebar > section > div > div:nth-child(1) > h5")
text = results.get_text()
text = text.lower()

print(text)

if "unavailable" in text:
    print("NO")
    client.messages.create(body='❌ Pebc portal is not available!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
else:
    print("YES")
    client.messages.create(body='🎉 Pebc portal is available!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)











