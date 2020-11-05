import boto3
import json

dynamodbclient=boto3.resource('dynamodb')
sample_table = dynamodbclient.Table('SDD-Driver')

with open('MOCK_DATA.json', 'r') as myfile:
    data=myfile.read()
    obj = json.loads(data)
    for i in obj:
      response=sample_table.put_item(
                                Item={
                                    'DrivingLicenseNumber': str(i['DrivingLicenseNumber']),
                                    'firstName': i['firstName'],
                                    'lastName': i['lastName'],
                                    'penaltyPoints': str(i['penaltyPoints']),
                                    'category': i['category'],
                                    'address': i['address'],
                                    'postcode': i['postcode']
                                    }
                                )
