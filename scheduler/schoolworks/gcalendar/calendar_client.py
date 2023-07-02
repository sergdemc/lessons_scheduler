from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleCalendar:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    CREDENTIALS_FILE = 'schoolworks/gcalendar/project-hb13718-c64384a2a7e7.json'

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            filename=self.CREDENTIALS_FILE, scopes=self.SCOPES
        )
        self.service = build('calendar', 'v3', credentials=credentials)

    def get_calendar_list(self):
        return self.service.calendarList().list().execute()

    def add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }
        return self.service.calendarList().insert(body=calendar_list_entry).execute()

    def add_event(self, calendar_id, event):
        return self.service.events().insert(calendarId=calendar_id, body=event).execute()

    def get_events(self, calendar_id):
        return self.service.events().list(calendarId=calendar_id).execute()

    def update_event(self, calendar_id, event_id, updated_event):
        return self.service.events().update(calendarId=calendar_id, eventId=event_id, body=updated_event).execute()


calendar_obj = GoogleCalendar()
# events = calendar_obj.get_events(GOOGLE_CALENDAR)
# pprint(events)

# event = {
#   'summary': 'Decsription of event',
#   'location': '',
#   'description': 'Test event',
#   'start': {
#     'dateTime': '2023-06-15T10:00:00-07:00',
#     'timeZone': 'UTC',
#   },
#   'end': {
#     'dateTime': '2023-06-15T10:00:00-07:00',
#     'timeZone': 'UTC',
#   },
#   # 'attendees': [
#   {'email': 'hb13718@gmail.com'},
# ],
# 'reminders': {
#   'useDefault': False,
#   'overrides': [
#     {'method': 'email', 'minutes': 24 * 60},
#     {'method': 'popup', 'minutes': 10},
#   ],
# },
# }

# calendar_obj.add_event(GOOGLE_CALENDAR, event)
# calendar_list = calendar_obj.get_calendar_list()
