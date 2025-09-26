import requests


def get_users() -> list:
    downloadusers   =   requests.get("https://dummyjson.com/users?limit=85") #downloading
    users   =   downloadusers.json().get('users',[]) #convert to list
    return users

def print_users(users:list) -> None:
    for user in users:
        print (user['firstName'])


def main():
    users    =   get_users()
    print_users (users)

if __name__ == "__main__":
    main()

