# AI GITHUB CAREER ADVISOR
import requests

username = input("Enter Your GitHub Username : ")
url = f"https://api.github.com/users/{username}"


response = requests.get(url)


#AGENT FUNCTION
def github_agent(data):
    print("-"*60)
    print("           ==== AI GITHUB CAREER ADVISOR ====")
    username = data['login']
    followers = data['followers']
    repos = data['public_repos']
    bio = data['bio'] or "Not Mentioned"
    company = data["company"]
    location = data["location"] or "Not Mentioned"
    created = data["created_at"] or "Not Mentioned"

    #Details
    print("-"*60)
    print("---USER DETAILS---")
    print(f"USERNAME : {username}")
    print(f"FOLLOWERS : {followers}")
    print(f"REPOSITORIES : {repos}")
    print(f"COMPANY : {company}")
    print(f"LOCATION : {location}")
    print(f"CREATED : {created}")
    print(f"BIO : {bio}")
    print("-"*60)

    
    print("            ---AI ANALYSIS---")

    #followers
    if followers >= 500:
        print("FOLLOWERS SUGGESTION : Strong Github Profile")
    elif followers >= 100:
        print("FOLLOWERS SUGGESTION : Good Github Profile")
    else:
        print("FOLLOWERS SUGGESTION : Beginner Github Profile")

    #repositories
    if repos >= 50:
        print('REPOSITORIES SUGGESTION : Strong Number Of Repositories')
    elif repos > 10:
        print("REPOSITORIES SUGGESTION : Continue contributing to open source.")
    else:
        print("REPOSITORIES SUGGESTION : Keep your repositories updated.")


#Main 
try:
    if response.status_code == 200:
      print(response.status_code, "OK")
      data = response.json()
      github_agent(data)

    else:
      print(response.status_code, "ERROR")
      print("PROGRAM END")
      


except Exception as e:
    print("ERROR OCCURS : ",e)


print("-"*60)
print("THANK YOU FOR USING OUR PROGRAM")