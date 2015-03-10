BeijingAir
==========

After reading a recent [Wired article](http://www.wired.com/2015/03/opinion-us-embassy-beijing-tweeted-clear-air/)
about the US Embassy in Beijing tweeting air quality metrics, I was inspired to write a quick python
script to collect these metrics. While I was at it, I also threw in a script to generate graphs of the
data.

Installation
------------

This script was tested with Python 2.7.8, so if you're using Python 3.x.x, some modification may
be necessary.

The required libraries for these scripts can be installed using pip:

    $ pip install -r requirements.txt

After installing python and the needed libraries, find the settings section of the script and enter in
your Twitter API keys and file output name.

Execution
---------

When the script is executed, it'll get the latest air quality metric from the BeijingAir
Twitter feed and record it in CSV format, which can then be used in most spreadsheet programs or with
the included graphing script.

When the program runs, it'll only get one data point, so you'll want to configure your system to run the
script on a regular interval using `crontab`, for Linux users, or something equivalent. The feed seems
to update roughly every hour, so you'll want to configure the script to run no more frequently than that.

To generate a quick graph of the collected data, use the included graph script:

    $ python graph.py data.csv