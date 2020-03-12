# NYRR to Gmail calendar event
Take NYRR training emails and create google calendar events

### NYRR Training Programs
New York Roadrunners offers virtual training programs for runners training 
for an upcoming race. Details can be found [HERE](https://www.nyrr.org/train/virtual-training). 
However, the current system does not offer a calendar or a way to add the daily workouts to your calendar. 
This script takes an .eml file received at the beginning, parses it, and creates google calendar events 
based off of it.

### Requirements
This script uses `eml_parser`, `beautiful_soup`, `pickle` and google's calendar API, which can be found [HERE](https://developers.google.com/calendar).

### Environmantal Variables
There is only one ENV VAR, and thats for the google calendar ID. This can simply be "primary" if you want it to be 
placed in you main calendar. Otherwise, add it by inputting:

export GOOGLE_CALENDAR_ID={calendar_id}

### Instructions
Download the email and place the .eml file in the `email_loc` folder and simply run the shell script `./run.sh`. The 
script will take the file, parse it, create events on your calendar, then delete the unneeded eml file.

Example of email: 
![blah](https://raw.githubusercontent.com/cjtamayo/nyrr_email_to_calendar/master/images/nyrr_email_screenshot0.png "original email")


Google calendar events created from email:
![alt text](https://raw.githubusercontent.com/cjtamayo/nyrr_email_to_calendar/master/images/nyrr_email_screenshot1.png "relevant calendar event")





