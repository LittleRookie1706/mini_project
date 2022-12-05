import meilisearch

client = meilisearch.Client('http://meilisearch:7700', 'masterKey')

news_index = client.index('news')
news_index.update_filterable_attributes(['tags',])