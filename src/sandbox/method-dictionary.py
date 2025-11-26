"""dictionary method"""

q = {
    "log_level": "ERROR",
    "uuid": "d41600a4-bf46-41a9-9823-bc33efe01bb0",
    "message": "メッセージ",
    "request_method": "GET",
    "request_uri": "/api/v1/tests/exception",
    "proc_time": "0.0015",
    "request_headers": {
        "host": "api.dev.ppol.adglobe-test.com",
        "x-forwarded-for": "118.238.237.233, 10.101.12.119",
        "connection": "close",
        "x-forwarded-proto": "https",
        "x-forwarded-port": "443",
        "x-amzn-trace-id": "Root=1-65a10df4-1f1f3cb61f9bba16443aa970",
        "cache-control": "max-age=0",
        "authorization": "Basic cGVwcG9sOiFoZTc4a3Qxalla",
        "sec-ch-ua": "Not_A Brand;v=8,Chromium;v=120,Google Chrome;v=120",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ja,en-US;q=0.9,en;q=0.8",
    },
    "request_body": None,
    "response_headers": None,
    "response_body": None,
    "traceback": [
        "line 35, in run_in_threadpool",
        "    return await anyio.to_thread.run_sync(func, *args)",
        "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
        "  File /usr/local/lib/python3.11/site-packages/anyio/to_thread.py, line 56, in run_sync",
        "    return await get_async_backend().run_sync_in_worker_thread(",
        "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
        "  File /usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py, line 2134, in run_sync_in_worker_thread",
        "    return await future",
        "           ^^^^^^^^^^^^",
        "  File /usr/local/lib/python3.11/site-packages/anyio/_backends/_asyncio.py, line 851, in run",
        "    result = context.run(func, *args)",
        "             ^^^^^^^^^^^^^^^^^^^^^^^^",
        "  File /app/api/v1/routers/tests.py, line 55, in test_exception",
        "    raise PeppolHttpException(",
        "exceptions.peppol_http_exception.PeppolHttpException",
    ],
    "http_status": 444,
    "remote_addr": "10.101.12.119",
    "request_date": "2024-01-12 19:01:24",
    "extra": {
        "request_params": {
            "peppol_api_id": "11",
            "peppol_password": "22",
            "authentication_key": "33",
            "status": "02",
            "gettime_from": "2022-01-01",
            "gettime_to": "2022-01-02",
        }
    },
}

# p = q["extra"]["request_params_"]["peppol_api_id"]
# if p is None:
#     print("request_params is None")
# else:
#     print(f"request_params is{p}")

test = {}

if test:
    print("AAAAAA----")
else:
    print("BBBB")

# def print_dict(prefix: str, data=None) -> None:
#     """出力"""
#     print("\n{}: {}".format(prefix, data))


# print_dict("A get → ", q.get("log_level__"))

# print_dict("A_2 get → ", q["log_level"])

# print_dict(
#     "B pop → %s"
#     % ((lambda q: [cloned := q.copy(), cloned.pop("request_headers")])(q)[1])
# )

# print_dict("C copy → %s", q.copy())

# print_dict("D clear → %s" % ((lambda q: [cloned := q.copy(), cloned.clear()])(q)[1]))

# print_dict("E items  ", q.items())

# print_dict("F values ", q.values())

# print_dict("G update → %s" % ((lambda q: q.update({"NAME": "hoge"}) or q)(q)))

# print_dict("H setdefault → ", ((lambda q: [q.setdefault("NAME", "apple"), q])(q)[1]))

# print_dict("I popitem → ", ((lambda q: [q.popitem(), q])(q)[1]))

# print_dict("J keys →", q.keys())

# print_dict(
#     "J fromkeys →",
#     q.fromkeys([5, 10, 5, 10, 2, 1, 3, 4, 6], ["田中"]),
# )

# user_info = {}
# company_info = {}
# user_info["userId"] = 1
# user_info["lastName"] = 2
# user_info["firstName"] = 3
# user_info["esCompanyId"] = 4
# company_info["peppolId"] = 5


# # print_dict("K user_info →", **user_info)

# test = {**user_info, **company_info, "test": "test"}
# print("AAA-", test)
