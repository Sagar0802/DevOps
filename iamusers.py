import boto3


client = boto3.client('iam')

listusrs = client.list_users()
#print(listusrs['Users'])


for i in listusrs['Users']:
    for k in i.keys():
        print(k,":", i[k])
