import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://app.gleam.bot',
    'Referer': 'https://app.gleam.bot/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
}

def print_(word):
    now = datetime.now().isoformat(" ").split(".")[0]
    print(f"[{now}] {word}")    
    

def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print_("File query_id.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print_("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]


def auth(query):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/auth'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def list(token):
    url = 'https://prod-api.gleam.bot/api/v1/projects/list'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_campaign(token):
    url = 'https://prod-api.gleam.bot/api/v1/campaigns'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_list_by_random(token):
    url = 'https://prod-api.gleam.bot/api/v1/projects/list?orderBy=random'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_quest_by_random(token):
    url = 'https://prod-api.gleam.bot/api/v1/projects/partners/quests?orderBy=random'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def quest(token, slug):
    url = f'https://prod-api.gleam.bot/api/v1/projects/{slug}/quests'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def start(token, id, query):
    url = f'https://prod-api.gleam.bot/api/v1/quests/{id}/start'
    headers['Authorization'] = f'Bearer {token}'
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def check(token, id, query):
    url = f'https://prod-api.gleam.bot/api/v1/quests/{id}/check'
    headers['Authorization'] = f'Bearer {token}'
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claim(token, id, query):
    url = f'https://prod-api.gleam.bot/api/v1/quests/{id}/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claimproject(token, slag, query):
    url = f'https://prod-api.gleam.bot/api/v1/projects/{slag}/farming/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(res.get('message'))
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claimrefill(token, query):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/energy/refill/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(f" Status Claim : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def startrefill(token, query):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/energy/refill/start'
    headers['Authorization'] = f'Bearer {token}'
    payload = {
        'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(f" Status Start : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getreffstats(token):
    url = 'https://prod-api.gleam.bot/api/v1/referrals/stats'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claimreffstats(token, query):
    url = 'https://prod-api.gleam.bot/api/v1/referrals/claim'
    headers['Authorization'] = f'Bearer {token}'
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(f" Status Claim : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def visits(token):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/visit'
    headers['Authorization'] = f'Bearer {token}'
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print_(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claim_daily_reward(token):
    url = 'https://prod-api.gleam.bot/api/v1/accounts/claim-daily-rewards'
    payload = {}
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(f" Status Start : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def unclaimed_loot(token):
    url = 'https://prod-api.gleam.bot/api/v1/lootboxes/unclaimed/count'
    headers['Authorization'] = f'Bearer {token}'
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            res = response.json()
            print_(f" Status Start : {res.get('message')}")
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claim_all_slug(quest_list, token, query):
    for project in quest_list:
        print_(f"Project : {project['title']}")
        slug = project.get('slug')
        # data_claimproject = claimproject(token, slug, query)
        # if data_claimproject is not None:
        #     print_(f"Claim Amount Farming : {data_claimproject['farming']['claimedAmount']} ")
        time.sleep(2)
        data_quest = quest(token, slug)
        if data_quest is not None:
            for quests in data_quest['quests']:
                completions = quests.get('completions')
                id = quests.get('id')
                if len(completions) == 0:
                    print_(f"Task : {quests['title']}")
                    data_start = start(token, id, query)
                    if data_start is not None:
                        print_('task opened...')
                    time.sleep(2)
                    data_check = check(token, id, query)
                    if data_check is not None:
                        print_('task checked...')
                    time.sleep(2)
                    data_claim = claim(token, id, query)
                    if data_claim is not None:
                        print_('task claimed...')
                    time.sleep(2)
                else:
                    for comp in completions:
                        state = comp.get('state')
                        if state == 'Claimed':
                            print_(f"Task : {quests['title']} DONE !!!")
                        else:
                            print_(f"Task : {quests['title']}")
                            data_check = check(token, id, query)
                            if data_check is not None:
                                print_('task checked...')
                            time.sleep(2)
                            data_claim = claim(token, id, query)
                            if data_claim is not None:
                                print_('task claimed...')
                            time.sleep(2)
        else:
            print_('detail quest not found')

def claim_all(list, token, query):
    for quests in list:
        completions = quests.get('completions',[])
        id = quests.get('id')
        if len(completions) == 0:
            print_(f"Task : {quests['title']}")
            data_start = start(token, id, query)
            if data_start is not None:
                print_('task opened...')
            time.sleep(2)
            data_check = check(token, id, query)
            if data_check is not None:
                print_('task checked...')
            time.sleep(2)
            data_claim = claim(token, id, query)
            if data_claim is not None:
                print_('task claimed...')
            time.sleep(2)
        else:
            for comp in completions:
                state = comp.get('state')
                if state == 'Claimed':
                    print_(f"Task : {quests['title']} DONE !!!")
                else:
                    print_(f"Task : {quests['title']}")
                    data_check = check(token, id, query)
                    if data_check is not None:
                        print_('task checked...')
                    time.sleep(2)
                    data_claim = claim(token, id, query)
                    if data_claim is not None:
                        print_('task claimed...')
                    time.sleep(2)

def claimdaily():
    while True:
        selector_ref = input("Claim ref point ? (default n) (y/n): ").strip().lower()
        if selector_ref in ['y', 'n', '']:
            selector_ref = selector_ref or 'n'
            break
        else:
            print_("Input 'y' or 'n'.")

    while True:
        queries = load_credentials()
        sum = len(queries)
        for index, query in enumerate(queries, start=1):
            print_(f"========== Account {index}/{sum} ==========")
            data_auth = auth(query)
            if data_auth is not None:
                token = data_auth.get('token')
                account = data_auth.get('account')
                energy = account['energyAmount']
                maxEnergy = account['maxEnergyAmount']
                print_(f"ID : {account['id']} || Name : {account['firstName']} {account['lastName']} || Username : {account['beautyName']}")
                print_(f"Energy : {account['energyAmount']}/{account['maxEnergyAmount']}")
                
                data_visit = visits(token)
                if data_visit is not None:
                    visit = data_visit.get('visit')
                    rewardsClaimed = visit.get('rewardsClaimed')
                    if not rewardsClaimed:
                        time.sleep(2)
                        data_claim_daily = claim_daily_reward(token)
                        if data_claim_daily is not None:
                            print_(f"daily reward claimed : Day {visit.get('consecutiveDays')} | Reward : {data_claim_daily.get('transaction').get('amount')}")


                time.sleep(2) 
                if energy >= 5:

                    data_campaign = get_campaign(token)
                    if data_campaign is not None:
                        list_campaigns = data_campaign.get('campaigns',[])
                        for campaign in list_campaigns:
                            title = campaign.get('title','')
                            print_(f"Title Main Task : {title}")
                            quests = campaign.get('quests',[])
                            claim_all(quests, token, query)

                    # data_quest_random = get_quest_by_random(token)
                    # if data_quest_random is not None:
                    #     claim_all(data_quest_random.get('quests'), token, query)

                    data_list = list(token)
                    if data_list is not None:
                        claim_all_slug(data_list.get('projects'), token, query)
                    
                    

                        

                    
                    
                else:
                    print_('Energy to low')
                
                if selector_ref == 'y':
                    statsref = getreffstats(token)
                    if statsref is not None:
                        reward = float(statsref.get('unclaimedRewardAmount'))
                        if reward > 0 :
                            claimreff = claimreffstats(token, query)
                            balance = claimreff.get('balance')
                            print_(f"Claim Balance : {reward} : Total Claim Balance : {balance['totalAmount']}")

                # if energy != maxEnergy:
                #     data_claimrefill = claimrefill(token, query)
                #     time.sleep(1)
                #     if data_claimrefill is not None:
                #         print_("Energy Claimed")
                #         time.sleep(1)

                #     data_startrefill = startrefill(token, query)
                #     if data_startrefill is not None:
                #         print_("Start Refill")
                #         time.sleep(1)

            else:
                print_('User Not Found')

        delay = random.randint(24000, 25000)
        printdelay(delay)
        time.sleep(delay)


def main():
    print(r"""
        
            Created By SxG
    find new airdrop & bot here: t.me/sansxgroup
              
        select this one :
        1. claim daily
          
          """)

    selector = input("Select the one ? (default 1): ").strip().lower()

    if selector == '1':
        claimdaily()
    else:
        exit()

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")


if __name__ == "__main__":
    main()