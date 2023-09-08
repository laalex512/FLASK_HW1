from flask import Flask, render_template

app = Flask('__name__')


@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/prod_item<num_item>/')
def prod_item(num_item):
    return render_template(f'prod_item{num_item}.html')

@app.route('/for_<for_whom>/')
def for_people(for_whom):
    return render_template(f'for_{for_whom}.html')

if __name__ == '__main__':
    app.run()