# DMV
Python program that scrapes NJ DMV website and records the time each licensing location closes for the day. I wrote this because I recently got married and my wife went twice to South Plainfield DMV, waited 6 hours and then was sent home, plus I'm new to Python so it sounded like a fun project.


Sample output:

DMV Scraper Version 2 by Mike Rotella 10-07-2020
Proccessing every 60 seconds for 960 attempts.

Use arguments [inteval in seconds between 1 and 60] [attempts between 1 and 960] to change defaults.

['Bakers Basin', 'Oakland', 'Bayonne', 'Paterson', 'Camden', 'Rahway', 'Cardiff', 'Randolph', 'Delanco', 'Rio Grande', 'Eatontown', 'Salem', 'Edison', 'S. Plainfield', 'Flemington', 'Toms River', 'Freehold', 'Vineland', 'Lodi', 'Wayne', 'Newark', 'W. Deptford', 'N. Bergen']
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
['Bakers Basin', 'Oakland', '10:30:10', 'Paterson', 'Camden', '10:30:10', 'Cardiff', 'Randolph', 'Delanco', 'Rio Grande', 'Eatontown', 'Salem', 'Edison', 'S. Plainfield', 'Flemington', 'Toms River', 'Freehold', 'Vineland', 'Lodi', '10:30:10', '10:30:10', 'W. Deptford', '10:30:10']
['Bakers Basin', 'Oakland', '10:30:10', 'Paterson', 'Camden', '10:30:10', 'Cardiff', 'Randolph', 'Delanco', 'Rio Grande', 'Eatontown', 'Salem', 'Edison', 'S. Plainfield', 'Flemington', 'Toms River', 'Freehold', 'Vineland', 'Lodi', '10:30:10', '10:30:10', 'W. Deptford', '10:30:10']
...
['11:39:19', '13:32:36', '10:30:10', '13:32:36', 'Camden', '10:30:10', 'Cardiff', '12:27:25', '11:39:19', 'Rio Grande', '14:19:42', 'Salem', '11:39:19', '11:39:19', '14:19:42', '14:19:42', '11:39:19', 'Vineland', '11:39:19', '10:30:10', '10:30:10', 'W. Deptford', '10:30:10']
