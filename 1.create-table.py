import boto3


def create_table():
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table_creation_resp = dynamodb.create_table(
        TableName='Student',
        KeySchema=[
            {
                'AttributeName': 'dept',
                'KeyType': 'HASH'  # Partition Key
            },
            {
                'AttributeName': 'stud_id',
                'KeyType': 'RANGE'  # Sort Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'dept',
                'AttributeType': 'S'  # string data type
            },
            {
                'AttributeName': 'stud_id',
                'AttributeType': 'S'  # string data type
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print(table_creation_resp)


if __name__ == "__main__":
    create_table()
