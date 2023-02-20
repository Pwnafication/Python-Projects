from bs4 import BeautifulSoup
import requests
import smtplib

response = requests.get(url="https://news.ycombinator.com/")
hackernews_wp = response.text
soup = BeautifulSoup(hackernews_wp, "html.parser")

article_text = []
article_links = []
article_votes = []

articles = soup.select(".titleline a")

for each in articles:
    article_text.append(each.getText())
    article_links.append(each.get("href"))

article_votes = [int(each_score.getText().split()[0]) for each_score in soup.find_all(name="span", class_="score")]

largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)

best_article_text = article_text[largest_index]
best_article_links = article_links[largest_index]

print(article_text[largest_index])
print(article_links[largest_index])

from bs4 import BeautifulSoup
import requests
import smtplib

response = requests.get(url="https://news.ycombinator.com/")
hackernews_wp = response.text
soup = BeautifulSoup(hackernews_wp, "html.parser")

article_text = []
article_links = []
article_votes = []

articles = soup.select(".titleline a")

for each in articles:
    article_text.append(each.getText())
    article_links.append(each.get("href"))

article_votes = [int(each_score.getText().split()[0]) for each_score in soup.find_all(name="span", class_="score")]

largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)

best_article_text = article_text[largest_index]
best_article_links = article_links[largest_index]

print(article_text[largest_index])
print(article_links[largest_index])

python_app_password = "XXXX"
my_email = "@"
my_password = python_app_password
email_list = ["@", "@", "@"]

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    for each in email_list:
        connection.sendmail(
            to_addrs=each,
            from_addr=my_email,
            msg=f"Subject: Hot Topic scraped from HackerNews! {best_article_text}\n\nCheck out the link!: {best_article_links}."
        )
