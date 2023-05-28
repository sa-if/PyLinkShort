import pyshorteners

# prompt the user to enter a list of URLs to shorten
urls = input("Enter a list of URLs to shorten (separated by commas): ").split(",")

# create a pyshorteners.Shortener object
s = pyshorteners.Shortener()


# shorten each URL in the list using the chosen service
short_urls = []
for url in urls:
    
    short_url = s.tinyurl.short(url)
    
    short_urls.append(short_url)

# print the shortened URLs
print("Shortened URLs:")
for short_url in short_urls:
    print(short_url)
