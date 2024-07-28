import functools
from collections import OrderedDict

import requests


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache.move_to_end(cache_key, last=True)
                cache_item = deco._cache[cache_key]
                cache_item['frequently'] += 1
                return cache_item['result']
            new_cache_item = {'result': f(*args, **kwargs), 'frequently': 1}
            if len(deco._cache) >= max_limit:
                lfu_item = min(deco._cache.items(), key=lambda x: x[1]['frequently'])
                del deco._cache[lfu_item[0]]
            deco._cache[cache_key] = new_cache_item
            return new_cache_item['result']

        deco._cache = OrderedDict()
        return deco

    return internal


@cache(max_limit=2)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

# Test
fetch_url('http://www.python.org/', first_n=5)
fetch_url('http://www.python.org/', first_n=5)
fetch_url('http://www.python.org/', first_n=5)
fetch_url('http://www.google.com/', first_n=5)
fetch_url('http://www.python.org/', first_n=5)
fetch_url('http://www.google.com/', first_n=5)
fetch_url('http://www.google.com/', first_n=5)
fetch_url('http://www.google.com/', first_n=5)
fetch_url('http://www.php.com/', first_n=5)
fetch_url('http://www.php.com/', first_n=5)
fetch_url('http://www.php.com/', first_n=5)
fetch_url('http://www.php.com/', first_n=5)
fetch_url('http://www.php.com/', first_n=5)
fetch_url('http://www.google.com/', first_n=5)
fetch_url('http://www.python.org/', first_n=5)
