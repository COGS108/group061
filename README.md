This is your group repo for your final project for COGS108.

This repository is private, and is only visible to the course instructors and your group mates; it is not visible to anyone else.

This repository will be frozen on the due date: 11:59pm on Tuesday, June 13th. No further changes can be made after that time.

Your final project will be graded based solely on a project notebook.

Make sure you have a notebook called 'FinalProject.ipynb' present in this repository by the due date.

## Workflow for Pushing Changes
After completing changes IN YOUR BRANCH:
 - Add and commit all relevant files
 
Update your branch to have the new master changes:
 - `git checkout [YOUR BRANCH]`
 - `git merge master`
 - fix any merge conflicts
 - test to make sure nothing broke
 
Squash your commits:
 - `git rebase -i HEAD~[NUMBER OF COMMITS]` OR `git rebase -i [SHA HASH OF FIRST COMMIT]`

Push to master
 - `git checkout master`
 - `git merge [YOUR BRANCH]`
 - `git push'