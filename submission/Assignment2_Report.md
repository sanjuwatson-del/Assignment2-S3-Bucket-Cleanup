# Assignment 2 Report

## Objective

To gain experience with AWS Lambda and Boto3 by creating a Lambda function that automatically deletes files older than 30 days from an Amazon S3 bucket.

## Services Used

* Amazon S3
* AWS Lambda
* IAM
* CloudWatch
* Boto3

## Steps Performed

1. Created an S3 bucket.
2. Uploaded sample files.
3. Created IAM role with AmazonS3FullAccess.
4. Created Lambda function using Python 3.x.
5. Implemented Boto3 code to identify and delete files older than 30 days.
6. Tested the function manually.
7. Verified deleted files using CloudWatch Logs.

## Output

The Lambda function successfully removed old files and logged the deleted file names.

## Conclusion

The automation worked successfully and reduced manual effort required to manage S3 storage cleanup.
