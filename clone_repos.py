"""
Clone all public GitHub repositories of given username
"""

import os

import git
import requests

USERNAME = input("Enter username: ")
DIR_TO_CLONE_TO = os.path.abspath(input("Directory to clone dirs to(relative): "))

repo_urls = map(lambda x: (x.get('name'), 
                           "git@github.com:{}/{}".format(USERNAME, x.get('name'))), 
                 requests.get('https://api.github.com/users/{}/repos'
                              ''.format(USERNAME)).json())

for name, url in repo_urls:
    print("Cloning " + url)
    git.Repo.clone_from(url, os.path.join(DIR_TO_CLONE_TO, name))
