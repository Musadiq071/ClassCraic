# test_s3_upload.py
import django
import os
from django.core.files.base import ContentFile
from storages.backends.s3boto3 import S3Boto3Storage

# Set Django settings module (if running as standalone script)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classcraic.settings')
django.setup()

# Create an S3 storage instance
s3_storage = S3Boto3Storage()

# Create a test file in memory
file_content = ContentFile(b"Hello S3 from Django!")

# Save the file to S3
file_name = "test_upload/test_file.txt"
s3_storage.save(file_name, file_content)

# Print the S3 URL
print("File uploaded! Accessible at:", s3_storage.url(file_name))
