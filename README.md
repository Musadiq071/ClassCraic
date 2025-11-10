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
