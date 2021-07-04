from flask import Flask,request;
from flask import render_template,jsonify,request;
#from flask import mysqldb
from flask_cors import CORS, cross_origin


app= Flask(__name__) # this is used to create an instance of flask app and then instansiate it
CORS(app);
app.config['CORS_HEADERS']='Content-Type';

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET','POST'])
def insert():
    return 'Insert API';

@app.route('/test_2',methods=['GET','POST'])
def test_2():
    #return 'API HI
    name=request.args.get('name');
    print(name);
    return '<h1>Name is : {}</h1>'.format(name);
    

@app.route('/test', methods=['GET','POST'])
def test():
  #  if request.method=='Post':  # check which method the data was sent by using flask request
    userDetails=request.form    
    name=userDetails['name_data'];
        #emailid=userDetails['emailid_data'];
        #password=userDetails['password_data'];
    print('User details name >'+ name +', emailid > ')#emailid+ ', password >' +password);
    print('Testing successfull');
    return 'API Test Hit .'
    

if __name__ =='__main__':   # it will check if the app name is main if yes run the app
    app.run(debug=True) #to make sure that changes are getting reflected instantly in dev we use debug=True


