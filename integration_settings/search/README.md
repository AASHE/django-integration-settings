# Shared AASHE Search Settings

## ElasticSearch

### Example

    from integration_settings.search.elasticsearch import *
    # you need to set your INDEX_NAME
    HAYSTACK_CONNECTIONS['default']['INDEX_NAME'] = 'documents'
