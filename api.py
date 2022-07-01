import requests
import json
import argparse
from datetime import datetime, timedelta

def getPullRequests(baseURL, header) :

    response = requests.request("GET", baseURL, headers=header, verify=False)
    jsn = json.loads(response.text)
    prList = []

    for pr in jsn:

        prList.append({"title": pr["title"], "state": pr["state"],
        "projectName": pr["base"]["user"]["login"],
        "repoName": pr["head"]["repo"]["name"], "authorName": pr["user"]["login"],
        "reviewerName": pr["requested_reviewers"], "prLink": pr["url"],
        "createdDate": pr["created_at"]})

    prFilterList = filter(lambda c: datetime.strptime(c["createdDate"], "%Y-%m-%dT%H:%M:%Sz") > (datetime.now() - timedelta(days=7)), prList)
    sendEmail(prFilterList)

def sendEmail(jsnResp):

    htmlBody = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html><head><style>
    tr.firstChild {
       background-color: #D0D0D0;
    }
    th {                  
        padding: 5px;
        text-align: center;
        font-weight: bold;
       }
    td {
        padding: 5px;
        text-align: left;
       }
    td, th {
        border: solid 1px black;
           }
    </style></head><body>
    <p><b>FROM</b>: rm-auto@test.com<br>
    <b>TO</b>: rm@test.com<br>
    <b>Subject</b>: PR Created for last week</p>
    Hi,<br/> <br/>Please find the list below<br/></br>
    <table border="0" cellpadding="0" cellspacing="0"><tr class="firstChild" ><th>Title</th><th>State</th><th>Project Name</th><th>Repo Name</th> 
    <th>Author</th><th>Reviewer</th><th>PR Link</th></tr>"""
     
   
    for prData in jsnResp:

        htmlBody += "<tr><td>"+ prData["title"]+ "</td><td>" + prData["state"] + "</td><td>"
        htmlBody += prData["projectName"]+ "</td><td>" + prData["repoName"] + "</td><td>"
        htmlBody += prData["authorName"]+ "</td><td>" + str(prData["reviewerName"]) + "</td><td>" + prData["prLink"]+ "</td></tr>"
    
    htmlBody += "</table>"
    print(htmlBody)
    
    

"""
##### Send Mail ####
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("youremailusername", "password")
server.sendmail("you@gmail.com", "target@example.com", htmlBody)
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--token', help='token to connect')
    parser.add_argument('--projectName', help='project Name')
    parser.add_argument('--repoName', help='repository name')

    args = parser.parse_args()
    baseURL = "https://api.github.com/repos/"+args.projectName+"/"+args.repoName+"/pulls"
    headers = {

    "Accept": "application/json",

    "Authorization": "Bearer {TOKEN}".format(TOKEN=args.token)
}

    getPullRequests(baseURL, headers)