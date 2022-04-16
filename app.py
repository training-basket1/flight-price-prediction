from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np


## WSGI connectrion
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET" ,"POST"])
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_minutes = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_minutes = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
       

        # Duration

        Duration = request.form["Duration"]
        Duration_hours = pd.to_datetime(Duration ).hour
        Duration_minutes = pd.to_datetime(Duration).minute
        

        # Total Stops
        Total_stops = int(request.form["stops"])
       

        # Airline
        airline=request.form['airline']
        Jet_Airways = 0
        IndiGo = 0    
        Air_India = 0
        Multiple_carriers = 0
        Spice_jet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0

        if airline == "Jet Airways":
            Jet_Airways = 1

        elif airline == "IndiGo":
            IndiGo =  1
        
        elif airline == "Air India":
            Air_India = 1

        elif airline == "Multiple Carriers":
            Multiple_carriers = 1

        elif airline == "Spice Jet":
            Spice_jet = 1

        elif airline == "Vistara":
            Vistara = 1
        
        elif airline == "GoAir":
            GoAir = 1

        elif airline == "Multiple Carriers Premium Economy":
            Multiple_carriers_Premium_economy = 1

        elif airline == "Jet Airways Business":
            Jet_Airways_Business = 1

        elif airline == "Vistara Premium Economy":
            Vistara_Premium_economy = 1


        #### Source ###   
        Source = request.form["Source"]
        S_Chennai = 0 
        S_Delhi = 0
        S_Mumbai = 0
        S_Kolkata = 0

        if Source == "Chennai":
            S_Chennai = 1

        elif Source == "Delhi":
            S_Delhi = 1

        elif Source == "Mumbai":
            S_Mumbai  = 1

        elif Source == "Kolkata":
            S_Kolkata = 1



        ## Destination###########
        destination = request.form["Destination"]
        
        D_Cochin = 0 
        D_Delhi = 0
        D_New_Delhi = 0
        D_Hyderabad = 0
        D_Kolkata = 0

        if destination == "Cochin":
            D_Cochin = 1

        elif destination == "Delhi":
            D_Delhi = 1

        elif destination == "New Delhi":
            D_New_Delhi = 1

        elif destination == "Hyderabad":
            D_Hyderabad = 1

        elif destination == "Kolkata":
            D_Kolkata = 1



        prediction = model.predict (np.array([[Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
            Multiple_carriers, Multiple_carriers_Premium_economy, Spice_jet,
            Vistara, Vistara_Premium_economy, D_Cochin, D_Delhi,
            D_Hyderabad, D_Kolkata, D_New_Delhi, S_Chennai, S_Delhi,
            S_Kolkata, S_Mumbai, Total_stops, Journey_day, Journey_month,
            Dep_hour, Dep_minutes, Arrival_hour, Arrival_minutes,
            Duration_hours, Duration_minutes ]]))
       
                                                       

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)




