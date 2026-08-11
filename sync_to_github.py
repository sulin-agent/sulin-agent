# -*- coding: utf-8 -*-
"""
把当前文件夹里的代码同步到 GitHub（代替被代理阻断的 git push）。
用法：在本文件夹打开终端，运行  python sync_to_github.py
适用：你的网络代理会掐断 git 的原生 push，但放行 GitHub REST API。
"""
import os
import json
import base64
import urllib.request
import urllib.error

REPO = "sulin-agent/sulin-agent"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# token 优先级：环境变量 GITHUB_TOKEN > 同目录 .github_token 文件
def load_token():
    t = os.environ.get("GITHUB_TOKEN")
    if t:
        return t.strip()
    p = os.path.join(SCRIPT_DIR, ".github_token")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            return f.read().strip()
    raise SystemExit("找不到 token：请设置环境变量 GITHUB_TOKEN，或在脚本同目录放一个 .github_token 文件（只写一行 token）")

TOKEN = load_token()
PROXY = os.environ.get("HTTP_PROXY") or "http://127.0.0.1:61665/"
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))

# 这些不传：.git 目录、token 文件、缓存
SKIP = {".git", ".github_token", "__pycache__"}
SKIP_EXT = {".pyc"}


def api(method, path, body=None):
    url = "https://api.github.com" + path
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + TOKEN)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "wb-sync")
    if data:
        req.add_header("Content-Type", "application/json")
    return OPENER.open(req, timeout=30)


def upload(local_path, remote_name):
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode("ascii")
    sha = None
    try:
        r = api("GET", f"/repos/{REPO}/contents/{remote_name}")
        sha = json.loads(r.read())["sha"]
    except urllib.error.HTTPError:
        pass  # 文件不存在，首次创建
    body = {"message": f"sync: update {remote_name}", "content": content}
    if sha:
        body["sha"] = sha
    api("PUT", f"/repos/{REPO}/contents/{remote_name}", body)


def main():
    files = []
    for name in sorted(os.listdir(SCRIPT_DIR)):
        full = os.path.join(SCRIPT_DIR, name)
        if not os.path.isfile(full):
            continue
        if name in SKIP or name.endswith(tuple(SKIP_EXT)):
            continue
        files.append((full, name))
    print(f"同步 {len(files)} 个文件到 github.com/{REPO} ...")
    ok = 0
    for full, name in files:
        try:
            upload(full, name)
            print("  [OK]  ", name)
            ok += 1
        except urllib.error.HTTPError as e:
            print("  [ERR] ", name, e.code, e.read().decode("utf-8")[:150])
    print(f"完成 {ok}/{len(files)}。打开 https://github.com/{REPO} 查看。")


if __name__ == "__main__":
    main()
