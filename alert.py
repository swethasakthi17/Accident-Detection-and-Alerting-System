import random
import time
import smtplib

# Set up the SMTP server details
HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "sanjumsanjana@outlook.com"
TO_EMAIL = "swathisanjay408@gmail.com","swethasellam@gmail.com"
PASSWORD = "Msanjana@1659"

# Generate and check random sensor data with timestamp
while True:
    temperature = random.randint(80, 100)
    distance = random.randint(120, 140)

    print(f"Accident detected at {temperature}; distance {distance}")

    # Check if temperature exceeds 95
    if temperature > 95:
        message = f"Subject: Warning\n\n Accident detected ,Speed value exceeded 95 as {temperature}"
        # Send email
        with smtplib.SMTP(HOST, PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, message)

    # Check if distance exceeds 135
    if distance > 135:
        message = f"Subject: Warning\n\nDistance value exceeded 135 as {distance}"
        # Send email
        with smtplib.SMTP(HOST, PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, message)

    time.sleep(3)  # Wait for 3 seconds before the next data check