if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv(override=True)

import os
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes


# To display example params enter
GenParams().get_example_values()

generate_params = {
    GenParams.MAX_NEW_TOKENS: 900
}

llm = Model(
    model_id=ModelTypes.LLAMA_3_70B_INSTRUCT,
    params=generate_params,
    credentials=Credentials(
        api_key = os.environ['WATSONX_AI_API_KEY'],
        url = os.environ['WATSONX_AI_URL']
    ),
    project_id=os.environ['WATSONX_AI_PROJECT_ID']
)