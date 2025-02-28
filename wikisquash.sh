#!/bin/bash

set -e  # Exit on error

# keep script inside repo
REPO_DIR="$(dirname "$(realpath "$0")")"
cd "$REPO_DIR"

git fetch origin
# Ensure archive branch exists
git checkout -B archive origin/archive || git checkout -B archive
git checkout master  # Work on master branch

# Find the latest commit on archive
LAST_ARCHIVE_COMMIT=$(git rev-parse archive)

# Get new commits on master that are not in archive
NEW_COMMITS=$(git log --reverse --format="%H" "$LAST_ARCHIVE_COMMIT"..master)

# Append new commits to archive
if [[ -n "$NEW_COMMITS" ]]; then
    git checkout archive
    for COMMIT in $NEW_COMMITS; do
        git cherry-pick "$COMMIT"
    done
    git push origin archive
fi

# Switch back to master for squashing
git checkout master
