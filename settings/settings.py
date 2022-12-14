import json


def read_settings():
    """Get the settings from the settings.json. Return parameters."""

    # With open closes the connection automatically after it is done
    with open("settings/settings.json") as settings:
        website_status_settings = json.load(settings)

    # get the hours between website status checks
    hours_between_status_checks = website_status_settings.get("hours_between_checks")

    # get the websites to be checked
    websites_to_check = website_status_settings.get("websites_to_check")

    return hours_between_status_checks, websites_to_check
