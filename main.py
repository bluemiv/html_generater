# -*- coding: utf-8 -*-
import os
import json


BASE_DIR_PATH = os.path.dirname(__file__)
RESOURCES_DIR_PATH = os.path.join(BASE_DIR_PATH, "resources")
RESULT_DIR_PATH = os.path.join(BASE_DIR_PATH, "result")


with open(os.path.join(BASE_DIR_PATH, "values.json"), "r") as f:
    value = json.loads(f.read())


def get_html(layout_name):
    with open(os.path.join(RESOURCES_DIR_PATH, layout_name), "r") as f:
        return f.read()


if __name__ == "__main__":
    print("check variable")
    assert os.path.exists(BASE_DIR_PATH), "Unexpected error. {}".format(BASE_DIR_PATH)
    assert os.path.exists(RESOURCES_DIR_PATH), "Resource is required. {}".format(RESOURCES_DIR_PATH)
    
    if not os.path.exists(RESULT_DIR_PATH):
        print("make result directories")
        os.makedirs(RESULT_DIR_PATH)

    html = get_html("index.html")

    for k, v in value.items():
        print("replace '{}'".format(k))
        html = html.replace(v["html"], v["python"])

    
    with open(os.path.join(RESULT_DIR_PATH, "index.html"), "w") as f:
        f.write(html)