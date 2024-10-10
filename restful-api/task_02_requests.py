#!/usr/bin/python3
"""send http request and print or save posts."""
import requests
import csv


def fetch_and_print_posts():
    """send a http request and get posts from the url."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print("Title: {}".format(post["title"]))
    else:
        raise ValueError("request not succesful")


def fetch_and_save_posts():
    """send http request and save posts to csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        posts_data = []
        for post in posts:
            posts_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        with open("posts.csv", mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)
        print("Posts saved to posts.csv")

fetch_and_print_posts()
fetch_and_save_posts()