# Order Analytics Platform

This guide provides instructions on how to set up the application and run analytics quries on the logistics database. 

## Prerequisite
* [Docker](https://www.docker.com/products/docker-desktop/)
* [docker-compose](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/)

## Folder Structure
```
order_analytics_platform/
├── app/                 # Application source code
│   ├── queries/         # SQL query files
│   ├── config.py        # Database configuration
│   ├── db.py            # Database connection utilities
│   ├── export.py        # CSV export utilities
│   ├── query_runner.py  # Query execution logic
│   ├── main.py          # Entry point for the application
│   └── requirements.txt # Python dependencies
├── db-scripts/          # Scripts for setting up the database
├── docker/              # Docker-related files
│   ├── application/      # Dockerfile for the app
│   ├── postgres-db/     # Dockerfile for the database
├──  docker-compose.yml  # Docker Compose configuration
└── README.md            # Documentation
```

## Analytics Queries
The following analytics queries (app/quries/) have been prepared for convenience:
* query_open_orders.sql: Number of open orders by `DELIVERY_DATE` and `STATUS`
* query_delivery_dates_with_most_open_orders.sql: Top 3 delivery dates with more open orders
* query_pending_items_count.sql: Number of open pending items by `PRODUCT_ID`
* query_customers_with_most_pending_orders.sql: Top 3 Customers with more pending orders

## Steps to Run the Quries
### 1. Clone the Repository
> git clone <repo_url>
 
### 2. Start the Application and Database

Once you have [Docker](https://www.docker.com/products/docker-desktop/) and [docker-compose](https://docs.docker.com/compose/install/) configured in your computer, with your Docker engine running, you must execute the following command:
   > docker-compose up

The default query query_open_orders.sql will run and the output will be exported.

### 3. Run Quries

To run a specified query, you can easily pass in the arguments:
* `query_path`: the path to the query you would like to execute
* `--export`: the flag to indicate whether you want to export the output to a csv
* `--export-path`: the customized output path

For example

> docker compose run app queries/query_open_orders.sql

> docker compose run app --export --export-path /app/output.csv queries/query_delivery_dates_with_most_open_orders.sql


### Step 4: Clean Up
Stop and remove containers:
> docker compose down


## Future Enhancements:
### Tests
* Implement units tests for the application logic
* Include data tests for validating queries
### Automated code formatter
* Add CI pipeline to automate code quality check, code formatting etc..
### Change Data Capture
* Add functionality to track and store the query history to the database
### Container Communication
* Currently both app and database containers are spinned up simultaneously through `docker compose`. It would be more logical to spin them up seperately while allow commnucation with each other.

