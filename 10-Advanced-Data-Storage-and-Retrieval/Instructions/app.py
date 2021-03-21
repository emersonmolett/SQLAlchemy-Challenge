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
"""""
# Precipitation Route
@app.route("ap1/v1.0/precipitation")

def precipitation():
    #Convert the query results to a dictionary using date as the key and prcp as the value.
    one_year_from_last_date = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation_date = Session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_from_last_date).\
        order_by(Measurement.date).all()

    precipitation_date_list = dict(precipitation_date)
    return jsonify(precipitation_date_list)
    
# Station Route 
@app.route("/api/v1.0/stations")
def stations():
      station_all = Session.query(Station.station, Station.name).all()
      station_list = list(station_all)  
      return jsonify(station_list)


# TOBs Route
@app.route("/api/v1.0/tobs")
def tobs():
    one_year_from_last_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    temperature_observation_data = Session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_from_last_date).\
        order_by(Measurement.date).all()
    temperature_observation_data_list = list(temperature_observation_data)
    return jsonify(temperature_observation_data_list)

# Start Day Route
@app.route("/api/v1/0/<start")
def start_day(start):
        start_day = Session.query(Measurement.date,func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            group_by(Measurement.date).all()
        start_day_list = list(start_day)
        return jsonify(start_day_list)


# Start & End Route        
@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start, end):
        start_end_day = Session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).\
            group_by(Measurement.date).all()
        start_end_day_list = list(start_end_day)
        return jsonify(start_end_day_list)


if __name__ == '__main__':
    app.run(debug=True)
