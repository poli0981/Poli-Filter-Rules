#!/bin/bash

# Run python script
python autoscript/sort_and_count_everything_rules.py --pure-rules

# Check file changes
ls -la

# Commit and push changes if there are any
git config --global user.name 'github-actions[bot]'
git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
git status
git add .
git diff --staged --quiet && echo "No changes – skip commit" || (git commit -m "Auto update rules [$(date +'%Y-%m-%d')] by GitHub Action" && git push)
