## Data Dictionary


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

# 5. **Taxi_zones** 

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