import boto3
from boto3.dynamodb.conditions import Key, Attr


def select_a_student(dept, stud_id):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    response = table.query(
        KeyConditionExpression=Key('dept').eq(dept) & Key('stud_id').eq(stud_id)
    )

    print(response['Items'])


def select_all_students_from_dept(dept):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    response = table.query(
        KeyConditionExpression=Key('dept').eq(dept)
    )

    print(response['Items'])


def filter_students_with_name_begins_with(dept, name):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    response = table.query(
        KeyConditionExpression=Key('dept').eq(dept),
        FilterExpression=Attr('stud_name').begins_with(name)
    )

    print(response['Items'])


def filter_stud_with_subject_list_contains(dept, subject_name):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    response = table.query(
        KeyConditionExpression=Key('dept').eq(dept),
        FilterExpression=Attr('subjects').contains(subject_name)
    )

    print(response['Items'])


if __name__ == '__main__':
    select_a_student('MATHS', 'STUD-001')
    select_all_students_from_dept('MATHS')
    filter_students_with_name_begins_with('MATHS', 'Vic')
    filter_stud_with_subject_list_contains('MATHS', 'Quantum')
