from flask import Flask, render_template, request,json,jsonify
from flask_pymongo import PyMongo


app=Flask(__name__)
# app.config['MONGO_DBNAME'] = 'ssmatri'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/ssmatri'
# mongo = PyMongo(app)

@app.route('/', methods=['POST'])
def root():

    name = request.form.get('name')
    # ID = request.form.get('ID')
    stars_ = request.form.get('stars')
    gothram_ = request.form.get('gothram')
    subsect_ = request.form.get('subsect')
    # qualification_ = request.form.get('qualification')
    age_From = request.form.get('ageFrom')
    age_TO = request.form.get('ageTo')
    height_From = request.form.get('heightFrom')
    height_To = request.form.get('heightTo')

    # Get all the input

    # print and see respose

    # do a find filter in mongodb


    response = {'message': "Welcome to matri!."+name}

    return jsonify(response)
    # print ("Name, ID",name_," ",ID_ )


if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)
