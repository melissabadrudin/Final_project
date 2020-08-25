
#import Flask magic
from flask import Flask, render_template, request

from helper import run_model
import time


#Flask logic section
#we are creating an object which is a flask app
app = Flask(__name__)

#create routes which is a possible door that our app can expect to be opened
# to do this we need to use decorators -> basicamente é usar um @
#@ calls a python inbuilt function without having to import anything

@app.route('/', methods = ['POST','GET'])

def index():
    #the python logic that will be ran when the route is called
    if request.method == 'POST':
        #do stuff
        parameter_1 = int(request.form['parameter 1'])
        parameter_2 = int(request.form['parameter 2'])
        parameter_3 = int(request.form['parameter 3'])
        parameter_4 = int(request.form['parameter 4'])
        parameter_5 = int(request.form['parameter 5'])
        parameter_6 = int(request.form['parameter 6'])
        parameter_7 = int(request.form['parameter 7'])
        parameter_8 = str(request.form['parameter 8'])
        parameter_9 = str(request.form['parameter 9'])
        parameter_10 = str(request.form['parameter 10'])
        parameter_11 = str(request.form['parameter 11'])
        parameter_12 = str(request.form['parameter 12'])
        
        time.sleep(2)
        prediction = [run_model(parameter_1, parameter_2, parameter_3, parameter_4,parameter_5,parameter_6,parameter_7,parameter_8,parameter_9,parameter_10,parameter_11,parameter_12)]
        print('the prediction is',prediction)
        
        #if we want the result in html
        #we need to pass it as a variable to html
        return render_template('main.html', predictions = prediction[0])
    else:
        return render_template('main.html')


#running our Flask app defined above   
if __name__ == "__main__":
    app.run(debug = True)

