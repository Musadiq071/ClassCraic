# ClassCraic

**Author / Creator:** Musadiq Hussain – Full Stack Python Developer

**Live Demo:** [ClassCraic on Heroku](https://classcraicapp-f9f89199719c.herokuapp.com/)

---

## Overview

ClassCraic is a social platform for students to engage, share educational materials, and interact with peers. It is built with Django and designed as a starting point for a larger community platform. Users can create profiles, post educational content, comment, like, and manage their own posts. 

This project demonstrates full-stack Django development with features like authentication, file storage on AWS S3, and deployment on Heroku.

---

## Features

- **User Authentication**
  - Register, login, logout
  - Change password, forgot password via email (SMTP)
  - Profile with picture and bio

- **Posts**
  - Create, edit, and delete posts
  - Upload attachments (images, PDFs)
  - Like and comment on posts

- **Social Interaction**
  - Comment and like posts
  - View other user profiles

- **Storage & Deployment**
  - Media files stored on AWS S3
  - Deployed on [Heroku](https://classcraicapp-f9f89199719c.herokuapp.com/)
  - Environment variables managed via `.env` using `python-decouple`

- **Additional Features**
  - Responsive UI using Bootstrap 5
  - Clean, user-friendly interface
  - Pagination for posts
  - Error messages and notifications for better UX

---

## Tech Stack

- **Backend:** Python 3.13, Django 5.2.6
- **Frontend:** Bootstrap 5, HTML, CSS
- **Database:** SQLite (development)
- **Cloud Storage:** AWS S3
- **Deployment:** Heroku
- **Email Service:** Gmail SMTP for password reset
- **Others:** django-crispy-forms, django-storages, python-decouple

---

## Getting Started (Local Development)

Follow these steps to run the project locally:

### Prerequisites

- Python 3.13+
- pip
- Git
- Virtualenv (recommended)

### Clone Repository

```bash
git clone https://github.com/Musadiq071/ClassCraic.git
cd ClassCraic
```
## Local Setup & Usage

### Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
##Install Dependencies

```bash
pip install -r requirements.txt

```
Environment Variables

Create a .env file in the root directory with the following:

SECRET_KEY=your_django_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password_or_app_password
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_STORAGE_BUCKET_NAME=your_s3_bucket
AWS_S3_REGION_NAME=your_s3_region


Run Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser (Optional)
python manage.py createsuperuser

Run the Server
python manage.py runserver


Visit http://127.0.0.1:8000/
 to see the app.

Usage

Register multiple users to simulate social interaction.

Upload posts with attachments (images, PDFs).

Like and comment on posts.

Reset passwords using the “Forgot Password” link.

Explore other user profiles and posts.

Contributing

Contributions are welcome! You can:

Submit feedback: Suggestions for UX/UI improvements or new features.

Collaborate: Contact me for joint projects or feature additions.

Fix bugs or add features: Open issues or submit pull requests.

Contact

Musadiq Hussain

Email: musadiqshahani@yahoo.com

GitHub: Musadiq071

LinkedIn: Musadiq Hussain

License

This project is licensed under the MIT License.
