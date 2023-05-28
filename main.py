import pyshorteners

# prompt the user to enter a URL
url = input("Enter a URL to shorten: ")

# create a Shortener object
s = pyshorteners.Shortener()

# shorten the URL
short_url = s.tinyurl.short(url)

# print the shortened URL
print("Shortened URL:", short_url)
