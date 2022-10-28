from flask import Flask

#Create app variable with Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Web Services Running'


#Start web services
if __name__ == '__main__':
    app.run(port=3001, debug=True, host='0.0.0.0')
