import os
import sys
from flask import Flask

_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, root_path=_root_path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://palm:Palmtech001@127.0.0.1:3306/flagman'

sys.path.append(os.path.join(_root_path, 'http'))
sys.path.append(os.path.join(_root_path, 'kernel'))

from  routes import api

