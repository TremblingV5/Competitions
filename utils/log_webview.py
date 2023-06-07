from flask import Flask
from flask import request
from flask import send_file

import os


def find_logs(path) -> list:
    result = list()
    for item in os.listdir(path):
        if "venv" in item:
            continue
        if ".log" in item:
            result.append(os.path.join(path, item))
        elif "." in item:
            pass
        else:
            try:
                result += find_logs(os.path.join(path, item))
            except:
                pass
    return result

app = Flask("LogWebView")


@app.route("/list")
def listPage():
    abs_path = os.path.abspath("./")
    result = find_logs("./")

    return f"<div>当前绝对路径：{abs_path}</div>" + "".join([
        f"<a href='download?path={x}'>{x}</a><br>" for x in result
    ])


@app.route("/download")
def download_file():
    file_path = request.args.get("path")

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"Not found: {file_path}"

if __name__ == "__main__":
    app.run()