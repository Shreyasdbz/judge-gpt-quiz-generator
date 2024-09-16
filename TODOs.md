# TODOs for the project

## Generation

[ ] Generate content based on the headline and context via different models
[ ] Generate translations for each headline using the most optimized model
[ ] Add better safeguards and fine tune prompting to get better results

## Storage

[ ] Establish connection to Azure CosmosDb for MongoDb database
[ ] Store generated articles as wells retrieve for generating new headlines

## Migraiton

[ ] Migrate over existing list of "Fragments" or articles that have already been generated in the old database
[ ] Use the fragments as context or headlines to re-generate headlines to maintain similarity

## Sanitazation

[ ] Clean up all generated articles texts eg. removing trailing white spaces, random capitalizations, etc
