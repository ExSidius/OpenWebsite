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

    elif  (site == "elms"):
        website = "https://elms.umd.edu";


    elif (site == "habitica"):
    	website = "https://www.habitica.com";

    # Default website input.
    else:
        website = "https://www." + site + ".com";

    # For default browser.
    if (browser == "def"):
        webbrowser.open(website, new=2, autoraise=True);

    # For any other browser.
    else:
        webbrowser.get(browser).open(website, new=2, autoraise=True);

    return;

# Check to make sure that user is following required format.
if (num_args >= 3):
    browser = sys.argv[1];

    for i in sys.argv[2:]:
        open_site(browser, i);

# Error message.
else:
    print("\n\nPlease use format:\npython open_browser_website.py [browser] [website1]" +
    "[website2]...\n\nOr if you have alias \"site\" set up:\nsite [browser] [website1] [website2]...\n\n");
