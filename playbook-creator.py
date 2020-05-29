import keyring
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseTask, CaseTaskLog
from thehive4py.query import And, In, Not, Eq

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

def get_case_by_casenum(casenum):
    query = And(Eq('caseId', casenum))
    return hive_api.find_first(query=query)

thehive_url="https://hnn-aab-3dctst.nl.eu.abnamro.com:9000"
thehive_token = keyring.get_password('hive_dev','can')

# Connect to TheHive
try:
    hive_api = TheHiveApi(thehive_url, thehive_token, cert=False)
    print('Connected to Hive')
except Exception as e:
    sys.exit(1)

def playbook_mapper(pb_name, case_num):

    with open('mitre-playbooks.json') as f:
        pb_list = json.load(f)
    print('Playbook found')

    for k,v in pb_list.items():
        if k == '{}'.format(pb_name):
            order_by_count = 0
            for key, val in v.items():
                for items in val:
                    task = CaseTask(group='{}'.format(key), title='{}'.format(items), order=order_by_count)
                    r = hive_api.create_case_task(get_case_by_casenum(case_num)['id'], task)
                    print(r.content)
                    order_by_count += 1

# #Testing - select PB:Tac_Teq
#playbook_mapper('PB:Initial Access_Hardware Additions', 461)
#playbook_mapper('PB:Initial Access_Spearphishing Attachment', 398)
