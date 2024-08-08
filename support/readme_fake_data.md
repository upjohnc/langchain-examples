# Fake Data

Example of creating fake data from an llm.

The code makes use of a pydantic model to define the desired returned values and then allows the `FewShotPromptTemplate`
to build out the prompt that is passed to the llm.

## Running the code

run `rye run fake-data`


## Bases for this example

The code is based on a use case example in the langchain : [code example](https://python.langchain.com/v0.1/docs/use_cases/data_generation/#quickstart)

**Caveat**

The tutorial code makes use of SyntheticDataGenerator and that loops through multiple calls
of the llm chain.  The result is the potential for duplicates.

For reference the code for generating synthetic data is here:
[generate command on the SyntheticDataGenerator class](https://github.com/langchain-ai/langchain/blob/3da2713172e7cf5f526e33d595e95ed1f82e45e1/libs/experimental/langchain_experimental/tabular_synthetic_data/base.py#L98)
