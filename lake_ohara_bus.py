import requests
from twilio.rest import Client
import time
import datetime

# account_sid, auth_token, & from_num you will get from Twilio. to_num is your cell number.

def send_sms_notification():            
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=to_num, 
            from_=from_num,
            body="Spot open! Book Now!!! https://reservation.pc.gc.ca/Home.aspx"
        )

        print(message.body)



# enter how many hours you want to run requests, refresh time (in minutes) for how often you want to run requests.
# bus date should be yyyy-mm-dd in string format

def check_reservations(hours, refresh_time, bus_date):                      
        minutes = refresh_time * 60
        intervals = int((hours * 60 * 60) / minutes)

        payload = {
                'ddlArrivalMonth': bus_date,
                'ddlArrivalDay': bus_date[5:7]
                }
  
        for interval in range(intervals):
                r = requests.post(r"https://reservation.pc.gc.ca/Yoho-LakeO'Hara?Calendar", data=payload, allow_redirects=False)

                condensed_response = r.text[r.text.find('Availability ('):]

                check1 = 'https://reservation.pc.gc.ca/Images/available_icon20x20.png'
                check2 = 'alt="Unavailable"'
                check3 = 'img title="Available"'

                if check1 in condensed_response or check2 in condensed_response or check3 in condensed_response:
                        print('Available!')
                        send_sms_notification()
                        return
                else: 
                        print('All Booked ' + str(datetime.datetime.now().time()))
                        time.sleep(minutes)
        
                        
#check_reservations(1,2,'2017-09-10') #uncomment, replace arguments to run script
