from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://palm:Palmtech001@127.0.0.1:3306/flagman'
