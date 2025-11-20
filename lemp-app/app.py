from flask import Flask
import mysql.connector
import toml

app = Flask(__name__)

# Load the secrets from the full path of secrets.toml
secrets = toml.load('/home/ubuntu/myapp/.streamlit/secrets.toml')

@app.route('/')
def home():
    # Connect to MySQL/MariaDB using credentials from secrets.toml
    conn = mysql.connector.connect(
        host=secrets["connections"]["mysql"]["host"],
        user=secrets["connections"]["mysql"]["username"],
        password=secrets["connections"]["mysql"]["password"],
        database=secrets["connections"]["mysql"]["database"]
    )

    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_TIMESTAMP")
    result = cursor.fetchone()

    # Clean up
    cursor.close()
    conn.close()

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Timestamp</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f4f4f4;
            }}
            h1 {{
                color: #4CAF50;
            }}
            .container {{
                border: 2px solid #4CAF50;
                padding: 20px;
                border-radius: 10px;
                background-color: white;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Current Timestamp</h1>
            <p style="font-size: 24px;">{result[0]}</p>
            <a href="http://86.50.20.182/data-analysis/">Here to data analytics</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
