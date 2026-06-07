import boto3
import os
from dotenv import load_dotenv

# Load AWS credentials from .env file
load_dotenv()

# Get credentials from .env
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_REGION = os.getenv('AWS_REGION')

# Connect to AWS S3
s3 = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Files to upload
files_to_upload = [
    ('economic_data.csv', 'raw/worldbank/economic_data.csv'),
    ('combined_data.csv', 'processed/combined_data.csv')
]

# Upload each file
for local_file, s3_path in files_to_upload:
    print(f"Uploading {local_file} to s3://{AWS_BUCKET_NAME}/{s3_path}...")
    s3.upload_file(local_file, AWS_BUCKET_NAME, s3_path)
    print(f"Done - {local_file} uploaded successfully")

print("\nAll files uploaded to AWS S3")