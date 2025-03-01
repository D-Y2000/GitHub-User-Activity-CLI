
import requests 
import re


def get_user_name():
    while(True):
        user_name=input("Enter the user name\n")
        # check if the given name is valid (contains letters)
        if re.search(r'[a-zA-Z]',user_name):
            break
    return user_name

def fetch_user_activity(user_name):
    url = f'https://api.github.com/users/{user_name}/events'
    response = requests.get(url, timeout = 15)
    if response.status_code == 200:
        #convert data into json .
        data = response.json()
        for event in data:
            if event['type'] == 'WatchEvent':
                message = f"{event['payload']['action']} {event['repo']['name']}"
            if event['type'] == 'PushEvent':
                message = f"Pushed {event['payload']['distinct_size']} commit(s) to {event['repo']['name']}"
            elif event['type'] == 'PullRequestEvent':
                message = f"{event['payload']['action']} a pull request to {event['repo']['name']}"
            elif event['type'] == 'PullRequestReviewEvent':
                message = f"{event['payload']['action']} a review on {event['payload']['pull_request']} from {event['repo']['name']}"
            elif event['type'] == 'PullRequestReviewCommentEvent':
                message = f"{event['payload']['action']} a comment  on {event['payload']['pull_request']} from {event['repo']['name']}"
            elif event['type'] == 'CreateEvent':
                message = f"Created a new  {event['payload']['ref_type']}" 
                #check if the object ceated was a branch or a repo.
                if event['payload']['ref_type'] == 'branch':
                    message += f" to {event['repo']['name']}"
                else:
                    message += f" {event['repo']['name']}"
            elif event['type'] == 'DeleteEvent':
                message = f"Deleted a {event['payload']['ref_type']}"
            elif event['type'] == 'ForkEvent':
                message = f"Forked {event['payload']['forkee']}"
            elif event['type'] == 'GollumEvent':
                message = f"{event['payload']['pages']['action']} {event['payload']['pages']['page_name']}"
            elif event['type'] == 'IssuesEvent':
                message = f"{event['payload']['action']} {event['payload']['issue']}"
            elif event['type'] == 'IssueCommentEvent':
                message = f"{event['payload']['action']} a comment on the issue : {event['payload']['issue']}"
            elif event['type'] == 'MemberEvent':
                message = f"{event['payload']['action']} {event['payload']['member']} To (from) {event['repo']['name']}"
            elif event['type'] == 'PublicEvent':
                message = f"Made {event['repo']['name']} public"
            elif event['type'] == 'ReleaseEvent':
                message = f"{event['payload']['action']} {event['payload']['release']}"
                message = f"Made {event['repo']['name']} public"
            print(f" - {message}.\n")
    else:
        print(f'Error fetching events for the user: {user_name}\t status code : {response.status_code}')




if __name__ == "__main__":


    print("####################### GitHub user activity tracker #######################\n\n")
    user_name = get_user_name()
    fetch_user_activity(user_name)


