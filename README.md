

## Lessons Scheduler
Lessons Scheduler is a full-featured application based on the Django framework that enables students applying for classes with a mentor.
This is a web application with the ability to choose a free date and time, cancel a lesson, or reschedule a lesson. Implemented automatic sending of reminders to students by email about the upcoming lesson and to the mentor in his telegram. Used Django, PostgreSQL, Redis, Celery, Docker, integration with Google Calendar, and Telegram API.


---

## Installation

### Prerequisites

#### Docker and Docker Compose

Before installing the package make sure you have Docker and Docker Compose installed:

```bash
>> docker --version
Docker version 24.0.2, build cb74dfc
```

```bash
>> docker-compose --version
Docker Compose version v2.18.1
```


### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/sergdemc/lessons_scheduler.git && cd lessons_scheduler
```


Create email account and generate app password for it. You can use [Gmail](https://mail.google.com/) for this purpose.

Create telegram bot and get its token. You can use [BotFather](https://t.me/botfather) for this purpose.

Get your telegram chat id. You can use [userinfobot](https://t.me/userinfobot) for this purpose.

Create Google Calendar and get its id. You can use [Google Calendar](https://calendar.google.com/) for this purpose.

Then you have to install all necessary dependencies:


Create .env file in the root folder and add following variables:
```bash
BOT_TOKEN = {telegram bot token}
MY_CHAT_ID = {your telegram chat id}

SECRET_KEY = {your Django secret key}

GOOGLE_CALENDAR = {google calendar id}

EMAIL_HOST_PASSWORD =  {app password}
EMAIL_HOST_USER = {email}
```


---

## Usage

Start the Docker containers by running the following command:

```bash
docker-compose up --build
```
By default, the server will be available at http://0.0.0.0:8000. 
