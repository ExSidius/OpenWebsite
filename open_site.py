#!/usr/bin/python

import webbrowser
import sys

num_args = len(sys.argv);

def open_site(browser, site):

    # Add additional website macros that you would like.
    if (site == "calendar"):
        website = "https://www.google.com/calendar";

    elif (site == "mail"):
        website = "https://www.gmail.com";

    # Default website input.
    else:
        website = "https://www." + site + ".com";

    # For default browser.
    if (browser == "def"):
        webbrowser.open_new(website);

    # For any other browser.
    else:
        webbrowser.get(browser).open_new(website);

    return;

# Check to make sure that user is following required format.
if (num_args >= 3):
    browser = sys.argv[1];

    for i in sys.argv[2:]:
        open_site(browser, i);

# Error message.
else:
    print("\nPlease use format:\npython open_browser_website.py [browser] [website1] [website2]...\n");
