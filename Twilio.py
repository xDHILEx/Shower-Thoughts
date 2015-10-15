#!/bin/env python2.7
""" This script sends the title returned from Reddit.py via text message
"""

import ConfigParser, time
from twilio.rest import TwilioRestClient
import Reddit

config = ConfigParser.ConfigParser()
config.read('Config.ini')

def sendText():
    """ Passes everything to Twilio API to send a text message """
    ACCOUNT_SID = config.get('Twilio', 'ACCOUNT_SID')
    AUTH_TOKEN = config.get('Twilio', 'AUTH_TOKEN')
    CELL_NUMBER = config.get('Twilio', 'CELL_NUMBER')
    # CELL_TO_TEXT is a list
    CELL_TO_TEXT = config.get('Numbers', 'CELL_TO_TEXT').split(',')

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    # grab 'each' cell phone number in list, creates message
    for each in CELL_TO_TEXT:
    	client.messages.create(
    		to = each,
    		from_ = CELL_NUMBER,
            # I'm *pretty sure* that this calls to reddit more than
            # necessary, will fix, but consider it extra randomness ;D
    		body = new_reddit.showerthought()
    	)
        # I'm *hoping* this helps alleviate requests to Twilio,
        # will investigate further.
    	time.sleep(1)

sendText()
