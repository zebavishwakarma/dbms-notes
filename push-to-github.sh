#!/bin/bash
# ============================================================
# push-to-github.sh
# Run this script inside your cloned dbms-notes repo folder
# to commit and push all files to GitHub.
#
# Usage:
#   chmod +x push-to-github.sh
#   ./push-to-github.sh
# ============================================================

set -e

echo ""
echo "========================================"
echo "  DBMS Notes — GitHub Push Script"
echo "========================================"
echo ""

# Check git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: git is not installed. Install it first."
    exit 1
fi

# Check we are inside a git repo
if [ ! -d ".git" ]; then
    echo "Not a git repo. Initializing..."
    git init
    git branch -M main
    echo ""
    read -p "Enter your GitHub remote URL (e.g. https://github.com/username/dbms-notes.git): " remote_url
    git remote add origin "$remote_url"
fi

# Configure git user if not set
if [ -z "$(git config user.name)" ]; then
    read -p "Enter your git username: " git_user
    git config user.name "$git_user"
fi

if [ -z "$(git config user.email)" ]; then
    read -p "Enter your git email: " git_email
    git config user.email "$git_email"
fi

echo ""
echo "Adding all files..."
git add .

echo ""
echo "Files staged:"
git status --short

echo ""
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Add: Complete DBMS notes, SQL scripts, and diagrams (RGPV Sem 5 & 6)"
fi

git commit -m "$commit_msg"

echo ""
echo "Pushing to GitHub..."
git push -u origin main

echo ""
echo "========================================"
echo "  Done! Check your repo on GitHub."
echo "========================================"
echo ""
