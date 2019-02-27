import numpy as np
from sqlalchemy import create_engine
from flask import Flask, jsonify
import config
import pymysql
pymysql.install_as_MySQLdb()


# Database Setup              
MySQL_root_PW = config.password
MySQL_db = 'ETL'
engine = create_engine("mysql://root:"+MySQL_root_PW+"@localhost/"+MySQL_db)


#App instance
app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/housing<br/>"
        f"/api/v1.0/medical<br/>"
        f"/api/v1.0/foods"
    )


@app.route("/api/v1.0/housing")
def housing():

    results = engine.execute("Select * FROM Housing;").fetchall()
    result_list = []

    for result in results:
        result_list.append(dict(result))
    return jsonify(result_list)


@app.route("/api/v1.0/medical")
def medical():

    results = engine.execute("Select * FROM Medical;").fetchall()
    result_list = []
    
    for result in results:
        result_list.append(dict(result))
    return jsonify(result_list)



"""@app.route("/api/v1.0/foods")
def foods():
    return """


if __name__ == '__main__':
    app.run()
