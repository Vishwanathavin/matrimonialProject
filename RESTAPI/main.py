from flask import Flask, render_template, request,json,jsonify
from flask_pymongo import PyMongo


app=Flask(__name__)
app.config['MONGO_DBNAME'] = 'ssmatri'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ssmatri'
mongo = PyMongo(app)

@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        name_ = request.form.get('name')
        ID_ = request.form.get('ID')

        # Get all the input

        # print and see respose

        # do a find filter in mongodb

        # print result

               
        response = {'message': "Welcome to matri! " + name_}
        return jsonify(response)
        # print ("Name, ID",name_," ",ID_ )

    return 1

if __name__ == "__main__":
	app.run(host="0.0.0.0")
