# Data Dictionary


## Yellow Taxi Trip Records

1. **VendorID:** A code indicating the TPEP provider that provided the record.
(Values: 1: Creative Mobile Technologies, LLC 2: VeriFone Inc.)

2. **tpep_pickup_datetime:** The date and time when the meter was engaged. 
Data type: Datetime

3. **tpep_dropoff_datetime:** The date and time when the meter was disengaged. Data type: Datetime

4. **Passenger_count:** The number of passengers in the vehicle. This is a driver-entered value.
Data type: Integer

5. **Trip_distance:** The elapsed trip distance in miles reported by the taximeter.
Data type: Numeric (decimal)

6. **PULocationID:** TLC Taxi Zone in which the taximeter was engaged.
Data type: Integer

7. **DOLocationID:** TLC Taxi Zone in which the taximeter was disengaged.
Data type: Integer

8. **RateCodeID:** The final rate code in effect at the end of the trip.
(Values:
1: Standard rate
2: JFK
3: Newark
4: Nassau or Westchester
5: Negotiated fare
6: Group ride)

9. **Store_and_fwd_flag:** Indicates whether the trip record was held in vehicle memory before sending to the vendor (store and forward) due to a lack of server connection.
(Values:
Y: Store and forward trip
N: Not a store and forward trip)

10. **Payment_type:** A numeric code signifying how the passenger paid for the trip.
(Values:
1: Credit card
2: Cash
3: No charge
4: Dispute
5: Unknown
6: Voided trip)

11. **Fare_amount:** The time-and-distance fare calculated by the meter.
Data type: Numeric (decimal)

12. **Extra:** Miscellaneous extras and surcharges (currently only $0.50 and $1 rush hour and overnight charges).
Data type: Numeric (decimal)

13. **MTA_tax:** $0.50 MTA tax automatically triggered based on the metered rate in use.
Data type: Numeric (decimal)

14. **Improvement_surcharge:** $0.30 improvement surcharge assessed at the flag drop (began in 2015).
Data type: Numeric (decimal)

15. **Tip_amount:** Tip amount (automatically populated for credit card tips; cash tips not included).
Data type: Numeric (decimal)

16. **Tolls_amount:** Total amount of all tolls paid in the trip.
Data type: Numeric (decimal)

17. **Total_amount:** The total amount charged to passengers (does not include cash tips).
Data type: Numeric (decimal)

18. **Congestion_Surcharge:** Total amount collected in the trip for NYS congestion surcharge.
Data type: Numeric (decimal)

19. **Airport_fee:** $1.25 fee for pickups at LaGuardia and John F. Kennedy Airports.
Data type: Numeric (decimal)


## 1. **Light Duty Vehicles**

1. **Vehicle ID:** Identification number for the vehicle

2. **Fuel ID:** Identification number for the type of fuel

3. **Fuel Configuration ID:** Identification number for the fuel configuration

4. **Manufacturer ID:** Identification number for the manufacturer

5. **Category ID:** Identification number for the category of vehicle

6. **Model:** Model of the vehicle

7. **Model Year:** The year the model of the vehicle was released
   
8. **Alternative Fuel Economy City:** Fuel economy in city conditions for alternative fuels
    
9. **Alternative Fuel Economy Highway:** Fuel economy on highways for alternative fuels
    
10. **Alternative Fuel Economy Combined:** Combined fuel economy for alternative fuels
    
11. **Conventional Fuel Economy City:** Fuel economy in city conditions for conventional fuels
    
12. **Conventional Fuel Economy Highway:** Fuel economy on highways for conventional fuels
    
13. **Conventional Fuel Economy Combined:** Combined fuel economy for conventional fuels
    
14. **Transmission Type:** Type of transmission used in the vehicle
    
15. **Engine Type:** Type of engine in the vehicle
    
16. **Engine Size:** Size of the vehicle's engine
    
17. **Engine Cylinder Count:** Number of cylinders in the vehicle's engine
    
18. **Engine Description:** Description of the vehicle's engine
    
19. **Manufacturer:** Name of the manufacturer
    
20. **Manufacturer URL:** URL related to the manufacturer

21. **Category:** Category or type of the vehicle
    
22. **Fuel Code:** Code representing the type of fuel
    
23. **Fuel:** Type of fuel used by the vehicle
    
24. **Fuel Configuration Name:** Name of the fuel configuration
    
25. **Electric-Only Range:** Range when operating solely on electric power
    
26. **PHEV Total Range:** Total range for plug-in hybrid vehicles
    
27. **PHEV Type:** Type of plug-in hybrid vehicle
    
28. **Notes:** Additional notes or remarks
    
29. **Drivetrain:** Type of drivetrain used in the vehicle

## 2. **Alternative Fuel Vehicles US**

1. **Category:** Vehicle Type

2. **Model:** Vehicle model, for example, "NSX" and "A3".

3. **Model Year:** Year of the vehicle model

4. **Manufacturer:** Vehicle manufacturer

5. **Fuel:** Type of fuel used by the vehicle

6. **All-Electric Range:** Fully electric range for electric vehicles

7. **PHEV Total Range:** Total range for plug-in hybrid vehicles

8. **Alternative Fuel Economy City:** Fuel economy in city for alternative fuels

9. **Alternative Fuel Economy Highway:** Fuel economy on highway for alternative fuels

10. **Alternative Fuel Economy Combined:** Combined fuel economy for alternative fuels

11. **Conventional Fuel Economy City:** Fuel economy in city for conventional fuels

12. **Conventional Fuel Economy Highway:** Fuel economy on highway for conventional fuels

13. **Conventional Fuel Economy Combined:** Combined fuel economy for conventional fuels

14. **Transmission Type:** Type of transmission

15. **Transmission Make:** Transmission manufacturer

16. **Engine Type:** Type of engine, for example, "SI" (fuel injection).

17. **Engine Size:** Engine size, for example, "3.5L" and "2.0L".

18. **Engine Cylinder Count:** Number of cylinders in the engine, for example, 6 and 4 cylinders.

19. **Number of Passengers:** Number of passengers the vehicle can accommodate

20. **Heavy-Duty Power System:** Heavy-duty power system

21. **Notes:** Additional notes, NaN indicates no data in this case.

22. **Drivetrain:** Type of drivetrain, for example, "AWD" (all-wheel drive) and "FWD" (front-wheel drive).

## 3. Electric and alternative full charing

1. **Fuel Type Code:** Indicates the type of fuel used by vehicle charging stations.

* CNG: Compressed Natural Gas.
* E85: A blend of ethanol with 85% ethanol and 15% gasoline.
* BD: Biodiesel, a renewable diesel fuel derived from biological sources.
* ELEC: Electricity.
* LPG: Liquefied Petroleum Gas.

2. **Station Name:** Name of the station.

3. **Street Address:** Represents the physical addresses of vehicle charging stations.

4. **Intersection Directions:** Provides detailed instructions on how to reach each charging station from specific locations or via specific routes.

5. **City:** City.

6. **State:** State.

7. **ZIP:** ZIP code.



## 4. **ElectricCarData**

1. **Brand:** Car brand (object).

2. **Model:** Car model (object).

3. **AccelSec:** AccelSec stands for "Acceleration Seconds." It measures how quickly the car can accelerate from 0 to 100 kilometers per hour (km/h) (float).

4. **TopSpeed_KmH:** Maximum speed the car can reach, measured in kilometers per hour (int).  

5. **Range_Km:** estimated maximum distance the car can travel on a single charge, measured in kilometers  (int).

6. **Efficiency_WhKm:** Efficiency_WhKm stands for "Efficiency Watt-Hours per Kilometer." It measures how efficiently the car uses energy, reflecting how much energy it consumes to travel a kilometer (int).  

7. **FastCharge_KmH:** Speed at which the car can recharge its battery using a fast charging station, measured in kilometers of range gained per hour of charging (object). 

8. **RapidCharge:** General term indicating whether the car supports some form of fast charging, allowing for quicker battery replenishment compared to standard charging (object).

9. **PowerTrain:** Refers to the combination of components that generate and deliver power to the wheels, including the motor(s), battery, and drivetrain. Electric cars typically have either a single motor (RWD) or dual motors (AWD).  (object) 

10. **PlugType:** Type of connector used to charge the car's battery  (object).

11. **BodyStyle:**  Overall physical shape and design of the vehicle, considering factors like passenger and cargo capacity, door configuration, and roofline  (object).

12. **Segment:** Market category the car belongs to, based on its size, features, and target audience  (object).

13. **Seats:** Number of seats in the vehicle (int).

14. **PriceEuro:** Vehicle price in euros (int).

# 5-6. **Taxi_zones** 

1. **Shape_Leng:** Length of the shape or area boundary (float).

2. **Shape_Area:** Area of the shape or area boundary (float).

3. **LocationID:** Location ID (int).

4. **Borough:** Borough or county name (object).

5. **Zone:** Geographical zone name (object).

6. **service_zone:** Service zone (object).




# 7. Vehicle Fuel Data Part 1. 


1. **ID (Unique Vehicle Identification) (int):** This column is maintained for the purpose of uniquely identifying each vehicle in the dataset, which facilitates vehicle management and tracking.


2. **Year (Year) (int):** The year of manufacture is retained, as it is relevant to determine the age of the vehicles, which may be related to their efficiency and emissions.


3. **Manufacturer (object):** The manufacturer is retained in consideration that this information provides insights into the quality and reputation of the vehicles, factors that may influence the decision to purchase vehicles from a particular manufacturer.


4. **Model (object):** The model name of the vehicle is maintained to identify the characteristics and specifications of each vehicle, which is essential for the analysis.


5. **fuelType1 and fuelType2 (FuelType1 and FuelType2)  (object):** These columns are retained to assess the feasibility of transitioning to electric vehicles and their impact on air quality. They say if a vehicle use FuelType 1(gas) o FuelType 2(E85, Electric)


6. **co2 (CO2 emissions in grams/mile for fuelType1) (float):** Retained to assess the environmental impact of vehicles on air quality, taking into account carbon dioxide emissions.


7. **co2A (CO2 emissions in grams/mile for fuelType2) (float):** Like the previous column, this is retained for alternative fuel vehicles.


8. **cylinders (Engine cylinders) (int):** The number of cylinders is retained, as it influences the performance and efficiency of the vehicle.


9. **Drive shaft type (object):** This is retained to consider the suitability of vehicles in different climatic conditions.


10. **VClass (EPA Vehicle Size Class)  (int):** Vehicle size classification is important in determining its carrying capacity and suitability for different types of passenger transport services.


11. **Range (int):** Vehicle range is crucial in assessing the availability and range of services.


12. **rangeCity and rangeHwy (City and highway range)  (int):** These columns are kept to plan routes in different driving conditions.


13. **phevBlended (Combined Plug-in Hybrid Electric Vehicle)  (int):** This column is maintained to consider hybrid vehicles.


14. **guzzler (Gasoline guzzler) (boolean):** Retained to identify vehicles with high fuel consumption.


15. **city08 (City MPG for fuelType1)  (float):** Number of miles a vehicle can travel per gallon of fuel under city driving conditions.


16. **cityA08 (city MPG for fuelType2) (float):** Number of miles a vehicle can travel for each gallon of alternative fuel in city driving conditions.


17. **cityCD (City gasoline consumption in depletable charging mode)  (float):** Gasoline consumption in depletable charging mode while driving in the city for plug-in hybrid vehicles (PHEVs) combined.


18. **cityE (City electricity consumption in kw-hrs/100 miles)  (float):** Electricity consumption in kilowatt-hours per 100 miles while driving in the city for electric vehicles.


19. **comb08U (Unrounded combined MPG for fuelType1) (float):** Unrounded value of miles per gallon under combined driving conditions for conventional vehicle fuel.


20. **combA08U (unrounded combined MPG for fuelType2) (float):** Unrounded value of miles per gallon under combined driving conditions for the vehicle's alternative fuel.


21. **combE (Combined electricity consumption in kw-hrs/100 miles) (float):** Combined electricity consumption in kilowatt-hours per 100 miles while driving under combined conditions.


22. **fuelCost08 (Annual fuel cost for fuelType1 in dollars) (float):** Estimated annual fuel cost in dollars for conventional vehicle fuel, based on 15,000 miles, 55% city driving and the price of fuel used by the vehicle.


23. **fuelCostA08 (Annual fuel cost for fuelType2 in dollars) (float):** Estimated annual fuel cost in dollars for the vehicle's alternative fuel, based on 15,000 miles, 55% city driving and the price of fuel used by the vehicle.


24. **ghgScore (EPA GHG Score; -1 = Not Available) (int):** Greenhouse gas (GHG) emissions score assigned by the EPA, where -1 indicates that the information is not available.


25. **lv2 (Cargo Volume 2) (int):** A measure of the space available for luggage or cargo in the vehicle, expressed in cubic feet.


26. **pv2 (Passenger Volume 2) (int):** A measure of the space available for passengers in the vehicle, expressed in cubic feet.


27. **phevComb (Plug-in Hybrid Electric Vehicle Combined MPG) (float):** A measure of the fuel consumption of the vehicle under mixed driving conditions, expressed in miles per gallon equivalent, which is a unit that compares the energy consumed by different types of fuel.


28. **highwayCD:** highway fuel economy for different types of vehicles.

29. **trany:** information about the type of transmission of vehicles.

30. **UCity:** Numerical values that could represent city fuel efficiency for 
different vehicles.

31. UHighway: It seems to contain numerical values that could represent highway fuel efficiency for 
different vehicles.

32. youSaveSpend:It seems to contain numerical values that possibly represent the savings or expenditure 
associated with the fuel efficiency of a vehicle compared to an average vehicle.

33. trans_dscr: It appears to contain descriptions related to the type or mode of transmission of the 
vehicles.

34. sCharger: It appears to contain categorical values indicating the presence of a supercharger in 
the vehicles.

35. atvType: It appears to contain information about the type of propulsion system or technology used in vehicles.

    - Hybrid: Indicates that the vehicle is a hybrid.
    
    - Diesel: Indicates that the vehicle uses a diesel engine.
    
    - EV: Indicates that the vehicle is electric.
    
    - FFV: Possibly indicates that the vehicle is a Flexible Fuel Vehicle, capable of running on 
    alternative fuels such as ethanol.
    
    - Bifuel (CNG): Indicates that the vehicle has the capability to use two types of fuel, with 
    one of them being compressed natural gas (CNG).
    
    - CNG: Indicates that the vehicle runs on compressed natural gas.
    
    - Bifuel (LPG): Indicates that the vehicle has the capability to use two types of fuel, with 
    one of them being liquefied petroleum gas (LPG).

36. "createdOn" seems to contain creation dates associated with the records of vehicles in the dataset.