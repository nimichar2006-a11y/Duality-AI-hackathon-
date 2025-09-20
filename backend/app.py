from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to Duality AI Platform Backend"}

if __name__ == "__main__":
    app.run(debug=True)
