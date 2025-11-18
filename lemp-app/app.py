from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/')
def home():

    # Connect to MySQL/MariaDB

    conn = mysql.connector.connect(
            host="localhost",
            user="exampleuser",
            password="LiirumLaarum123#",
            database="exampledb"
            )

    cursor = conn.cursor()

    cursor.execute("SELECT CURRENT_TIMESTAMP")
    result = cursor.fetchone()



    # Clean up
    cursor.close()
    conn.close()

#    return f"<h1>{result[0]}</h1>"
    
    
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
        </div>
    </body>
    </html>
    """



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
