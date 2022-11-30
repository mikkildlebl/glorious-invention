from flask import Flask, render_template, request 

app = Flask(__name__) 
     
@app.route('/')
def index(): 
    return render_template('index.html') 
     
@app.route('/', methods = ['POST']) 
def get_data(): 
    score = request.form['score']
    
    if request.method == 'POST': 
        with open('data.txt', 'w') as f:
            f.write("\n" + str(score))
            f.close()
    return render_template("index.html") 

     
if __name__ == '__main__': 
    app.run(debug = True)
