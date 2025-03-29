import httpx

text = "你好" * 1024 * 512  # 约 2MB+
print(f"请求文本长度：{len(text)} 字符")

try:
    resp = httpx.post(
        "http://192.168.3.83:8081/embed",  # 或反代地址
        headers={"Content-Type": "application/json"},
        json={"inputs": [text]},
        timeout=60
    )
    print(f"状态码：{resp.status_code}")
    print(resp.text[:500])
except Exception as e:
    print(f"请求失败：{e}")
