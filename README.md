# ranger_api

This code is used to query ranger api and list the accesses defined for a given user in all the ranger policies


Usage:

[mymacbook]$ python3.7 /Users/lakshs80/Desktop/myprojects/ranger/user_perm.py 
Enter the ranger url: https://rangerUi:6182
Enter the ranger admin id: admin
Enter the admin password: 
Enter the id of the user to view their access:shailendra


########################################
schema-registry: 
########################################
{'schema-branch': ['*'], 'schema-metadata': ['*'], 'schema-group': ['*']}
['create', 'read', 'update', 'delete']


{'schema-branch': ['*'], 'schema-metadata': ['*'], 'schema-group': ['*'], 'schema-version': ['*']}
['create', 'read', 'update', 'delete']




########################################
hive: 
########################################
{'database': ['mydatabase'], 'column': ['*'], 'table': ['*']}
['select', 'read']




########################################
knox: 
########################################
{'topology': ['*'], 'service': ['*']}
['allow']




########################################
yarn: 
########################################
{'queue': ['*']}
['submit-app', 'admin-queue']




########################################
nifi: 
########################################
{'nifi-resource': ['*']}
['READ', 'WRITE']




########################################
hbase: 
########################################
{'column-family': ['*'], 'column': ['*'], 'table': ['*']}
['read', 'write', 'create', 'admin']


