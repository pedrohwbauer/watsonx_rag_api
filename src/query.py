if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv(override=True)

from models import Answer
from search import search
from llm import llm

def query(question: str) -> Answer:

    search_response = search(question)

    if(search_response.doc_id == None):
        return Answer(content='Nenhum documento encontrado')

    combined_input = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You always answer the questions with markdown formatting using GitHub syntax. The markdown formatting you support: headings, bold, italic, links, tables, lists, code blocks, and blockquotes. You must omit that you answer the questions with markdown.

Any HTML tags must be wrapped in block quotes, for example ```<html>```. You will be penalized for not rendering code in block quotes.

When returning code blocks, specify language.

You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don'\''t know the answer to a question, please don'\''t share false information.<|eot_id|><|start_header_id|>user<|end_header_id|>

Here is a document that might help answer the question: {question}

Document content:


{search_response.body_content}

Please provide an answer in the portuguese language based only on the provided document content. If the answer is not found in the document, respond with '\''Não sei a resposta'\''.<|eot_id|><|start_header_id|>assistant<|end_header_id|>
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""
    
    return Answer(
        content=llm.generate_text(prompt=combined_input),
        url=search_response.url,
        page=search_response.page
    )

    