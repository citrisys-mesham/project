
from flask import Flask
from controllers import api_blueprint,static_blueprint

app=Flask(__name__)
app.secret_key = 'mysecretkey'

app.register_blueprint(
    static_blueprint,
    url_prefix="/",
)
app.register_blueprint(

    api_blueprint,url_prefix='/api'
)

if __name__==('__main__'):
    app.run(debug=True)