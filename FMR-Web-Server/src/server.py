from flask import render_template
import connexion
#Makes application instance
app = connexion.App(__name__,specification_dir='./')
#Read Swagger file to find endpoints
app.add_api('swagger.yml')
#Makes URL route in application for '/'
@app.route("/")
def home():
    return render_template('home.html')
#If run in standalone mode, run application
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
