from flask import Flask,jsonify

 
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(
        status="up",
        server="v1.0"
    )

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Beautiful Glowing Card</title>
  <style>
    body {
      background: #0f0c29;  /* Dark background for contrast */
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: 'Arial', sans-serif;
    }

    .card {
      width: 200px;
      height: 250px;
      background: linear-gradient(45deg, #ff00cc, #3333ff);
      border-radius: 15px;
      padding: 20px;
      color: white;
      box-shadow: 0 0 20px rgba(255, 0, 204, 0.5);
      transition: transform 0.3s, box-shadow 0.3s;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 30px rgba(51, 51, 255, 0.7);
    }

    h1 {
      font-size: 1.5em;
      margin: 0;
    }

    p {
      font-size: 0.9em;
      opacity: 0.8;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello World!</h1>
    <p>✨ Hover over me! ✨</p>
  </div>
</body>
</html>  <br/><br/> This is v1.0"""
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
    
    
from flask import Flask,jsonify

 
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(
        status="up",
        server="v2.0"
    )

@app.route("/")
def home():
    return "<b> Welcome to my project!! </b> <br/><br/> This is v2.0"
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)