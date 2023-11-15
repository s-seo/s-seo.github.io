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
        response = requests.post('http://13.124.73.243:8000/summarize', json = {'text': post_content[i:i + length]})
        summarized_contents.append(response.json()['summary'])
    
    response = requests.post('http://13.124.73.243:8000/summarize', json = {'text': '\n'.join(summarized_contents)})
    summarized_content = response.json()['summary']

    front_matter, main_content = post_content.split('\n---')

    if 'TL;DR;' in main_content:
        summary_content, main_content = main_content.split('.code-example }')

    with open(file_path, 'w') as f:
        f.write(front_matter)
        f.write("\n---\n\n")
        f.write('### TL;DR;')
        f.write('\n')
        f.write(summarized_content)
        f.write('\n')
        f.write('{: .fs-4 .ls-7 .bg-grey-lt-300 .text-grey-dk-300 .code-example }')
        f.write('\n')
        f.write(main_content)

if __name__ == "__main__":
    changed_files = sys.argv[1].split(',')
    print(changed_files)
    for file in changed_files:
        if file.endswith('.md') and 'docs/' in file:
            print(file)
            summarize_file(file)
        else:
            print('not end with .md')