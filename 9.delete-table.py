import boto3


def delete_table():
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    delete_table_resp = table.delete()

    print(delete_table_resp)


if __name__ == "__main__":
    delete_table()
