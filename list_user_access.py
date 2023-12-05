
"""
This code is used to query ranger and print the accesses defined for a given user. 
"""
import requests
import getpass


ranger_url = input("Enter the ranger url: ")
ranger_admin_user = input("Enter the ranger admin id: ")
pwd=getpass.getpass("Enter the admin password: ")
query_user = input("Enter the id of the user to view their access:")


output={}
url = ranger_url + "/service/public/v2/api/policy"
r = requests.get(url,verify=False, auth=(ranger_admin_user,pwd))
cntr=0
for item in r.json():
    #print(str(item['id']) + " -- " + item['name'])
    service_name=item['service']
    
    resource_item={}
    for resources_key in item['resources'].keys():
        resource_item[resources_key]=item['resources'][resources_key]['values']            
        
    for policy in item['policyItems']:
        access_list=[]
        for access in policy['accesses']:
            if access['isAllowed'] == True:
                access_list.append(access['type'])
        
        for user in policy['users']:
            if user == query_user:
                cntr= cntr + 1
                if service_name in output:
                    output[service_name][cntr] = {"Access":access_list, "items":resource_item}
                else:
                    output[service_name] = {cntr:{"Access":access_list, "items":resource_item}}



for svc in output.keys():
    print("\n")
    print("########################################")
    print(svc + ": ")
    print("########################################")
    for cnt in output[svc].keys():
        print(output[svc][cnt]['items'])
        print(output[svc][cnt]['Access'])
        print("\n")
                
