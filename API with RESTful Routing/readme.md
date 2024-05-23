# Building Your Own API with RESTful Routing
## Concepts Practised
- HTTP Requests (GET, POST, PUT, PATCH, DELETE)
- Postman Software
- Publish API Documentation
## API with RESTful Routing
## Features

- **Retrieve a random cafe**: Get a random cafe from the database.
- **Retrieve all cafes**: Get a list of all cafes in the database.
- **Search for a cafe**: Find a cafe by location.
- **Add a new cafe**: Add a new cafe to the database.
- **Update a cafe's coffee price**: Update the coffee price of a specific cafe.
- **Delete a cafe**: Delete a cafe from the database by ID.

## Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
    ```sh
    pip install Flask Flask-SQLAlchemy
    ```
3. Create the database:
    ```sh
    python
    >>> from your_script_name import db
    >>> db.create_all()
    >>> exit()
    ```

## Configuration

- Ensure that the database URI is correctly set in the script:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    ```

## Usage

1. Run the Flask application:
    ```sh
    python your_script_name.py
    ```
2. Access the API endpoints through a tool like Postman or via your web browser.

<img width="1054" alt="day66" src="https://user-images.githubusercontent.com/98851253/163257600-a4924c5d-7f0b-4606-8583-0a63fbe614e6.png">
