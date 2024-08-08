# Example Projects

Examples of langchain stuff

`rye sync` to get started

## Fake Data

`rye run fake-data`

Notes about duplicates because the llm can only give back
a few so you need to loop over the call to the llm

Code example: https://python.langchain.com/v0.1/docs/use_cases/data_generation/#quickstart
makes use of SyntheticDataGenerator and that loops through multiple calls
the result is potential duplicates
https://api.python.langchain.com/en/latest/tabular_synthetic_data/langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator.html#langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator
https://python.langchain.com/v0.1/docs/use_cases/data_generation/#5-generate-synthetic-data

## Database

Example of using an llm to create descriptors of database tables.

[readme : database example](./support/readme_database.md)
