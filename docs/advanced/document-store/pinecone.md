# Pinecone

[Pinecone](https://www.pinecone.io/docs/) can be used as a document store for DocumentArray. It is useful when one wants to have faster Document retrieval on embeddings, i.e. `.match()`, `.find()`. Pinecone makes it easy to build high-performance vector search applications. It’s a managed, cloud-native vector database with a simple API and no infrastructure hassles.

````{tip}
This feature requires `pinecone-client` and an api key. You can install it via `pip install "docarray[pinecone]"`, and get your key at https://www.pinecone.io/start/.
````

## Usage

One can instantiate a DocumentArray with Pinecone storage like so:

```python
from docarray import DocumentArray

da = DocumentArray(
    storage='pinecone', 
    config=dict(
        init_api_key=os.getenv('PINECONE_EXAMPLE_API_KEY'),
        index_name='jina-example',
        index_metric='cosine',
        index_type='approximated',
        index_dimension=768
    )
)
```

Note that specifying the `n_dim` is mandatory before using `Annlite` as a backend for DocumentArray.

Other functions behave the same as in-memory DocumentArray.

## Config

Many config options can be set, but the primary ones to consider are:

| Name                | Description                                                                     | Default                     |
|---------------------|---------------------------------------------------------------------------------|-----------------------------|
| `n_dim`             | Number of dimensions of embeddings to be stored and retrieved                   | **This is always required** |
| `data_path`         | The data folder where the data is located                                       | **A random temp folder**    |
| `metric`            | Distance metric to be used during search. Can be 'cosine', 'dot' or 'euclidean' | 'cosine'                    |

## Support

If there are any Pinecone specific questions, we e




    init_api_key: str = None
    init_host: str = None
    init_environment: str = None
    init_project_name: str = None
    init_log_level: str = None
    init_openapi_config: pinecone.core.client.configuration.Configuration = None
    init_config: str = '~/.pinecone'
    index_name: str = 'jina-example'
    index_dimension: int = 8
    index_timeout: int = None
    index_type: str = "approximated"
    index_metric: str = "cosine"
    index_replicas: int = 1
    index_shards: int = 1
    index_pods: int = 1
    index_pod_type: str = 'p1'
    index_index_config: dict = None
    namespace: str = ''

