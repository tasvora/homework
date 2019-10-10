import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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


####################################################################################################
# Using the render_template to render a welcome page with all the links to various routes.
# Refered website https://www.freecodecamp.org/news/
#                 how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
####################################################################################################

@app.route("/")
def welcome():
    return render_template("welcome.html")

#################################################################
# Created a route welcome, in case the welcome.html does not work 
#################################################################


@app.route("/welcome")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;&amp;&lt;end&gt;"
    )


####################################################################################################
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
####################################################################################################


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation data"""
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

######################################################
# Return a JSON list of stations from the dataset.
######################################################

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
        station_dict["Station"] = station[0]
        all_stations.append(station_dict)

    return jsonify(all_stations)


####################################################################################################
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
####################################################################################################

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

####################################################################################################
# minimum temperature, the average temperature, and the max temperature for a given start date.
# Return a JSON list with TMIN, TAVG, and TMAX 
####################################################################################################

@app.route("/api/v1.0/<start>")
def weather_data(start):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a TMin TAvg and TMax"""
    print("Here i am in Start Date")
    print(f"Start Date {start}")    
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

####################################################################################################
# minimum temperature, the average temperature, and the max temperature for a given start-end range.
# Return a JSON list with TMIN, TAVG, and TMAX 
####################################################################################################

@app.route("/api/v1.0/<start>/<end>")
def weather_st_end_data(start,end):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a TMin TAvg and TMax"""
    print("Here i am in Start Date And End Date")
    print(f"Start Date {start}")
    print(f"End Date {end}")    
    weather_Date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()    
    # Convert list of tuples into normal list
    weather_st_end = []
    for Tmin, Tavg, Tmax in weather_Date:
        wt_dict = {}
        wt_dict["Tmin"] = Tmin
        wt_dict["Tavg"] = Tavg
        wt_dict["Tmax"] = Tmax
        weather_st_end.append(wt_dict)

    return jsonify(weather_st_end)

#################################################
# Initialize Flask Debug Mode
#################################################

if __name__ == '__main__':
    app.run(debug=True)
