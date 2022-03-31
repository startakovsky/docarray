from typing import MutableSequence, Iterable, Iterator, Union
from docarray import Document
from docarray.array.storage.base.seqlike import BaseSequenceLikeMixin

class SequenceLikeMixin(BaseSequenceLikeMixin):

    def __eq__(self, other):
        return self.config == other.config

    def __contains__(self, x: Union[str, 'Document']):
        if self.index.fetch([x.id])['vectors']:
           return True
        return False
    
    def __repr__(self):
        return f'<DocumentArray[Pinecone] (length={len(self)}) at {id(self)}>'

    # def insert(self, index: int, value: 'Document'):
    #     # Optional. By default, this will add a new item and update offset2id
    #     # if you want to customize this, make sure to handle offset2id
    #     ...

    # def append(self, value: 'Document'):
    #     # Optional. If you have better implementation than `insert`
    #     ...

    # def extend(self, values: Iterable['Document']) -> None:
    #     # Optional. If you have better implementation than `insert` one by one
    #     ...

    def __len__(self):
        namespace_meta = self.get_namespace_meta()
        if not namespace_meta:
            return 0
        return namespace_meta['vector_count']

    # def __iter__(self) -> Iterator['Document']:
    #     # Optional. By default, this will rely on offset2id to iterate
    #     ...
