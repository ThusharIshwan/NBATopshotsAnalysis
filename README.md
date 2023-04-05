# NBA Topshots Analysis
Code needed for my analysis into the NBA Topshots Market


## Flow

The flow folder is an instance of the onflow/flow set to python

The protobuf files can be found here : https://github.com/onflow/flow
In order to generate the python files in flow follow the gRPC instructions : https://grpc.io/docs/languages/python/quickstart/

## scripts/collection

These use the above to scrape the data from the flow blockchain. Different events can be passed into the procedure in order to scrape from different projects.

## scripts/analysis/txn_transform
Transforms the data that was scraped into the daily data for the regression.

## regression
Uses R (lm/plm) to run the desired regressions.

## data/basketball_data.csv
The additional data is gathered from:
salary data -> Hoopshype (See scripts/collection/nba_scrape/nba_scrape.py)
Player Impact Estimate (PIE) data -> NBA Stats (See scripts/collection/nba_scrape/nba_scrape.py) (March 16th 2023)
Twitter Followers -> Gathered Manually (March 16th 2023)

## data/date_accumulated_edition_play_prices.csv
This is the final result for the data used in the regression analysis. It is acquired by using the methods in the collection folder to scrape the flow blockchain, and then transform that data by accumulating the transactions by date, play and edition.