import requests
import json
import pytest

def import_gists_to_database(db, username, commit=True):
    resp = requests.get('https://api.github.com/users/{}/gists'.format(username))
    if resp.status_code==404:
        raise requests.HTTPError(resp.text)
    resp_data=resp.json()
    n=0
    for i in resp_data:
        dt_id= resp_data[n]["id"]
        dt_url= resp_data[n]["html_url"]
        dt_pllurl=resp_data[n]["git_pull_url"] 
        dt_pshurl=resp_data[n]["git_push_url"] 
        dt_commit =resp_data[n]["commits_url"] 
        dt_frkurl=resp_data[n]["forks_url"]
        dt_public=resp_data[n]["public"]
        dt_create=resp_data[n]["created_at"]
        dt_update=resp_data[n]["updated_at"]
        dt_comment=resp_data[n]["comments"]
        dt_cmturl=resp_data[n]["comments_url"]
        if commit:
            query= "INSERT INTO gists(github_id, html_url,git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments,comments_url) VALUES (:dt_id,:dt_url,:dt_pllurl,:dt_pshurl,:dt_commit,:dt_frkurl,:dt_public,:dt_create,:dt_update,:dt_comment,:cmturl)"
            db.execute(query,{'dt_id':dt_id,'dt_url':dt_url,'dt_pllurl':dt_pllurl,'dt_pshurl':dt_pshurl, 'dt_commit':dt_commit, 'dt_frkurl':dt_frkurl, 'dt_public':dt_public,'dt_create':dt_create,'dt_update':dt_update,'dt_comment':dt_comment,'cmturl':dt_cmturl})
        n=n+1