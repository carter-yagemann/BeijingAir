#!/usr/bin/python

'''
    BeijingAir
    graph.py

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

import sys
import matplotlib.pyplot as plt

#-----------------------------------------------------#
#                  Helper Functions                   #
#-----------------------------------------------------#
def usage():
    print 'Usage: python graph.py <csv_input_data>'

############################################
##                 Main                   ##
############################################
if len(sys.argv) != 2:
    usage()
    sys.exit()

filename = sys.argv[1]

try:
    file = open(filename, 'r')
    y_array = []
    x_array = []

    # Generate array
    while True:
        nextline = file.readline();
        # Have we hit EOF?
        if nextline == '':
            break
        
        # Convert csv to array
        parsedline = nextline.split(', ')
        
        # Exclude averages, No Data, or unexpected lines
        if len(parsedline) < 3:
            continue
        if 'No Data' in parsedline[2]:
            continue
        if '24hr avg' in parsedline[1]:
            continue
            
        # Passed validation, store data point
        y_array.append(parsedline[2])
        x_array.append(parsedline[0])

    file.close()

    # Display graph
    plt.title('Beijing Air Quality\n' + x_array[0] + ' to ' + x_array[-1])
    plt.plot(y_array)
    plt.ylabel('PM2.5')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    fig = plt.gcf()
    fig.canvas.set_window_title('BeijingAir')
    plt.show()
    
except KeyboardInterrupt:
    print "\nCaught keyboard interrupt, exiting."
    sys.exit()
except:
    print "\nUnexpected Exception:", str(sys.exc_info()[1])
    sys.exit()