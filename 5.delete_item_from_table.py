import boto3


def delete_student(dept, stud_id):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    delete_item_resp = table.delete_item(
        Key={
            'dept': dept,
            'stud_id': stud_id
        }
    )

    print(delete_item_resp)


if __name__ == '__main__':
    delete_student('PHYSICS', 'STUD-001')
