from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

#to do all the above dynamicaly

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#if I want to write to text
def write_to_file(data):
    with open('database.txt', mode ='a') as database:
        email = data['email']
        subject=data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode ='a') as database_csv:
        email = data['email']
        subject=data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#this is for the contact form, there are adjustments in the contact.html also for this
@app.route('/submit_form', methods=['POST', 'GET'])   #post means the browser wants us to save information, get means that the browsers to send information
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()    #{'email': 'ionveronica87@gmail.com', 'subject': 'sss', 'message': 'ssssssssssssssssssss'} 
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
    