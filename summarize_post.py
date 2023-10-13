# summarize_post.py
import os
import sys
import requests
import json

def summarize_file(file_path):
    with open(file_path, 'r') as f:
        post_content = f.read()

    length = 4000
    summarized_contents = []
    for i in range(0, len(post_content), length):
        response = requests.post('http://43.201.66.120:8000/summarize', json = {'text': post_content[i:i + length]})
        summarized_contents.append(response.json()['summary'])
    
    response = requests.post('http://43.201.66.120:8000/summarize', json = {'text': '\n'.join(summarized_contents)})
    summarized_content = response.json()['summary']

    front_matter, main_content = post_content.split('\n---')
    
    with open(file_path, 'w') as f:
        f.write(front_matter)
        f.write("\n---\n")
        f.write('TL;DR; (OpenAI API, github actions 기반 자동 요약문)')
        f.write('\n***\n')
        f.write(summarized_content)
        f.write('\n***\n')
        f.write(main_content)

    # with open(file_path, 'r') as f:
    #     print(f"Content of {file_path} after writing:")
    #     print(f.read())

if __name__ == "__main__":
    changed_files = sys.argv[1].split()
    # changed_files = ['docs/Study/CFReviewModel.md']
    print(changed_files)
    for file in changed_files:
        if file.endswith('.md') and 'docs/' in file:
            print(file)
            summarize_file(file)

# response = requests.post('http://43.201.66.120:8000/summarize', json = {'text': post_content})
# summarized_content = response.json()['summary']


