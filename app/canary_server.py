import os
import webcolors
from flask import Flask

app = Flask(__name__)

def color_name_to_hex(color_name):
    """Convert a color name to a hex color code."""
    # Attempt to convert the color name to hex code
    hex_color = webcolors.name_to_hex(color_name)
    return hex_color

@app.route('/')
def home():
    title = "Welcome to the Canary Server"
    
    # Get the background color name from the environment variable or use a default value
    color_name = os.getenv('COLOR', 'white')  # Default color name if not set
    hex_color = color_name_to_hex(color_name)  # Convert color name to hex code
    
    return f'''
        <html>
            <head>
                <title>{title}</title>
                <style>
                    body {{
                        background-color: {hex_color};  /* Background for the canary server */
                        font-family: Arial, sans-serif;
                        text-align: center;
                        padding: 50px;
                    }}
                    h1 {{
                        color: #2b2b2b;
                        font-size: 3em;
                        margin-bottom: 10px;
                    }}
                    h2 {{
                        color: #ff0000; /* Red for canary warning */
                        font-size: 2.5em;
                        margin-top: 0;
                    }}
                    p {{
                        color: #333;
                        font-size: 1.2em;
                    }}
                    .container {{
                        max-width: 800px;
                        margin: 0 auto;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>TEAM R.H.A.L</h1>
                    <h2>{title}</h2>
                    <p>Welcome to the official canary server of Team R.H.A.L. Test the latest features here!</p>
                    <p>Current Background Color: {color_name}</p>

                    <img src="https://i.ibb.co/4Ty2rhs/asd.png" alt="Team R.H.A.L Logo">
                     
                </div>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Different port for the canary server