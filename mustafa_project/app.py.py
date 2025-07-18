from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
      <head>
        <title>Mustafa Bot</title>
      </head>
      <body style="font-family: Arial;">
        <button onclick="window.location.href='/details'" 
                style="padding: 10px 20px; font-size: 18px;">Mustafa Khan</button>
      </body>
    </html>
    '''

@app.route("/details")
def details():
    return '''
    <html>
      <head><title>Details</title></head>
      <body style="font-family: Arial;">
        <h2>Name: Mustafa Khan</h2>
        <p>Age: 17</p>
        <p>Course: Artificial Intelligence & Machine Learning</p>
        <p>College: Theem College of Engineering</p>
        <p>Diploma Year: 2nd Year</p>
        <p>10th Passout: 2024</p>
      </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
