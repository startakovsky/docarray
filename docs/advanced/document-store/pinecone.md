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

Many config options have been implemented, but the primary ones to consider are:

| Name              | Description                                                                                       | Default                     |
|-------------------|---------------------------------------------------------------------------------------------------|-----------------------------|
| `init_api_key`    | Pinecone API key available at https://www.pinecone.io/start.                                      | **This is always required** |
| `index_name`      | The name of the Pinecone Index. Read more [here](https://www.pinecone.io/docs/manage-indexes/).   | **This is always required** |
| `index_dimension` | A positive integer representing the dimension; Pinecone supports up to 20,000                     | **This is always required** |
| `index_metric`    | Distance metric to be used during search. Can be 'cosine', 'dotproduct' or 'euclidean'            | 'cosine'                    |
| `index_type`      | The computation of the distance metric can either be 'approximated' or 'exact'.                   | ''approximated'             |
| `namespace`       | Each DocumentArray consists of exactly one [namespace](https://www.pinecone.io/docs/namespaces/). | 'jira-example'              |

## Support

If there are any Pinecone specific questions or clarifications sought, go to the Pinecone [Community Page](https://www.pinecone.io/community/).



