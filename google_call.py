from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
from dateutil.parser import parse


def authentication_store():
    """
    IF creds are needed, this will grab it and store it via pickle
    :param need_auth:
    :return:
    """
    print("Getting authentication")
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
    credentials = flow.run_local_server(port=0)
    pickle.dump(credentials, open("token.pkl", "wb"))

    return


def distance_clean(distance):
    """
    This part seems to have some issues with spacing. Lets fix that
    :param distance:
    :return: cleaned distance! (string)
    """
    distance = distance.replace("(", " (")
    distance = distance.replace("miles", "miles ")
    distance = distance.replace("off", "off ")
    distance = distance.replace("Warmdown", "Warmdown ")
    distance = distance.replace("Warmup", "Warmup ")
    distance = distance.replace("Fartlek", "Fartlek ")
    distance = distance.replace("  ", " ")

    return distance


def event_creator(day, workout, distance, description):
    """
    Taking the details from the email, then creating the event
    :param day:
    :param workout:
    :param distance:
    :param description:
    :return:
    """
    print("Building {}".format(day))
    credentials = pickle.load(open("token.pkl", "rb"))
    try:
        service = build("calendar", "v3", credentials=credentials)
    except:
        print("credentials error, trying re-authentication")
        authentication_store()
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)

    date_event = parse(day)

    if "miles" in distance:
        end = distance.find("miles")
        summary = '{}- {}'.format(workout, distance[:end+5])
    else:
        summary = workout

    if distance == "place_hold":
        full_descrip = description
    else:
        full_descrip = '{}\n\n{}'.format(distance_clean(distance), description)


    event = {
      'summary': summary,
      'location': os.getenv('CALENDAR_LOCATION','New York, NY 10019'),
      'description': full_descrip,
      'start': {
        'date': date_event.strftime("%Y-%m-%d"),
        'timeZone': os.getenv('CALENDAR_TIME_ZONE','America/New_York'),
      },
      'end': {
        'date': date_event.strftime("%Y-%m-%d"),
        'timeZone': os.getenv('CALENDAR_TIME_ZONE','America/New_York'),
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 60},
        ],
      },
    }


    event = service.events().insert(calendarId=os.getenv('GOOGLE_CALENDAR_ID', 'primary'), body=event).execute()
    

    print('created event for {}'.format(day))

    return