import os
from elasticsearch import Elasticsearch
from models import SearchResponse

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv(override=True)

# Initialize Elasticsearch client
es_client = Elasticsearch(
    [os.environ['ELASTICSEARCH_URL']],
    api_key=os.environ['ELASTICSEARCH_API_KEY'],
    verify_certs=False,
    request_timeout=360
)

def search(query: str) -> SearchResponse:
    search_query = {
        "size": 1,
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "body_content"]
            }
        }
    }

    response = es_client.search(index=os.environ['ELASTICSEARCH_INDEX'], body=search_query)

    if response['hits']['hits']:
        hit = response['hits']['hits'][0]
        doc_id = hit['_id']
        title = hit['_source'].get('title', 'No title')
        url = hit['_source'].get('url', 'No URL')
        body_content = hit['_source'].get('body_content', 'No content')
        page = str(hit['_source'].get('page', 'No page'))
        print(f"ID: {doc_id}, Title: {title}, URL: {url}, page: {page}")
        return SearchResponse(doc_id=doc_id, title=title, url=url, body_content=body_content, page=page)
    else:
        return SearchResponse()
