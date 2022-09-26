import requests
cache = dict()

def get_article_from_server(url):
    print('Fetching article from server...')
    response = requests.get(url)
    return response.text
def get_article(url):
    print('Getting article...')
    if url not in cache:
        cache[url] == get_article_from_server(url)
        return cache[url]
get_article('https://s3.amazonaws.com/tcmg476/http_access_log')
get_article('https://s3.amazonaws.com/tcmg476/http_access_log')
print()
f['StartDate']
df['StartDate'] = pd.to_datetime(df['StartDate'])
least_recent_date = df['StartDate'].min()
most_recent_date = df['StartDate'].max()

