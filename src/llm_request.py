if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv(override=True)

import os
import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

def llm_request(query):
    body = {
        "input": query,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "repetition_penalty": 1
        },
        "model_id": os.environ['WATSONX_AI_MODEL_ID'],
        "project_id": os.environ['WATSONX_AI_PROJECT_ID'],
        "moderations": {
            "hap": {
                "input": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                },
                "output": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                }
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['WATSONX_AI_ACCESS_TOKEN']}"
    }

    response = requests.post(
        os.environ['WATSONX_AI_API_URL'],
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    return data['results'][0]['generated_text']
