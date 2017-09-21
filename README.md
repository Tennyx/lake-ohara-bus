# The Bus to Lake O'hara
Get notified via text when a seat opens up on the bus to [Lake O'Hara, BC](https://www.hikebiketravel.com/wp-content/uploads/2013/07/Lake-OHara-087-copy.jpg). The bus to this beautiful place is notoriously full, and it happens quickly - if you're like me you will want to know if someone cancels immediately. This script will check for you at whatever frequency (be nice) you desire and sends you a text if it happens. You must be signed up on [Twilio](https://www.twilio.com/) for the latter. Free trial account should be all you need.   

### What You Need

* [python 3](https://www.python.org/download/releases/3.0/)
* [pip](https://pip.pypa.io/en/stable/installing/) - To install dependencies
* [requests](http://docs.python-requests.org/en/master/)
* [twilio](https://www.twilio.com/)

### Installing

After python 3 is installed, follow the instructions on pip link to install pip. Then to install requests and twilio type the following in the terminal:

```
pip3 install requests
```
```
pip3 install twilio
```

## Next Steps
Sign up for [Twilio](https://www.twilio.com/). For this small script a free trial will work just fine. Once you sign up you will receive:
* Account SID
* Authorization Token
* Twilio Number

These three things will allow you to send the text notification to yourself. In the script you will replace the following in the corresponding order above:
* account_sid
* auth_token
* from_num
* additionally, fill in to_num with whatever cellphone  # you want the notification sent to

here are the corresponding lines of code in the *send_sms_notification* function:

```python
client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=to_num, 
            from_=from_num,
            body="Spot open! Book Now!!! https://reservation.pc.gc.ca/Home.aspx"
        )
``` 
Now to move onto the main function *check_reservations*. All you have left to do is set your:
* Time the script runs in **hours**
* How frequently you want it to send requests (in minutes) to the site in **refresh_time**
* Date range in **bus_date**. Enter date as string in yyyy-mm-dd format. It will return that day and the 15 days after.

If any of these days open up as available, the *send_sms_notification* will fire and send you a link to make a reservation.

## Authors

[Cale Switzer](http://www.caleswitzer.com)

The mountains are calling, and you must go!

![Lake O'hara](https://www.hikebiketravel.com/wp-content/uploads/2013/07/Lake-OHara-087-copy.jpg)

###### Photo credit: Leigh McAdam
