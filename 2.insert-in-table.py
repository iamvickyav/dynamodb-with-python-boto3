import boto3

from student import Student


def insert_student_data(stud: Student):
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    insert_item_resp = table.put_item(
        Item={
            'dept': stud.dept,
            'stud_id': stud.stud_id,
            'stud_name': stud.stud_name,
            'stud_age': stud.stud_age,
            'subjects': stud.subjects
        }
    )

    print(insert_item_resp)


if __name__ == '__main__':
    student = Student('PHYSICS', 'STUD-001', 'Vicky', 28, ['Material Science'])
    insert_student_data(student)
