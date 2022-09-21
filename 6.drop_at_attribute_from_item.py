import boto3


def drop_student_name(dept, stud_id):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    response = table.update_item(
        Key={
            'dept': dept,
            'stud_id': stud_id
        },
        UpdateExpression='REMOVE stud_name'
    )

    print(response)


if __name__ == '__main__':
    drop_student_name('PHYSICS', 'STUD-001')
