from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)


contacts=[
    {
        "id":1,
         "name":'abdull',
         "phone":"080493"
    },
    {
        "id":2,
         "name":'abdull2',
         "phone":"080233493"
    },
    {
        "id":3,
         "name":'abdull3',
         "phone":"080493324"
    }
]

@app.route('/')
def index():
    return render_template("index.html",contacts=contacts)


@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name=request.form['name']
        phone=request.form['phone']
        new_id=len(contacts)+1
        contacts.append({"id":new_id,"name":name,"phone":phone})
        return redirect(url_for('index'))

    return render_template("add.html")  

if __name__=='__main__':
    app.run(debug=True)