# ETL_recipes
ETL on two datasets of food recipes taken from Edamam and Spoonacular. This transforms and matches data recipes by titles and ingredients names only. MongoDB must be installed (with default mongo configurations &lt; localhost, 2700>)

## Sprint 5: to get ETL and recommender done, just run run.py

## Sprint 4: Load ready data
Navigate to where allrecipes.bson is located or change the path accordingly ``` /path/to/allrecipes.bson ```

```
# change dbname to yours
mongorestore --db dbname allrecipes.bson
```
