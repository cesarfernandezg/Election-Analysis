# Election-Analysis

# Project Overview
Complete the election audit of a local congressional election

# Resources
- Data source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.60.0

# Summary
The analysis of the election show:
- Election Results
- Total Votes: 369,711
- Votes per candidate:
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
- Winner
  Winner: Diana DeGette
  Winning Vote Count: 272,892
  Winning Percentage: 73.8%

# Challenge Overview
The purpose of this election audit is to know how many votes were in total for each county and for each candidate, in Colorado. It was requested to get the total votes and also the percentage of votes for each candidate in order to determine the winner.

# Election Audit Results
- How many votes were cast in this congressional election?
  Total votes = 369,711
  
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  Votes per County:
  - Jefferson: 38,855 (10.51%)
  - Denver: 306,055 (82.78%)
  - Arapahoe: 24,801 (6.71%)
  
- Which county had the largest number of votes?
  Denver had the largest number of votes. This could be because Denver has a larger population than the other two counties.
  
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  Votes per Candidate:
  - Charles Casper Stockham: 85,213 (23.05%)
  - Diana DeGette: 272,892 (73.81%)
  - Raymon Anthony Doane: 11,606 (3.14%)
<img width="493" alt="Screen Shot 2021-10-10 at 20 37 03" src="https://user-images.githubusercontent.com/90527537/136721514-a3affecb-c57f-48fe-b2a8-919a85a82e3b.png">

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  The winner is:
  Diana DeGette, with a total votes of 272,892 that is 73.81% of the votes

# Election-Audit Summary
One advantage of writing scripts on Python is that the script could be modified in order to adatp the script to any situation and give the results that are expected. For instance, this scrip could be very useful to any other election in the US. Of course it must be modified but that is the beauty of Python, that the code can be adapted to any situation.
The following code can help this commission for any election by doing the following changes:
1. The first step would be getting a new data file with the election results and the script would work if the data has: county names, candidate names, total votes.
So, what the commission should do is to capture the data in a CSV file in order to be loaded and readable
2. Another way this script could be helpful to any election, is that not matter the quantity of the data or the votes for this matter, the script would run and get the results the commission ask for in less time than using other tools.

