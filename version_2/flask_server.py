from flask import Flask,render_template,request,redirect,url_for
import os

app = Flask(__name__)



import geojsonio

from geojsonio import display

with open('stations3.geojson') as f:
    contents = f.read()
    #print geojsonio.make_url(contents)
    #print contents
    #display(contents)
    #print geojsonio.make_url(contents)


#@app.route('/')
#def hello_world():
#    return geojsonio.make_url(contents)
    
@app.route('/')
def index():
    #return render_template('index.html')
    return redirect(geojsonio.make_url(contents))

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(geojsonio.make_url(contents))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')    
    
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 6001))
    app.run(host='0.0.0.0', port=port)    