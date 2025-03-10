from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes-somos')
def about():
    return render_template('about.html')

@app.route('/servicios')
def services():
    return render_template('services.html')

@app.route('/noticias')
def news():
    return render_template('news.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return "Gracias por tu mensaje <b>" + name +"</b>. Te contactaremos al <b>" + email + "</b> pronto."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
