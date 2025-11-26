"""lambda.py"""


def test_kwargs(method, url, **kwargs):
    """_summary_"""
    print(f"method: {method}")
    print(f"url: {url}")
    print(f"kwargs: {kwargs}")


test_kwargs(
    "get",
    "http://hogehoge",
    params={"param": 1},
    headers=[{"bbb": 2}, {"bbb": 2}],
    abcd=2,
)
