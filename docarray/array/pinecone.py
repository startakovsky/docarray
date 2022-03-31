from .document import DocumentArray
from .storage.pinecone import StorageMixins, PineconeConfig

__all__ = ['DocumentArrayPinecone', 'PineconeConfig']


class DocumentArrayPinecone(StorageMixins, DocumentArray):
    """This is a :class:`DocumentArray` that uses Pinecone as
    vector search engine and storage.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
