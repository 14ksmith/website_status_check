# Website Status Checker

<p align="center">
  <img alt ="Website Image" src="assets/www.png" width="200">
</p>

## Overview

Website Status Checker is a Python program that allows users to check if all designated websites are up and running correctly. The user can specify however many websites they would like the program to check and requests them asynchronously, allowing for speedy response times. If any websites are not working, the user will be sent an email notification identifying which websites are down.

## How to Use Website Status Checker

### Setup

#### Settings

In order to use Website Status Checker, first download all necessary packages by running `requirements.txt`.

Next, update the settings.json file with the following information. `seconds_between_checks` specifies how many seconds you would like the program to wait before checking website status again. `websites_to_check` contains all of the websites you would like the program to check the status of. And `email_server` tells the program which server you are using to send the email notifications.

Below is an example of the settings.json file:

```json
{
  "seconds_between_checks": 60,
  "websites_to_check": {
    "google": "http://www.google.com",
    "facebook": "http://www.facebook.com",
    "instagram": "http://www.instagram.com"
  },
  "email_server": "smtp.mail.yahoo.com"
}
```

#### Email Notifications

Finally, to set up email notifications, follow the steps below:

1. Add an email address that you want notifications to be sent to if a website is donw. You can add this address as the value for `TO_EMAIL` in the `.env` file.

2. Add the email address that will send notifications. You can add this as the value for `FROM_EMAIL` in the `.env` file. (This can be the same address as the `TO_EMAIL`, if desired).

3. Add the password for the `FROM_EMAIL` by setting the value of `EMAIL_PASSWORD` in the `.env` file.

### Running Website Status Checker

To run the program, run `python3 main.py`. The program will run on a loop and update the user if there are any websites down on a schedule set by the user in `settings.json`. If there are no websites down, no email notification will be sent.
