"""
Install flask:
    - pip3 install flask
Create venv:
    - pip3 install virtualenv
    - python3 -m venv Web/web_server/ or virtualenv Web/web_server
Init Flask(Linux)
    - export FLASK_APP=Web/web_server/server.py
    - flask run

    (Debug mode On) - For modifying in real time
    - export FLASK_ENV=development
    - flask run
Pay attention:
    - You can add {{}} in html to inject Python code.
      Whit this, you can pass parameters to make your website dynamically
    - Pasing parameters: /<username>/<int:post_id>, and then in
      render_template('url', parameter_name=parameter_name_html)
"""
import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>.html')
def html_page(page_name='index.html'):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='\n', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


"""- Add this url in the action attribute of the tag form in the html
   - Add the name of the method to use (GET, POST, PUT, DELETE) in the html tag method
   - Add ,in the html tags inputs/textarea, the attribute name to being able to store that value"""


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)

            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Somthing went wrong'
