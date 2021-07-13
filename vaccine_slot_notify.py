import requests
import datetime
from twilio.rest import Client


def vaccine_notifier():
    district_kasaragod_id = 295
    date = str(datetime.datetime.today().date().strftime("%d-%m-%Y"))

    params = {
        "district_id": district_kasaragod_id,
        "date": date
    }
    vaccine_centres = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",
        params=params)

    message_body = None
    for each in vaccine_centres.json()['centers']:
        for each_centre in each["sessions"]:
            centre_name = each['name']
            availability = each_centre['available_capacity_dose1']
            vaccine_name = each_centre['vaccine']
            age_group = each_centre['min_age_limit']
            date_available = each_centre['date']
            if age_group == 18 and availability > 0:
                message_body += "Vaccine available at " + centre_name + " " +\
                                vaccine_name + "Available "\
                                + str(availability) + " On " + date_available
                print(message_body)

    account_sid = "x"
    auth_token = "x"
    client = Client(account_sid, auth_token)
    print(message_body)
    if message_body:
        message = client.messages.create(
                             body="TEst",
                             from_='+18186166179',
                             to='+918086637696'
                         )

        print(message.sid)


if __name__ == '__main__':
    vaccine_notifier()


