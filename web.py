from flask import Flask,request,render_template
import joblib
app = Flask(__name__)
@app.route('/')
def main():
    return render_template("body.html")


@app.route('/heart', methods= ['GET','POST'])
def dd():
    m = joblib.load(r'C:\Users\victus\OneDrive\Desktop\mlpro\yoyoy\heartdisease.pkl')
    if request.method == 'POST':
        p = int(request.form['age'])
        a = int(request.form['sex'])
        b = int(request.form['cp'])
        c = int(request.form['trestbps'])
        d = int(request.form['chol'])
        e = int(request.form['fbs'])
        n = int(request.form['restecg'])
        f = int(request.form['thalach'])
        g = int(request.form['exang'])
        h = int(request.form['oldspeak'])
        i = int(request.form['slope'])
        j = int(request.form['ca'])
        k = int(request.form['thal'])
        kl = m.predict([[p ,a , b ,c ,d ,e ,n ,f ,g, h ,i ,j ,k]])
        print(kl)
        if kl == 1:
            b = 'Heart Disease Targeted'
        else:
            b = 'No Heart Disease Targeted'

        print(b)
        return render_template('heart.html', a = b)
    return render_template('heart.html')


@app.route('/brain', methods= ['GET','POST'])
def bb():
    br = joblib.load(r'C:\Users\victus\OneDrive\Desktop\mlpro\yoyoy\brain.pkl')
    if request.method == 'POST':
        p = int(request.form['gender'])
        a = int(request.form['age'])
        b = int(request.form['hyper'])
        c = int(request.form['heartdisease'])
        d = int(request.form['ever'])
        e = int(request.form['fbs'])
        f = int(request.form['type'])
        g = int(request.form['avg'])
        h = int(request.form['bmi'])
        i = int(request.form['smoking'])
        l = br.predict([[p ,a , b ,c ,d ,e ,f ,g, h ,i]])
        if l == 1:
            b = 'Brain Stroke'
        else:
            b = 'No Brain Stroke'
        return render_template('brain.html', r = b)
    return render_template('brain.html')


@app.route('/lungs', methods= ['GET','POST'])
def b():
    l = joblib.load(r'C:\Users\victus\OneDrive\Desktop\mlpro\yoyoy\lungs.pkl')
    if request.method == 'POST':
        u = int(request.form['age'])
        a = int(request.form['gender'])
        f = int(request.form['somkingtesting'])
        b = int(request.form['lungcapacity'])
        c = int(request.form['diseasetype'])
        d = int(request.form['treatmenttype'])
        e = int(request.form['hospitalvisits'])
        k = l.predict([[u ,a , b ,c ,d ,e ,f]])
        if k == 1:
            b = 'Recovered Detected'
        else:
            b = 'Not Recovered Detected'
        return render_template('lungs.html', r = b)
    return render_template('lungs.html')


@app.route('/kidney', methods= ['GET','POST'])
def n():
    p = joblib.load(r'C:\Users\victus\OneDrive\Desktop\mlpro\yoyoy\kid.pkl')
    if request.method == 'POST':
        a = int(request.form['bp'])
        f = int(request.form['sg'])
        b = int(request.form['al'])
        c = int(request.form['su'])
        d = int(request.form['rbc'])
        h = int(request.form['bu'])
        m = int(request.form['sc'])
        n = int(request.form['sod'])
        o = int(request.form['pot'])
        q = int(request.form['hemo'])
        r = int(request.form['wbcc'])
        wi = int(request.form['rbcc'])
        w = int(request.form['htn'])
        kl = p.predict([[a , b ,c ,d ,f ,h ,m ,n ,o ,q ,r ,wi ,w]])
        if kl == 1:
            b = 'Chronic Disease Detected'
        else:
            b = 'Not Disease Detected'
        return render_template('kidney.html', r = b)
    return render_template('kidney.html')


     
if __name__ =='__main__':
    app.run(debug=True)