# Movie Manager Tool

The application consists of API endpoints for managing users, movies, and video generation.

## Features

- **Hello Endpoint:**
  - show the Hello, Django! text.
- **Movie Management:**
  - Create, list, view, update, delete Movies.
- **Video Generatin:**
  -We can upload the video, and after uploading, a watermarked version of the video is available for download.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jayeshn10/movie-manager-tool/
cd movie-manager-tool
```
2. Create virtual environment
```
python -m venv venv

OR

virtualenv venv
```
3. Activate virtual environment
```
For windows

command - .\venv\Scripts\activate

For Linux or Mac

command - source venv/bin/activate

```
4. Install all required packages
```
pip install -r requirements.txt
```
5. Install IMAGEMAGICK 
```
Install IMAGEMAGICK and update the path of "IMAGEMAGICK_BINARY" in settings.py
```
6. Run migrations

```
python manage.py makemigrations

python manage.py migrate
```
7. Run Server
```
python manage.py runserver

```
8. Login Credentials
```
username : jayesh

password : jayesh
```

## Note
I added the frontend to the project for a better understanding of the project.