# New Relic integration on Heroku

This document details how to add NewRelic to any Heroku instance.

## Installation

1) Provision the "NewRelic APM" add-on for your Heroku instance. This can be done in the Heroku dashboard under
the Resources tab, or via the command line interface with the command:

    heroku addons:create newrelic:wayne
    
Optional: Add '--app app_name' to specify the instance if it is not your default application for the heroku toolbelt.

Be sure to select the "wayne" tier, which is the free tier of the add-on.

2) Add "newrelic" to your app's requirements.txt.

## Configuration

1) Edit your procfile to use NewRelic to initialize gunicorn. See Procfile template in this directory.

2) Go into the settings tab on Heroku. Replace the setting "NEW_RELIC_LICENSE_KEY" with the AASHE account number.

3) Add a new setting, "NEW_RELIC_APP_NAME", providing a descriptive name of the application. This will be the title
displayed within NewRelic.

Saving these settings will automatically trigger restarting the dyno(s), so there is no need to manually reboot
anything. Simply go to your NewRelic dashboard and you should see the new application in the list.