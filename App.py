from flask import Flask , request , make_response
from rembg import remove

app = Flask(__name__)

@app.route('/' , methods=['POST'])
def removeBG():
    if request.method  != 'POST':
        response = make_response()
        response.status = 409
        return response

 
    if request.files == '' :
        response = make_response()
        response.status = 500
        return response

    file = request.files['file']
    if file.filename == ' ':
        response = make_response()
        response.status = 500
        return response
    
    if file.mimetype != 'jpeg' or 'jpg' or 'png':
        response = make_response()
        response.status = 500
        return response
    
    
if  __name__ == '__main__' :
    app.run('localhost' , 8080 , True)

