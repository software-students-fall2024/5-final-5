# Meal Menu Ordering System

![API CI/CD](https://github.com/username/repo/workflows/API%20CI/CD/badge.svg)
![DB CI/CD](https://github.com/username/repo/workflows/DB%20CI/CD/badge.svg)

## Description

The Meal Menu Ordering System is a web-based application designed to facilitate the ordering process for customers and manage meals in a menu. The system uses two subsystems: 
1. A Flask application for handling the frontend and backend logic.
2. A MongoDB database for storing meal, cart, and order data.

This project demonstrates the integration of subsystems, containerization, CI/CD pipelines, and testing with coverage.

## Subsystems

- **Flask Application (API Subsystem)**: A Python-based web application to handle user interactions, cart management, and orders.
- **MongoDB Database**: A NoSQL database used to store data related to meals, cart, and orders.

## DockerHub Links

- [Flask Application Image](https://hub.docker.com/r/username/api)
- [MongoDB Database Image](https://hub.docker.com/r/username/db)

## Teammates

- [Finnick Li](https://github.com/FinnickL)

## Setup Instructions

### Prerequisites

- Docker
- Python 3.9+
- MongoDB

### Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
MONGO_URI=mongodb://<username>:<password>@localhost:27017/meal_menu?authSource=admin
```

Replace `<username>` and `<password>` with your MongoDB credentials.

### Starter Data

To populate the database with starter data, use the following script:

```bash
docker exec -it <db_container_name> mongoimport --db meal_menu --collection meals --file starter_data.json --jsonArray
```

### Running the Project Locally

1. Clone the repository:

    ```bash
    git clone https://github.com/username/repo.git
    cd repo
    ```

2. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

3. Access the application at `http://localhost:5001`.

### Running Tests

To run tests and check coverage:

```bash
pytest --cov=. --cov-report=term
```

## CI/CD Pipeline

This project uses GitHub Actions for CI/CD pipelines. Each subsystem has its own workflow file.

- The API subsystem is built, tested, and deployed via the `api.yml` workflow.
- The Database subsystem is built and deployed via the `db.yml` workflow.

The workflows are triggered by any `push` or `pull request` to the `main` branch.

## Secrets and Configuration Files

- `.env`: Contains sensitive information like database credentials. It should not be included in the repository.
- Ensure that the `.env` file is correctly set up in the production environment.

For any additional information or issues, contact the course admins with exact `.env` details as specified above.
``` 

This `README.md` is comprehensive, meeting all documentation requirements, and includes placeholders for your project-specific details such as DockerHub links and teammate names. Let me know if further adjustments are needed!