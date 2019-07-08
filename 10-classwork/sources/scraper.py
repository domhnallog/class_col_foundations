import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

response = requests.get("http://www.bbc.com")
doc = BeautifulSoup(response.text, 'html.parser')

stories = doc.find_all(class_='media-list__item')

rows = []
# Grab their headlines and bylines
for story in stories:
    row = {}
    # Grab all of the h2's inside of the story
    headline = story.find(class_='media__link')
    # If a headline exists, then process the rest!
    if headline:
        # They're COVERED in whitespace
        row['headline'] = headline.text.strip()
        # Get the URL
        row['link'] = headline['href']
        try:
            row['summary'] = story.find(class_='media__summary').text.strip()
        except:
            pass

        rows.append(row)

# Create our dataframe
df = pd.DataFrame(rows)
df.to_csv("bbc-data.csv")

# No wait, let's include the time in the filename
datestring = time.strftime("%Y-%m-%d-%H-%M")
filename = f"bbc-data-{datestring}.csv"

# Save it
df.to_csv(filename, index=False)
