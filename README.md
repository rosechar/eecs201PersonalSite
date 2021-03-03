# rosechar.github.io
personal website project for eecs 201

uses git hooks (pre-commit and post-commit) to automate the deploy process

# markdown automation

## to add a new post:
- git add 'source/iimd.md' -f (-f flag neccesary bc source folder is in git ignore)
- git commit -m "message"

## pre-commit hook:
- checks whether commit contains markdown files
- if it does, run lint check
- if pass lint, convert to html with pandoc
- unstage markdown files so they don't get added to remote repo 

## post-commit hook:
- stage html post and updated updates.html
- push to remote 
- run selenium_test.py

# Selenium automation
- prints each post title
- checks each post url to see if it is valid
- prints error with url if invalid

# lighthouse automation 
- integrated with git actions
