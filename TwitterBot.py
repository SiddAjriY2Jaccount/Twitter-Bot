import tweepy
import requests
from datetime import datetime
import time
import itertools
import functools

CONSUMER_KEY = "********"
CONSUMER_SECRET = "**********"

ACCESS_KEY = "*************"
ACCESS_SECRET = "**************"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)

log = itertools.partial(print, end="\r")


def download_image():
    while True:
        try:
            image = requests.get('https://unsplash.it/1920/1080/?random').content
        except requests.RequestError:
            log("Retrying downloading")
            time.sleep(2 * 60)
        else:
            break
    with open('image.jpg', 'wb') as f:
        f.write(image)
    log("Download done.")


def upload_image(count):
    while True
        try:
            twitter_API.update_with_media("image.jpg", status="Wallpaper #{}".format(count))
        except tweepy.TweepError:
            log("Retrying uploading")
            time.sleep(2 * 60)
        else:
            break
    log("Image #{} uploaded at {:%H:%M}".format(count, datetime.now()))


def delay(hour_delay):
    now = datetime.now()
    new_day = now.day + 1 if now.hour >= 20 else now.day
    new_hour = now.hour + now.hour % hour_delay
    next_post = now.replace(day=new_day, hour=new_hour, minute=0, second=0)
    time.sleep((next_post - now).total_seconds())


for count in itertools.count(1):
    download_image()
    delay(4)
    upload_image(count)
