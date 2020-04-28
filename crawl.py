from twython import Twython
import json
from datetime import datetime
import csv
import io

twitter = Twython("x7SMGCVUbA2eJhZfDHQBKXb6x",
    "ZNzVomN6aJfZM3CMsPewobFVvyXcSMcwa6Gys5n2txGeOo7fYl",
    "1229646215010119680-rtAC63ZzBmaV1hWj7ISYiDnHkuRv7b",
    "bjlkqJCIv1Hlf0eklJdgWIlml2GF48kWVNPbhnV6jW008")

twitter_true_ids = [
    1240423992277647361,
]
twitter_false_ids = [
    1239693931140403200,
]
for twitter_id in twitter_true_ids:
    csv_data = []
    data_twitter_trues = twitter.request('https://api.twitter.com/1.1/statuses/retweets/%s.json?count=100'%(twitter_id))
    for dt in data_twitter_trues:
        csv_data.append([dt['user']['id'], dt['id'], dt['text'], dt['created_at']])
        output = open('result/True_%s.csv'%(twitter_id), 'w')
        writer = csv.writer(output, delimiter=',')
        writer.writerows(csv_data)
        output.seek(0)

for twitter_id in twitter_false_ids:
    csv_data = []
    data_twitter_false = twitter.request('https://api.twitter.com/1.1/statuses/retweets/%s.json?count=100'%(twitter_id))
    for dt in data_twitter_false:
        csv_data.append([dt['user']['id'], dt['id'], dt['text'], dt['created_at']])
        output = open('result/False_%s.csv'%(twitter_id), 'w')
        writer = csv.writer(output, delimiter=',')
        writer.writerows(csv_data)
        output.seek(0)