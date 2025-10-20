# test_s3_upload.py
import django
import os
from django.core.files.base import ContentFile
from storages.backends.s3boto3 import S3Boto3Storage

# 1️⃣ Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classcraic.settings')
django.setup()

# 2️⃣ Create an S3 storage instance
s3_storage = S3Boto3Storage()

# 3️⃣ Create a test file in memory
file_content = ContentFile(b"Hello S3 from Django!")

# 4️⃣ Define the exact file path in your existing folder
file_name = "profile_pics/test_file.txt"


# 6️⃣ Save the file to S3
s3_storage.save(file_name, file_content)

# 7️⃣ Print the public URL
print("File uploaded! Accessible at:", s3_storage.url(file_name))
