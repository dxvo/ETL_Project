# ETL_Project - Consumer Price Index (CPI) DataBase 

### Background:
- The CPI measures the retail price changes of about 80,000 goods and services purchased by consumers, called a market basket. The market basket covers over 180 categories falling into eight major groupings:
    <ul>
		<li>Food and beverage</li>
		<li> Housing </li>
		<li>Apparel</li>
		<li>Transportation</li>
		<li>Medical care</li>
		<li>Recreation</li>
		<li>Education and communication</li>
		<li>Other</li>
		<li>Food and beverage </li>
    </ul>
- There is a base period for the CPI: the current base period is the 36 month period encompassing the years 1982-1984. This base period is equal to “100” on the index. Subsequent measurements are expressed as some multiple of this base period, for example a 20% increase would be expressed as “120.”

### How could it be useful?
- The Consumer Price Index (CPI) is a measure that examines the weighted average of prices of a basket of consumer goods and services, such as transportation, food and medical care. It is calculated by taking price changes for each item in the predetermined basket of goods and averaging them. Changes in the CPI are used to assess price changes associated with the cost of living; the CPI is one of the most frequently used statistics for identifying periods of inflation or deflation.

### Relational or Nonrelational Database?
- It will be relational database as we would like to make it available to be used for time or category analysis. For example, different categories can be analyzed on same time period or vice versa. Also, relational database would be ideal in this case to manage a database in an effective manner. Each database will be linked to each other by year or relative category so it can be analyzed in different spectrum. 

### Data Source

[Web_Scrapping From This Source](http://www.econstats.com/blscu/cu_itemSAFy.htm)</br> 
[API Request from FED website](https://api.stlouisfed.org) </br>
[Excel Source from Labor Statistics](https://www.bls.gov/developers/)

### Procedure

- 1st step: Extract information from source stated above 
- 2nd step: Clean and transform data into dataframe (please see .ipynb files for more details)
- 3rd step: Load data infro MySQL database 
- Final step is to build an API application with flask to display query results in json format.