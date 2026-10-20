README: COFACTOR-Residential Dataset 3

Dataset Overview
This dataset contains hourly sub-metered energy use data from 194 residential units, including single family houses, apartments and cabins. The data is collected from Sikom Connect AS in the COFACTOR project. Sikom is a Norwegian company specializing in smart control solutions for heating, electricity, and security in homes and cabins. Established in 1997, Sikom has become a leading provider of remote cabin heating solutions, commonly known in Norway as "Ring Hytta Varm," allowing users to control heating and monitor energy consumption via mobile devices. They also sell smart thermostats, heating control units, and control systems for homes and cottages. Users of SIKOMs systems were invited to share their hourly, total electricity consumption data (AMS-measurements) and to participate in a survey about their property for research purposes. 194 property owners (5 apartments, 154 cabins and 35 houses) volunteered to share their energy use data and filled in the survey. The duration of the time series data varies between a few months to two years.  COFACTOR-Residential Dataset 3 contains one csv-file per building. The CSV-files in the dataset contains meta data about the buildings and hourly time series data containing energy use and weather data. The files in Dataset 3 only contain one energy meter per building which is “ElImp”, the AMS-meter that shows the hourly imported electricity use. 


Dataset accessability
Repository name: data.sintef.no
Data identification number: 
Direct URL to data product: https://data.sintef.no/product/dp-b750d103-a434-45c2-ba5e-1af13f0a866f
Direct URL to dataset: https://data.sintef.no/feature/fe-e7c34e7c-162c-40a0-9c6f-c67e60d3281c
Instructions  for accessing the data: The data product is open access and does not require sign-in registration.

Data Summary
- Number of files: 194
- Time series resolution: Hourly
- Time series duration: Variable between 2021-2023.

Data sources:
194 property owners and SIKOM customers (5 apartments, 154 cabins and 35 houses) volunteered to share their energy use data and filled in the survey. The duration of the time series data varies between a few months to two years.

Files and Structure
The dataset consists of a ZIP-folder with comma separated .txt files. Each file is labelled "Building_XXXX" (XXXX is a number) and contains the building information (meta data) and time series data for an individual building/group of buildings. More information about each building is given in the data descriptor (see citation). 
Each CSV file consists of:
1. Metadata Section
- General building details including ID, construction year, floor area, number of buildings and number of units.
- Heating system details
2. Time Series Data Section
- Timestamp format: %Y-%m-%dT%H:%M:%S%z (local normal time: CET, UTC+01:00)
- Weather columns: outdoor temperature, wind speed, wind direction and global solar radiation, relative humidity
- Energy columns: Main or sub-meters [Wh/h]


Codes Used in CSV Files
Metadata Categories
- Header_line: First line of measurements in the CSV file
- Location: Location of the building
- Year_of_construction: Year the building was constructed
- Floor_area: Floor area in square meters
- Number_of_units: Number of apartments in the building/heating central.
- Number_of_buildings: Number of buildings on the lot
- Building_category: Building type (e.g., Apt for apartment)
- Notes: Additional information about the building and energy data
- Dhw_heat_source: Type of heating technology for domestic hot water
- Sh_heat_source: Type of heating technology for space heating
- ev_chargepoints:Number of chargers and their capacity
- ventilation_types:Number of chargers and their capacity
- number_of_users: Number of users (residents)
- Pv: Photovoltaic system specifications
- Timestamp_format: Format for timestamps in the time series
- Time_zone: Time zone of the dataset (UTC+01:00)
- Building_id: Unique identifier for the building

Metadata Codes:
- Apt: Apartment building category
- Hou: Single family house
- Cab: Cabin
- CAV_fxd: Constant air volume (fixed)
- EB: Electric boiler
- EFH: Electric floor heater
- EH: Electric heater
- DH: District heating
- GSHP: Ground source heat pump
- HWH: Hot water heater
- A2A: Air to air heat pump
- FP: Fire place
- ASHP: Air source heat pump
- Nat: Natural ventilation
- Mech: Mechanical ventilation
- "1:7.4": 1 EV charger at 7.4 kW charger capacity


Weather Columns:
- Tout: Outdoor temperature (Celsius)
- SolGlob: Global Solar Horizontal Radiation (W/m2)
- WindSpd: Wind speed (m/s)
- WindDir: Wind direction (degrees)
- RH: Relative humidity (%)


Energy Columns:
- ElImp: Imported electricity (Wh/h)


Applications
The dataset can be used for:
- Energy benchmarking and validation of building simulations
- Heating disaggregation research
- Energy time series classification and forecasting
- Grid planning and energy flexibility studies

Limitations
- Sub-meter quality varies, and users should assess data before resampling
- Gaps exist in some time series, though AMS meters and district heating meters are more reliable
- The dataset is specific to Oslo apartment block, which are within the same climate zone.

Citation
If you use this dataset, please cite:
Sørensen, Å. L., Lien, S. K., & Walnum, H. T. (n.d.). COFACTOR-Residential: Hourly electricity and heating data from residential buildings in Norway. Manuscript submitted for publication in Data in Brief.

Contacts
For questions about the dataset, contact:
Synne Krekling Lien (SINTEF Community)
Email: synne.lien@sintef.no
Harald Taxt Walnum (SINTEF Community)
Email:harald.walnum@sintef.no

Acknowledgements
The dataset is published with permission and help from Dråpe Entreprenør AS, Elvia (DSO), and Sikom Connect AS and we greatly acknowledge them for sharing the access to the data. The dataset is provided by the projects “Coincidence factors and peak loads of buildings in the Norwegian low carbon society” (COFACTOR) funded by Research Council of Norway and partners through grant number 326891. The authors gratefully acknowledge the support from the Research Council of Norway  and research partners.

License
This dataset is licensed under Creative Commons Attribution 4.0 (CC BY 4.0).