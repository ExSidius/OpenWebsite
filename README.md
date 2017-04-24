# OpenWebsite
## A Python Script for Opening Websites from Terminal
### .com Websites. Oh, and you can open macros too.

## The Story

It all began one afternoon when I found myself having to open Facebook.

I don't use Facebook often. 'Tis but a distraction, and I have thus blocked *it*, and many a website, on Google Chrome (my default browser).

And so I found myself taking several seconds extra to open the website. I thought to myself -
> No man should endure this trauma. No man should suffer like this.
> No man will ever have to do this again.

And so, I spent a ~~few seconds~~ *good deal more than a few seconds* programming this script. Thankfully, given my general ineptitude in the world of Python, it was a useful learning experience.

## How Do I Use The Script?
First of all, make sure you have python installed on your computer. If you're running a Mac, it will be installed by default.

Then you must download the file named `open_site.py` and store it in your home directory. Assuming you download to your Downloads folder,
and it is nested within your home directory like any self-respecting Downloads folder would, you can simply run the following command within your terminal.

```
cd
cp ~/Downloads/open_site.py ~/
```

This should move it over to your home directory.

### Now I'm sure the thought has crossed your mind -
> Can't I just drag and drop?

### My response is as follows -
Why yes you can, you silly ass, but if you're on this website, it's clearly to improve your programming skills and turn into an obnoxious master coder. Any master coder with a modicum of self-worth has already abandoned the GUI, since the 50s, 60s, 70s, and 80s (also affectionately referred to as the ***Golden Age of Computer Programming***) didn't possess them, and *why in the world* would one want to make ones' life easier in the slightest, if efficiency was being compromised in the process.

Listen buddy, if you're reading a tutorial about opening websites from a terminal, instead of clicking the little logo at the bottom of your screen and typing a few characters, then clearly you're already too far gone to return to GUIs, so you might as well do **everything** in the Terminal.

# Back to the Actual Guide.

Now, in order to run the script, you must use the following syntax -

`python open_site.py [browser] [website1] [website2]...`

An example of this would be -

`python open_site.py firefox facebook netflix youtube`

Also note that the command for your default browser is `def`, as in -

`python open_site.py def pizzahut`

Another thing you can do to make your life even easier than it already is, is to set up an alias -

`alias site="python open_site.py"`

Now you can type one less word and launch a website by simply saying -

`site def facebook`

Can I get any lazier?

## What else can I do with this marvellous script?
Why, the world is your oyster! Given that this script is open-source, you can manipulate it as you will.

It's not a particularly complicated bit of Python code, and it's fairly clear how you can modify the code to use less inputs, to have more macros (it currently only has `mail` going to GMail, and `calendar` going to Google Calendars).

Enjoy!

## - Mukul Ram
