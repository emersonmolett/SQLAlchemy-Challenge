This assignment uses Python and SQLAlchemy to perform climate analysis and data exploration. </br>

Precipitation Analysis: </br>
As the data set contained measurements going back to January 1, 2010, the data had to be structured in a way to only analyze that last year of information. A new dataframe was created with this information and sorted by date. Pandas was used to create a plot, visualizing the precipitation for the specified 12-month period.  

</br>

Station Analysis: </br>
Code was successfully deployed that:
<li>Identifies the number of unique weather stations</li>
<li>Identifies the most active weather station</li>
<li>Calculates the maximum, minimum and average temperatures for the most active weather station</li> 
<li>Creates a histogram plot for the temperature observation data, for the prior 12-months</li>

</br>

API SQLite Connection & Landing Page:</br>
A Flask Application was effectively implemented that: 
<li>Generates the engine to the sqlite file</li>
<li>Reflects the database schema</li>
<li>Saves measurement & station to the table in the sqlite file</li>
<li>Creates and bikes the session between the Python application and database</li>

</br>

API Static Routes:</br>
The statis route accomplished:
<li>Return the JSONified precipitation data for the last year in the database</li>
<li>Produces a JSON with the date as the key and the value of the precipitation</li>
<li>Generates the JSONified data of all the stations in the database</li>
<li>Makes the JSONified data for the most active station for the prior 12-months</li>

</br>
API Dynamic Route:
A dynamic route was generated that:
<li>Accepts the state date as a parameter from the URL</li>
<li>Returns the minimum, maximum, and average temperatures calculated from the given start date to the end of the dataset </li>

