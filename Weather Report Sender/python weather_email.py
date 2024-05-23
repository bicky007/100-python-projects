import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration
API_KEY = 'your_openweathermap_api_key'
CITY = 'your_city'
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
RECIPIENT_EMAIL = 'recipient_email@example.com'

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] != 200:
        raise Exception(f"Error fetching weather data: {data['message']}")
    weather_description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    return f"Weather in {city}:\nDescription: {weather_description}\nTemperature: {temp}°C\nFeels Like: {feels_like}°C\nHumidity: {humidity}%"

def send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {str(e)}')

if __name__ == '__main__':
    try:
        weather_report = get_weather(API_KEY, CITY)
        send_email(
            subject='Current Weather Report',
            body=weather_report,
            to_email=RECIPIENT_EMAIL,
            from_email=EMAIL_ADDRESS,
            from_password=EMAIL_PASSWORD,
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT
        )
    except Exception as e:
        print(f'Error: {str(e)}')
