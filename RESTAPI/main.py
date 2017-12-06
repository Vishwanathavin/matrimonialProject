from flask import Flask, render_template, request,json,jsonify
from flask_pymongo import PyMongo


app=Flask(__name__)
app.config['MONGO_DBNAME'] = 'ssmatri'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ssmatri'
mongo = PyMongo(app)

@app.route('/', methods=['POST'])
def root():

    name = request.form.get('name')
    # ID = request.form.get('ID')
    STAR_noPadham = request.form.get('stars')
    GOTHRAM = request.form.get('gothram')
    SUBSECT = request.form.get('subsect')
    # qualification_ = request.form.get('qualification')
    age_From = request.form.get('ageFrom')
    age_TO = request.form.get('ageTo')
    height_From = request.form.get('heightFrom')
    height_To = request.form.get('heightTo')

    # Get all the input
    filterList=["STAR_noPadham","GOTHRAM","SUBSECT","age_From","age_TO","height_From","height_To"]

    queryList=[]
    for filter in filterList:
        if filter is not None:
            if filter in [STAR_noPadham,GOTHRAM,SUBSECT]:
                queryList.append({filter:filter})



    # do a find filter in mongodb
    output = mongo.db.personInfo.find({"$and":[{"STAR_noPadham":STAR_noPadham},{"SUBSECT":subsect_}]})
    for val in output:
        print(val)
    response = {'message': "Welcome to matri!."+name}

    return jsonify(response)
    # print ("Name, ID",name_," ",ID_ )


if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)
