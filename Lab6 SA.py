from pprint import pprint 
from sys import argv
import requests


def main():
    user_num = argv[1]
    dict = get_user_info(user_num)

    if dict:

        user_strings =  get_user_strings(dict)
        pastebin_url = post_to_pastebin(user_strings[0], user_strings[1])
        print(pastebin_url)

def post_to_pastebin(title, body):
    print("Posting to Pastebin...", end='')
    
    params = {

        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    
    
    resp_msg = requests.post(" https://pastebin.com/api/api_post.php", data=params)

    if resp_msg.status_code == 200:
        print('Success')
        return resp_msg.text
    else:
        print('failed. Code:',resp_msg.status_code)
        return str(resp_msg.status_code)
            }

def get_user_strings(user_dict):
    title = user_dict['name'] + "'s Location"
    body_text = "Latitude: " + user_dict['address']['geo']['lat'] + "\n"
    body_text += "Longitude: " + user_dict['address']['geo']['lng']
    return (title,body_text)
    

def get_user_info(user_num):
    print("Getting user info...", end='')
    resp_msg = requests.get("https://jsonplaceholder.typicode.com/users/" + user_num)

    if resp_msg.status_code == 200:
        print('Success')
        return resp_msg.json()
    else:
        print('failed. Code:',resp_msg.status_code)
        return 
    
main()




