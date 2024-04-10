# Cheap-Flight-Finder

Using a combination of different APIs to create a cheap flight finder.

## Table of Contents
- Description
- Installation
- Screenshots

## Description
The Cheap-Flight-Finder is a tool that leverages various APIs to find the most affordable flights. It uses Google Sheets as a database to store the names of cities we're interested in traveling to and the minimum ticket prices we've set for each city. The tool then uses the Tequila API to search for flight information within the next 6 months and sends a notification to our cell phone if it finds a flight that meets our price criteria.


## Tools
- **Google Sheets:** Used as a database to store and retrieve data.
- **Requests:** A Python module used for making HTTP requests to APIs.
- **Sheety API:** This tool enables communication with Google Sheets, allowing us to read, write, and manage data in Google Sheets. It's a valuable tool for automating tasks and managing data.
- **Twilio SMS API:** Used to send a notification to our cell phone when a flight discount is found. More information can be found at https://www.twilio.com/docs/sms.
- **Tequila API:** Used to search for flight information such as prices, departure dates, departure airports, arrival cities and airports, and IATA airport codes. More information can be found at https://tequila-api.kiwi.com.

## Screenshots
![google_sheet_img](https://github.com/bardack134/Cheap-Flight-Finder/assets/142977989/8a772eb2-e93d-4801-b5ee-9fbedccf08ae)




![app-img](https://github.com/bardack134/Cheap-Flight-Finder/assets/142977989/a6ef0aad-ebed-4e3e-a911-6c704ef7c768)



