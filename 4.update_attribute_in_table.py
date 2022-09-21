import boto3


def update_student_name(dept, stud_id, stud_name):
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
        UpdateExpression='SET stud_id = :stud_name',
        ExpressionAttributeValues={
            ':stud_name': stud_name
        }
    )

    print(response)


def update_list_of_subjects(dept, stud_id, subjects):
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
        UpdateExpression='SET subjects = :subjects',
        ExpressionAttributeValues={
            ':subjects': subjects
        }
    )

    print(response)


if __name__ == '__main__':
    update_student_name('PHYSICS', 'STUD-001', 'Valli')
    update_list_of_subjects('PHYSICS', 'STUD-001', ['Mech', 'ECE'])
