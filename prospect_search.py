"""
This is an experimental project to write a program
that helps a salesperson to quickly identify the full contact information of a named prospect.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of sales prospects
prospects = [
    {'name': 'John Smith', 'company': 'ABC Corp', 'email': 'john.smith@abccorp.com', 'phone': '123-456-7890'},
    {'name': 'Jane Doe', 'company': 'XYZ Inc', 'email': 'jane.doe@xyzinc.com', 'phone': '234-567-8901'},
    {'name': 'Bob Johnson', 'company': 'ACME Corp', 'email': 'bob.johnson@acmecorp.com', 'phone': '345-678-9012'},
    {'name': 'Alice Lee', 'company': 'Foo Bar Inc', 'email': 'alice.lee@foobar.com', 'phone': '456-789-0123'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['search_input']
        matches = [prospect for prospect in prospects if query.lower() in prospect['name'].lower() or query.lower() in prospect['email'].lower() or query in prospect['phone']]
        return render_template('index.html', prospects=prospects, matches=matches)
    return render_template('index.html', prospects=prospects)

if __name__ == '__main__':
    app.run(debug=True)
