from typing import Sequence, Iterable

from docarray.array.storage.base.getsetdel import BaseGetSetDelMixin
from docarray import Document
from docarray.array.storage.base.helper import Offset2ID

from .helper import (
    get_Document_from_pinecone_vector, 
    get_pinecone_vector_from_Document
)

class GetSetDelMixin(BaseGetSetDelMixin):
        
    def _get_doc_by_id(self, _id: str) -> Document:
        result = self.index.fetch([_id], namespace=self._config.namespace)
        pinecone_vector = result['vectors'][_id]
        document = get_Document_from_pinecone_vector(pinecone_vector)
        return document

    def _get_docs_by_ids(self, ids: Sequence[str]) -> Iterable['Document']:
        print('fetching')
        result = self.index.fetch([_ids], namespace=self._config.namespace)
        print('fetched')
        pinecone_vectors = result['vectors'].values()
        return (get_Document_from_pinecone_vector(v) for v in pinecone_vectors)

    def _del_doc_by_id(self, _id: str):
        return self.index.delete([_id], namespace=self._config.namespace)

    def _set_doc_by_id(self, _id: str, value: Document):
        pinecone_vector = get_pinecone_vector_from_Document(value)
        return self.index.upsert(
           [(_id, pinecone_vector[1], pinecone_vector[2])],
           namespace=self._config.namespace
        )

    def _load_offset2ids(self):
        self._offset2ids = Offset2ID([str(i) for i in range(len(self))])


    def _save_offset2ids(self):
        # to be implemented
        ...
