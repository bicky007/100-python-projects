# Weather Email Report

This Python project fetches the current weather report for a specified city using the OpenWeatherMap API and sends it to a specified email address.

## Features

- Fetches the current weather report including temperature, weather description, feels like temperature, and humidity.
- Sends the weather report to a specified email address using SMTP.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required library:
    ```sh
    pip install requests
    ```

## Configuration

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) by signing up.
2. Update the following variables in the script with your own values:
    ```python
    API_KEY = 'your_openweathermap_api_key'
    CITY = 'your_city'
    EMAIL_ADDRESS = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_email_password'
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    RECIPIENT_EMAIL = 'recipient_email@example.com'
    ```
    - Replace `your_openweathermap_api_key` with your actual OpenWeatherMap API key.
    - Replace `your_city` with the city you want to get the weather report for.
    - Replace `your_email@example.com` with your email address.
    - Replace `your_email_password` with your email password.
    - Replace `smtp.example.com` and `587` with your email provider's SMTP server and port. For Gmail, use `smtp.gmail.com` and `587`.
    - Replace `recipient_email@example.com` with the email address you want to send the weather report to.

## Usage

1. Save the script to a file, for example `weather_email.py`.
2. Run the script using Python:
    ```sh
    python weather_email.py
    ```
3. The script will fetch the current weather report for the specified city and send it to the specified email address.

## Example

Here is an example of how to use the script:

1. Open `weather_email.py` in a text editor.
2. Update the configuration section with your API key, city, and email credentials.
3. Run the script:
    ```sh
    python weather_email.py
    ```
4. Check your email for the weather report.


## Acknowledgements

- This project uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch weather data.
- Email sending is handled using Python's built-in `smtplib` library.
