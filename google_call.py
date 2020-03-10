from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
from dateutil.parser import parse
from datetime import datetime


need_auth = False
if need_auth:
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
#calendar_list = service.calendarList().list().execute()
#print(calendar_list)
x = 'Tuesday Mar 10'
dt = parse(x)

event = {
  'summary': 'Test calendar UP',
  'location': 'City Hall Park, New York, NY 10007',
  'description': 'Testing this out, son',
  'start': {
    #'dateTime': dt.strftime("%Y-%m-%dT%H:%M:%S"),
    'date': dt.strftime("%Y-%m-%d"),
    'timeZone': 'America/New_York',
  },
  'end': {
    'date': dt.strftime("%Y-%m-%d"),
    'timeZone': 'America/New_York',
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'popup', 'minutes': 10},
    ],
  },
}


event = service.events().insert(calendarId='primary', body=event).execute()