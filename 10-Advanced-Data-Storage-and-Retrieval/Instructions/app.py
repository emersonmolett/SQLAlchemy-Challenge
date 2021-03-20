import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt 

from sqlalchemy.pool import StaticPool 

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
 
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.passenger

Station = Base.classes.station 
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Home page

@app.route("/")
def welcome():
  
    return """"<html>
<h1> Climate App (Flask API)</h1>
<p> Precipitation Analysis:</p>
<ul>
    <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
</ul>
<p> Station Analysis:</p>
<ul>
    <li><a href="/api/v1.0/stations"/api.v1.0/stations</a></li>
</ul>
<p> Temperature Analysis:</p>
<ul>
    <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
</ul>
<p> Start Day Analysis:</p>
<ul>
    <li><a href="/api/v1.0/2017-08-18">/api/v1.0/2017-08-18</a></li>
</ul>
<p>Start & End Analysis:</p>
<ul>
   <li><a href="api/v1.0/2017-08-18/2017-08-18">/api/v1/0/2017-08-18/2017-08-18</a></li>
</ul>
</html> 
""""
# Precipitation Route
@app.route("ap1/v1.0/precipitation")

def precipitation():
    #Convert the query results to a dictionary using date as the key and prcp as the value.
    one_year_from_last_date = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation_date = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_from_last_date).\
        order_by(Measurement.date).all()

    precipitation_date_list = dict(precipitation_date)
    return jsonify(precipitation_date_list)
    
# Station Route 
@app.route("/api/v1.0/stations")
    def stations():
      station_all = session.query(Station.station, Station.name).all()
      station_list = list(station_all)  
      return jsonify(station_list)








@app.route("/api/v1.0/names")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Passenger.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/passengers")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)

# @app.route("/api/v1.0/time_series/<start_date>")
# def passengers(start_date):
    

#     return jsonify(all_passengers)
if __name__ == '__main__':
    app.run(debug=True)
