# Event Management API

This is a simple Event Management API built with Django and Django Rest Framework (DRF). The API allows you to create and manage events, attendees, and tickets.

## Features

- Create and retrieve events with associated attendees and tickets.
- Validate attendee numbers against the maximum number of attendees for each event.
- Ensure unique email addresses for each attendee.
- SQLite is used as the database for local development and testing.

## Project Structure

- **Event**: Model to store event details (title, date, location, and max_attendees).
- **Attendee**: Model to store attendee information (name and email).
- **Ticket**: Model to associate an attendee with an event (event and attendee foreign keys).

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.
- [Make](https://www.gnu.org/software/make/manual/make.html) installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArashAryanCo/backend-task
   cd backend-task
   ```

2. Build and run the application using Docker and Docker Compose:

   ```bash
   make build
   make up
   ```

### Managing the Project

The `Makefile` provides shortcuts for common Docker and Django management tasks:

- **Start the application:**
  ```bash
  make up
  ```
  This will start the containers in detached mode.

- **Build the Docker images:**
  ```bash
  make build
  ```

- **Stop the running containers:**
  ```bash
  make down
  ```

- **Stop and remove volumes:**
  ```bash
  make down-v
  ```

- **Run migrations:**
  ```bash
  make migrate
  ```

- **Make new migrations:**
  ```bash
  make makemigrations
  ```

- **Create a Django superuser:**
  ```bash
  make createsuperuser
  ```

### Running Migrations

To apply database migrations (SQLite is used by default):

```bash
make migrate
```

To create new migrations based on model changes:

```bash
make makemigrations
```

### Superuser Creation

To create a Django superuser for accessing the admin interface:

```bash
make createsuperuser
```

### Accessing the API

After starting the application, the API will be available at:

- [DRF Docs](http://localhost:8000/api/)
- [Swagger](http://localhost:8000/api/schema/swagger-ui/#/)
- [Redoc](http://localhost:8000/api/schema/redoc/)

You can interact with the following endpoints:

- **Events**: `/api/events/` (GET, POST)
- **Attendees**: `/api/attendees/` (GET, POST)
- **Tickets**: `/api/tickets/` (GET, POST)

### Database

This project uses SQLite as the database, which is sufficient for local development and testing. The database file is stored in the `root` directory and is persisted even after stopping the Docker containers.

### Docker Commands Overview

Here’s a quick summary of the make commands:

| Command            | Description                                      |
|--------------------|--------------------------------------------------|
| `make up`          | Start the Docker containers in detached mode     |
| `make build`       | Build the Docker images                          |
| `make down`        | Stop the running containers                      |
| `make down-v`      | Stop the containers and remove volumes           |
| `make migrate`     | Run Django database migrations                   |
| `make makemigrations` | Create new migrations based on model changes    |
| `make createsuperuser` | Create a superuser for Django admin access     |

### License

This project is licensed under the MIT License. See the [LICENSE](./LICENCE) file for details.