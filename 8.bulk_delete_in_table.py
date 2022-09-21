import boto3

from student import Student


def delete_bulk_student_records(students: list):

    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id="dummy",
                              aws_secret_access_key="dummy",
                              region_name="local",
                              endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Student')

    with table.batch_writer() as writer:
        for student in students:
            writer.delete_item(Key={
                'dept': student.dept,
                'stud_id': student.stud_id
            })


if __name__ == '__main__':
    s1 = Student('PHYSICS', 'STUD-001', 'Vicky', 28, ['Material Science'])
    s2 = Student('ENGLISH', 'STUD-002', 'Valli', 28, ['Literature'])
    delete_bulk_student_records([s1, s2])
