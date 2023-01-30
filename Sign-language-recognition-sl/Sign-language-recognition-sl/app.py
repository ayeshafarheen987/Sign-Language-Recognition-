from flask import Flask
import cv2
## WSGI application
app =Flask(__name__)

@app.route('/')  # decorater
def welcome():  
    return "welcome to Data science "




if __name__=='__main__':
    app.run()