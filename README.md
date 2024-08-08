# Example Projects

Examples of langchain stuff

`rye sync` to get started

## Set up

#### Rye

Instructions to install rye: [rye website](https://rye.astral.sh/guide/installation/)

Run `rye sync` to get the virtualenv set up.

#### Justfile

There is a `.justfile` with common commands.  You can set up `just` on a mac with brew: `brew install just`.
For further reference: [just github](https://github.com/casey/just).

#### Llama3

The code uses `llama3` as the model.  Instructions for local set up is at:
[download ollama](https://ollama.com/download).

You can then run the model in a terminal tab with `ollama serve llama3`.
There are other commands that are helpful in the `.justfile`.

## Examples:

### Fake Data

Example of using an llm to create fake data based on a given data schema in a pydantic model.

[readme : fake data example](./support/readme_fake_data.md)

### Database

Example of using an llm to create descriptors of database tables.

[readme : database example](./support/readme_database.md)
