# summarize_post.py
import os
import sys
import requests
import json

def summarize_file(file_path):
    with open(file_path, 'r') as f:
        post_content = f.read()

    response = requests.post('http://localhost:8000/summarize', json = {'text': post_content})
    summarized_content = response.json()['summary']

    with open(file_path, 'w') as f:
        f.write(summarized_content)
        f.write("\n\n")
        f.write(post_content)

if __name__ == "__main__":
    changed_files = sys.argv[1].split()
    for file in changed_files:
        if file.endswith('.md') and 'docs/' in file:
            summarize_file(file)
