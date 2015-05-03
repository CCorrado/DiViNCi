# DiViNCi
EE/CpE Senior Design
Group 14: Digital Hoboken
Advisor: Professor Bruce McNair
Contact: Christopher Corrado
        CCorrads@gmail.com

Using this Repo Requires understanding of method and goal. The Digital Hoboken Senior Design Project end goal is to produce a readable (and connectable) file or database containing a breakdown analysis of provided twitter data (or other social media data) based on time, location, and frequency. We then provide this analysis to the Virtual Hoboken team for use in the virtual model (Unreal, Unity, etc)

(BuildScripts/BuildLinux.sh) To build out an Ubuntu 14.04 LTS machine with proper requirements, run the linux Script in BuildScripts dir "BuildLinux" as sudo bash BuildLinux. It is reccomended to build a machine with 14.04 and apt-get install git, clone this repo, then create a new branch.

(MiningScripts/Location_Call.py) To garner locations, the Digital Hoboken team decided on utilizing the Yelp API for location search in order to compare specific words from the Twitter data. The Yelp API accomplishes three tasks: 
1. Ability to find locations based on GPS coordinate within a certain radius
2. Return business details (coordinate locaiton, hours, open/closed binaries, full name, rating, etc)
3. Easily manipulated in Python (used), C#, Java, etc.

(MiningScripts/pyminer.py) To analyze the twitter data from the Hob1.SQL file, a python script was written to analyze each line in a database. (local MySQL database imported the Hob1.SQL file) The NLTK (www.nltk.org) libraries were used to tokenize each tweet. In other words, translate each word in the tweet into a grammatical variable, noun, propernoun, adjective, etc)

(DigitalHobokenResults.xlsx) This spreadsheet is a summary of results (tabs with raw data, actual tweets from DB, and a Results tab) after running the pyminer script, outputting the raw text (MiningScripts/Final_Miner_results.txt), formatting this text (removing (),"",u' chars) and importing them comma separated into the spreadsheet.this text is then analyzed in excel in the Results tab using a function (=COUNTIF(Data!A$rownum:A$rownum,Arownum) to count the frequency of the mentioned location name.

Analysis:
The results are quite noisy, because social media data is noisy. Filtering out the top and bottom outlyers is a proof of method as some truth can be found between the data and the analysis. Stronger NLP methods should be implemented to further this code.
