#!/bin/bash

# Run python script
python autoscript/sort_and_count_everything_rules.py --pure-rules

# Check file changes
ls -la

# Commit and push changes if there are any
git config --global user.name "poli0981"
git config --global user.email "127664709+poli0981@users.noreply.github.com"
git add .
git diff --staged --quiet && echo "No changes – skip commit" || (git commit -m "Auto update rules [$(date +'%Y-%m-%d')]" && git push)
