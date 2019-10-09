import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Instructions/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation data"""
    # Query all passengers
    prcp_results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    
    # Convert list of tuples into normal list
    all_prcp = []
    for date, prcp in prcp_results:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations"""
    print("Here i am in stations")
    station_results = session.query(Station.station).distinct().all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = []
    for station in station_results:
        station_dict = {}
        station_dict["Station"] = station
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations"""
    print("Here i am in tobs")
    last_tobs_data = session.query(Measurement.date, Measurement.tobs).\
                    order_by(Measurement.date.desc()).first()
    last_date = last_tobs_data[0]
    last_date_object = dt.datetime.strptime(last_date, "%Y-%m-%d")
    deltatime = (last_date_object - dt.timedelta(365))

    # Perform a query to retrieve the data and tobs scores
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
                      filter(Measurement.date >= deltatime).\
                      order_by(Measurement.date.desc()).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = []
    for date, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temp Obs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def weather_data(start):
    print(f"Start Date {start}")
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Stations"""
    print("Here i am in stations")
    weather_startDate = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close()    
    # Convert list of tuples into normal list
    weather_st = []
    for Tmin, Tavg, Tmax in weather_startDate:
        wt_dict = {}
        wt_dict["Tmin"] = Tmin
        wt_dict["Tavg"] = Tavg
        wt_dict["Tmax"] = Tmax
        weather_st.append(wt_dict)

    return jsonify(weather_st)

 

if __name__ == '__main__':
    app.run(debug=True)
