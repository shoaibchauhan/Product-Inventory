# Product Inventory API

This project provides a set of CRUD APIs for managing a product inventory using FastAPI, Pydantic, Uvicorn, ORM, and PostgreSQL. The project is designed to be production-ready and dockerized for ease of deployment.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- CRUD operations for managing products.
- Dockerized for easy deployment.
- Type hints for better code readability and maintenance.
- Follows REST API design best practices.
- Uses PostgreSQL as the database.

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/product-inventory-api.git
    cd product-inventory-api
    ```

2. Start the application using Docker Compose:

    ```bash
    docker-compose up --build
    ```

    This command will start the FastAPI application along with a PostgreSQL database.

## Usage

The API will be available at `http://localhost:8000`.

You can access the interactive API documentation at `http://localhost:8000/docs`.

## API Endpoints

- **GET /products**: Get all products.
- **GET /products/{id}**: Get a single product by ID.
- **POST /products**: Create a new product.
- **PUT /products/{id}**: Update a product by ID.
- **DELETE /products/{id}**: Delete a product by ID.

## Project Structure

