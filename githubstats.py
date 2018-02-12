#!/usr/bin/env python

from github import Github

g = Github(client_id="5ab8062c170c1245b85d", client_secret="4bf2688b6b191ba1df0330ad63fe16f8a58f57c4")

# Contents of array are 0:commits, 1:issues, 2:unit tests
amrutha = [0] * 3
sonam = [0] * 3
jenni = [0] * 3
ruchi = [0] * 3
jaemin = [0] * 3

calculated = False

repo = g.get_user("sonambenakatti").get_repo("idb")
open_issues = repo.open_issues_count # Number of open issues

# Get number of commits for each user
def user_commits():
    stats = repo.get_stats_contributors()
    while(stats == None):
        stats = repo.get_stats_contributors()
    
    for contributor in stats:
        name = contributor.author.name
        total = contributor.total
        if name == "Amrutha Sreedharane":
            amrutha[0] = total
        elif name == "Sonam Benakatti":
            sonam[0] = total
        elif name == "Jennifer Rethi":
            jenni[0] = total
        elif name == "Ruchi Shekar":
            ruchi[0] = total
        elif name == "Jaemin":
            jaemin[0] = total

# Get number of issues for each user
def user_issues():
    for issue in repo.get_issues(state="closed"):
        name = issue.closed_by.name
        if name == "Amrutha Sreedharane":
            amrutha[1] += 1
        elif name == "Sonam Benakatti":
            sonam[1] += 1
        elif name == "Jennifer Rethi":
            jenni[1] += 1
        elif name == "Ruchi Shekar":
            ruchi[1] += 1
        elif name == "Jaemin":
            jaemin[1] += 1

# Get the total number of commits for the repository
def total_commits() -> int:
    total_commits = 0
    total_commits = amrutha[0] + sonam[0] + jenni[0] + ruchi[0] + jaemin[0]
    return total_commits

