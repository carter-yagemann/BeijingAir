#!/usr/bin/python

'''
    BeijingAir
    fetch_datapoint.py

    Copyright Carter Yagemann 2015

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import twitter
import sys

############################################
##               Settings                 ##
############################################
consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

data_filename       = 'data.csv'

#-----------------------------------------------------#
#                  Helper Functions                   #
#-----------------------------------------------------#
def connect(consumer_key, consumer_secret,
            access_token, access_token_secret):
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
    
    # Verify tokens
    result = api.VerifyCredentials()
    if result == None:
        raise InvalidTokens()
        return None
    
    return api
    
#-----------------------------------------------------#
#                    Exceptions                       #
#-----------------------------------------------------#
class InvalidTokens(Exception):
    def __init__(self):
        self.value = 1
    def __str__(self):
        return "Could not validate tokens."

############################################
##                 Main                   ##
############################################
try:
    # Connect to Twitter
    sys.stdout.write("Connecting to twitter... ")
    api = connect(consumer_key, consumer_secret,
                  access_token, access_token_secret)
    sys.stdout.write("Done.\n")
    
    # Get latest Beijing air quality metrics from US embassy's twitter
    latest_status = api.GetUserTimeline(screen_name='BeijingAir')[0].text
    parsed_status = latest_status.split('; ')

    # Open file for storing data points    
    file = open(data_filename, "a")

    # Store data point
    for element in parsed_status[:-1]:
        file.write(element + ', ')
    file.write(parsed_status[-1] + '\n')
    
    file.close()
    
except InvalidTokens as e:
    print "\nInvalidTokens:", e
    sys.exit()
except KeyboardInterrupt:
    print "\nCaught keyboard interrupt, exiting."
    sys.exit()
except:
    print "\nUnexpected Exception:", str(sys.exc_info()[1])
    sys.exit()
