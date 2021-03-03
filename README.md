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
- convert to html with pandoc
- update updates.html to include new post
- unstage markdown files so they don't get added to remote repo 

## post-commit hook:
- stage html post and updated updates.html
- push to remote 
- run selenium_test.py

# Selenium automation
- prints each post title to console 
- checks each post url to see if it is valid
- prints error with url to console if invalid

# lighthouse automation 
- integrated with git actions
