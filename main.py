from flask import Flask, render_template, request
app = Flask(__name__)
import pickle

file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method== "POST":
        myDict = request.form
        Fever = int(myDict['Fever'])
        Age = int(myDict['Age'])
        Pain = int(myDict['Pain'])
        RunnyNose = int(myDict['RunnyNose'])
        diffBreath = int(myDict['diffBreath'])
    

        inputFeatures=[Fever,Pain,Age,RunnyNose,diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print(infProb)

        return render_template('show.html', inf=round(infProb*100))
    return render_template('index.html')

    #return 'Hello , world' +  str(infProb)

if __name__ == "__main__":
    app.run(debug=True) 