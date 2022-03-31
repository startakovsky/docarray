"""This is the helper module for DocumentArrayPinecone modules."""

from dataclasses import asdict

from docarray import Document

def get_kwargs_from_config(pinecone_config, kwarg_type):
    """Return kwargs to generate associated config."""
    kwargs = dict()
    prefix_length = len(kwarg_type) + 1
    for k, v in asdict(pinecone_config).items():
        if not k.startswith(kwarg_type):
            continue
        kwargs[k[prefix_length:]] = v
    if kwarg_type == 'index':
        kwargs['index_type'] = kwargs.pop('type')
    return kwargs


def get_pinecone_vector_from_Document(document):
    return (document.id, document.embedding, document.text)


def get_Document_from_pinecone_vector(pinecone_vector):
    id = pinecone_vector['id']
    text = pinecone_vector.get('metadata', '{}')
    embedding = pinecone_vector['values']
    return Document(id=id, text=text, embedding=embedding)
