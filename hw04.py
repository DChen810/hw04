import requests
import json
"""
You should write a function that will take as input a GitHub user ID. 
The output from the function will be a list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories.


So, for example, if user John567 has 2 repositories named "Triangle567" and "Square567" each with some number of commits, then the function might output :

Repo: Triangle567 Number of commits: 10
Repo: Square567 Number of commits: 27
"""
"""
getRepo function:get the name of the repository of the users using API 
"""
def getRepo(username):
    API = ("https://api.github.com/users/" + username + "/repos")
    userInfo = requests.get(API)
    repos = json.loads(userInfo.text)
    repoResult = [ ]
    
    for repoTarget in repos:
        try:
            repoResult.append(repoTarget.get("name"))
        except:
            repoResult = []
         
    return repoResult


"""
getCommit function: get the number of commit times of each repositories
"""
def getCommit(username,reponame):
    API = "https://api.github.com/repos/" + username + "/" + reponame + "/commits"
    repoInfo = requests.get(API)
    commits = json.loads(repoInfo.text)
    commit = len(commits)
    return commit

if __name__ == "__main__":
    username = input("Enter the username: ")     
    repoResult = getRepo(username) 
    print("user:  " + username)
    for repository in repoResult:              
        commit = getCommit(username, repository)
        print("Repo: " + repository + " Number of Commits: " + str(commit))