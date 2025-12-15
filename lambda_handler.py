lambda_handler.py
import json
import time
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SensorData')

def lambda_handler(event, context):
    item = {
        'DeviceID': event.get('deviceId', 'unknown'),
        'Timestamp': int(time.time()),
        'Temperature': event.get('temperature', 0),
        'Humidity': event.get('humidity', 0)
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps('Data stored successfully')
    }
