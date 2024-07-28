import psutil
import functools
import requests


def memory_usage(f):
    @functools.wraps(f)
    def internal(*args, **kwargs):
        process = psutil.Process()
        start_memory_usage = process.memory_info().rss
        result = f(*args, **kwargs)
        end_memory_usage = process.memory_info().rss
        print(f"Memory usage: {(end_memory_usage - start_memory_usage) / (1024 * 1024)} MB")
        return result

    return internal


@memory_usage
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('http://www.python.org/')
