import keyring
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseTask, CaseTaskLog
from thehive4py.query import And, In, Not, Eq

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

# def get_case_by_casenum(casenum):
#     query = And(Eq('caseId', casenum))
#     return hive_api.find_first(query=query)

# thehive_url="https://thehive.com:9000"
# thehive_token = keyring.get_password('hive_dev','can')

# Connect to TheHive
# try:
#     hive_api = TheHiveApi(thehive_url, thehive_token, cert=False)
#     print('Connected to Hive')
# except Exception as e:
#     sys.exit(1)

def chk_mapping(group_def_list):

    try:
        with open('sample-pb.json') as f:
            pb_list = json.load(f)
    except BaseException as e:
        print(e)
        sys.exit(1)

    if pb_list:
        tasks_dict = {}
        for i in group_def_list:
            for k,v in pb_list.items():
                if k == i:
                    for key, val in v.items():
                        if key == 'Default':
                            for phase, task in val.items():
                                tasks_dict[phase] = task
                else:
                    for key, val in v.items():
                        if key == i:
                            for phase, task in val.items():
                                if task:
                                    for k, v in tasks_dict.items():
                                        if k == phase:
                                            for i in task:
                                                v.append(i)
                                            tasks_dict[k] = v
    return tasks_dict


# for k,v in pb_list.items():
#     if k == '{}'.format(pb_name):
#         order_by_count = 0
#         for key, val in v.items():
#             for items in val:
#                 task = CaseTask(group='{}'.format(key), title='{}'.format(items), order=order_by_count)
#                 r = hive_api.create_case_task(get_case_by_casenum(case_num)['id'], task)
#                 print(r.content)
#                 order_by_count += 1

# # #Testing - select PB:Tac_Teq

rule_list = ['Initial Access', 'Drive-by Compromise']
print(chk_mapping(rule_list))

