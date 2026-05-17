from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
 
 return "DevSecOps Lab run Success"
 
@app.route("/health")
def health():
 
 return {
      "status": "healthy",
      "service": "devsecops-lab"
         }

@app.route("/version")
def version():
 
 return {
      "version": "1.0",
      "environment": "development"
        }

if __name__ == "__main__":
 
 app.run(host="0.0.0.0", port=8080)
