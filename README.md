# Matching
Matching Businesses and Local Influencers

This was part of the Product Studio challgenge at Cornell Tech.

In order to assist companies in entering new markets our team developed a platform where we matched local influencers with these companies based on the researched criteria:
- Market (country)
- Industry
- Number of followers
- Price per post

There was a need to create databases of potential local influencers and companies that are willing to enter new markets. 

As not everybody in the team had a technical background, google spreadsheets were used in compiling the aforementioned datasets.

Then, the spreadsheets were converted to SQL tables that were deployed on MySQL server on AWS.

Also the simple script to apply the searching criteria of a selected company was developed. After that it was put to the AWS EC2 instance allowing to call it from different devices.
