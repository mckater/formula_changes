from flask import Flask, render_template, url_for
# from diagnose import add_diagnosis_routes

app = Flask(__name__)
# add_diagnosis_routes(app)
#

@app.route('/change_diagnosis')
def schange_diagnosis():
    return render_template('change_diagnosis.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
