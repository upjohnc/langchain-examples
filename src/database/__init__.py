from pprint import pprint

import click

from database import code


@click.command()
@click.option(
    "-r",
    "--response-type",
    type=click.Choice(
        ["json", "text"],
        case_sensitive=False,
    ),
    default="text",
)
@click.option("-t", "--table-name", default="Album")
def main(response_type, table_name):
    print("Running code")
    llm = code.get_llm()
    db = code.get_db()
    table_info = code.get_table_info(table_name, db)

    if response_type == "json":
        response = code.run_json_response(llm, table_info)
    else:
        response = code.run_text_response(llm, table_info)
    pprint(response)
    return 0
