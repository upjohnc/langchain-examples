from langchain.output_parsers import PydanticOutputParser
from langchain_community.llms import Ollama
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, FewShotPromptTemplate, PromptTemplate
from langchain_experimental.tabular_synthetic_data.base import SyntheticDataGenerator
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)
from pydantic import BaseModel, Field

from fake_data.const import MODEL


class Actor(BaseModel):
    name: str = Field(description="name of actor")
    gender: str = Field(description="gender of actor")
    height: float = Field(description="height of actor in feet")


class AllActors(BaseModel):
    all: list[Actor] = Field(description="list of actors")


# todo: turn into a pydantic_object and then spit out the json
examples = [
    {"example": "name: Jonah Hill, gender: male, height: 5.02"},
    {"example": "name: Julia Roberts, gender: female, height: 5.89"},
    {"example": "name: Mel Gibson, gender: male, height: 6.03, eye_color: blue"},
]


def main_code() -> int:
    llm = Ollama(model=MODEL)

    # parser = PydanticOutputParser(pydantic_object=AllActors)
    parser = JsonOutputParser(pydantic_object=Actor)
    template = PromptTemplate(input_variables=["example"], template="{example}")

    prompt_template = FewShotPromptTemplate(
        prefix=SYNTHETIC_FEW_SHOT_PREFIX,
        examples=examples,
        suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
        input_variables=["subject", "extra"],
        example_prompt=template,
    )

    llm_chain = prompt_template | llm | parser

    end = []
    min_total_examples = 9

    # negative downside: it will repeat names
    while len(end) < min_total_examples:
        result = llm_chain.invoke(
            {
                "subject": "personal information",
                "extra": (
                    "Create examples in a json format"
                    f" from this json schema : {parser.get_format_instructions()}"
                ),
            }
        )
        # sometimes returns only one result, so it isn't in a list
        if isinstance(result, dict):
            result = [result]
        end.extend(result)
    print(end)
    print(len(end))

    t = [Actor.model_validate(i) for i in end]
    print(t)

    return 0
