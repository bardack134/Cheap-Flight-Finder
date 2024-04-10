# Cheap-Flight-Finder
Using a combination of different APIs to create a cheap flight finder.

**Description**
We use Google Docs Sheet as a database. In this document, we save the names of the cities we are interested in traveling to and for which we will search for flight tickets. It also contains minimum ticket prices that we have set for each city. Using Tequila API, we get the ‘IATA location identifier’, which we will use again in Tequila API, to search for flight information within the next 6 months. The cheapest one found in that 6-month period, if the ticket price according to the API, is less than or equal to the price we have set in our ‘Google Sheet’ database, we automatically send a notification to our cell phone with the information of the flight found. For example, ‘ent from your Twilio trial account - Low price alert! Only £64831 to fly from Sapporo-CTS to Bogotá-NRT, from 2024-05-14’


**Tools**

**Google Sheets:** It is used as a database to store and get back data.

**Requests**: A Python module used to make HTTP requests to APIs.

**Sheety API** It's tool that allows us to communicate with Google Sheets. We use Python to read, write, and manage data in Google Sheets. It’s a very useful tool for automating tasks and managing data.

**The Twilio SMS API** - https://www.twilio.com/docs/sms is used to send a message to my cellphone when there is a flight discount.

**Tequila API:** Used to search for flight information such as prices, departure date, departure airport, arrival city and airport, IATA airport code (International Air Transport Association)  "https://tequila-api.kiwi.com"


![google_sheet_img](https://github.com/bardack134/Cheap-Flight-Finder/assets/142977989/8a772eb2-e93d-4801-b5ee-9fbedccf08ae)




![app-img](https://github.com/bardack134/Cheap-Flight-Finder/assets/142977989/a6ef0aad-ebed-4e3e-a911-6c704ef7c768)
