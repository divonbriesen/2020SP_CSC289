# CSC289 Stock Portfolio Project

An application that allows users to track their stock portfolio

## Stack

- Jinja view engine
- Flask server
- Sqlite3 database

### Setup

Change to the **project** directory then type the following commands:

    > set FLASK_APP=portfolio
    > set FLASK_ENV=development
    > flask init-db
    > flask run
    
Application will be served on http://127.0.0.1:5000/.

#### Additional Setup

The application currently uses Alpha Vantage for retrieving stock data but another API or web scraper should be implemented in the future.

You'll see API calls to Alpha Vantage in **static/scripts/getStockInfo.js**. To use the script, get an API key from https://www.alphavantage.co/ and add it to the *ALPHAVANTAGE_API_KEY* variable.

**IMPORTANT** This is not a secure way to store API keys. Do not commit your API keys to Git.

### Todo

- Find different API or web straper to retrieve stock data (Alpha Vantage only allows 5 calls per minute / 500 calls per day)
- Implement secure method for storing ENV variables (API keys, etc.)
- Make modal or page template for buying and selling stocks
- Make formatting consistent for owned and unowned stocks
- Improve security.  Username and password are currently being passed as query params for the **register** and **login** endpoints 
