import warnings
import copy
from typing import (
    Optional,
    TYPE_CHECKING,
    Union,
    Dict
)
from textwrap import dedent

from dataclasses import dataclass

import pinecone

from docarray.array.storage.base.backend import BaseBackendMixin
from docarray.helper import dataclass_from_dict

from .helper import get_kwargs_from_config

if TYPE_CHECKING:
    from docarray.types import (
        DocumentArraySourceType,
    )


@dataclass
class PineconeConfig:
    """
    Using Pinecone, in order to start working with vectors in a namespace,
    configuration details need to be provided at the connection level and
    the index-and-below level. For more information on these options, 
    see the signatures of `pinecone.init` and `pinecone.create_index`.
    """
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


class BackendMixin(BaseBackendMixin):
    
    def _init_storage(
        self, 
            _docs: Optional['DocumentArraySourceType'] = None, 
            config: Optional[Union[PineconeConfig, Dict]] = None,
            **kwargs
    ):
        """Initialize Pinecone client and instantiate pinecone.Index."""

        config = copy.deepcopy(config)
        if not config:
            raise ValueError('Empty config is not allowed for Pinecone storage')
        elif isinstance(config, dict):
            config = dataclass_from_dict(PineconeConfig, config)

        init_kwargs = get_kwargs_from_config(config, 'init')
        pinecone.init(**init_kwargs)
        if config.index_name not in pinecone.list_indexes():
            index_kwargs = get_kwargs_from_config(config, 'index')
            pinecone.create_index(**index_kwargs)
            self.index = pinecone.Index(config.index_name)
        else:
            self.index = pinecone.Index(config.index_name)
            self.validate_index_configuration(config)

        self._config = config
        super()._init_storage(_docs, config, **kwargs)
    
    def get_index_meta(self):
        return self.index.describe_index_stats()

    def get_namespace_meta(self):
        index_meta = self.get_index_meta()
        namespaces_meta = index_meta['namespaces']
        if not self._config.namespace in namespaces_meta:
            return None
        return namespaces_meta[self._config.namespace]

    def validate_index_configuration(self, config):
        """Raise exception if index and config possibly do not align.
        
        The latest version (2.0.8) of pinecone-client at the time of this 
        writing does not allow to programmatically lookup metric or 
        index_type, so the logic here will _only_ compare dimension
        """
        index_meta = self.get_index_meta()
        warnings.warn(dedent("""\
            Ensure that `metric` and `index_type` match desired configuration
            by accessing your index at https://app.pinecone.io 
            """).replace("\n", ''))
        index_dim = index_meta['dimension']
        config_dim = config.index_dimension
        if index_dim != config_dim and not config_dim: #in other words, None is OK
            raise ValueError(dedent(f"""\
                Dimension of index ({index_dim}) does not match up with 
                configuration dimension ({config_dim}) used to instantiate 
                DocumentArrayPinecone.""").replace('\n', ''))
