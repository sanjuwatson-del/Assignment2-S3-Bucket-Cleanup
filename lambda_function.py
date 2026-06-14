import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = "assignment2-s3-cleanup-yourname"

def lambda_handler(event, context):

    deleted_files = []

    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME
    )

    if 'Contents' in response:

        for obj in response['Contents']:

            file_age = datetime.now(
                timezone.utc
            ) - obj['LastModified']

            if file_age.days > 30:

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=obj['Key']
                )

                deleted_files.append(
                    obj['Key']
                )

                print(
                    f"Deleted: {obj['Key']}"
                )

    return {
        "statusCode": 200,
        "deleted_files": deleted_files
    }