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