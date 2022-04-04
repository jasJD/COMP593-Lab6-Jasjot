from pprint import pprint 
from sys import argv
import requests


def main():
    user_num = argv[1]
    dict = poke_info(user_num)

    if dict:

        user_strings =  poke_info(dict)
        pastebin_url = post_to_pastebin(user_strings[0], user_strings[1])
        print(pastebin_url)

def post_to_pastebin(title, body):
    print("Posting to Pastebin...", end='')
    
    params = {

        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    
    }
    resp_msg = requests.post(" https://pastebin.com/api/api_post.php", data=params)

    if resp_msg.status_code == 200:
        print('Success')
        return resp_msg.text
    else:
        print('failed. Code:',resp_msg.status_code)
        return str(resp_msg.status_code)
                
def get_poke_string(poke_info):
    title = poke_info['name'] + "'s'Stats"
    body_text =  poke_info['weight'] + '\n'
    body_text += "Ability 1:" + poke_info["abilities"][0]['ability']["name"] + '\n'
    body_text += "Ability 2:" + poke_info['abilities'][1]['ability']["name"] + '\n'
    return (title,body_text)
    

def poke_info(user_num):
    print("Getting user info...", end='')
    resp_msg = requests.get("https://pokeapi.co/api/v2/pokemon-form/" + user_num)

    if resp_msg.status_code == 200:
        print('Success')
        return resp_msg.json()
    else:
        print('failed. Code:',resp_msg.status_code)
        return 
    
main()




