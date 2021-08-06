# -*- coding: utf-8 -*-
import os
import json


BASE_DIR_PATH = os.path.dirname(__file__)
RESOURCES_DIR_PATH = os.path.join(BASE_DIR_PATH, "resources")
RESULT_DIR_PATH = os.path.join(BASE_DIR_PATH, "result")


def get_file(layout_name, json_value=False):
    with open(os.path.join(RESOURCES_DIR_PATH, layout_name), "r", encoding="utf-8") as f:
        if(json_value):
            return json.loads(f.read())
        return f.read()


def gen_breadcrumb():
    breadcrumb = get_file("breadcrumb.json", json_value=True)
    if breadcrumb["use"]:
        html = ''
        for item in breadcrumb["items"]:
            html += '<li><a href="{url}">{text}</a></li>\n'.format(**item)
        return html

def gen_emoji_container():
    breadcrumb = get_file("emoji_container.json", json_value=True)
    if breadcrumb["use"]:
        html = ''
        for item in breadcrumb["items"]:
            html += '<li><a href="{url}">{text}</a></li>\n'.format(**item)
        return html

if __name__ == "__main__":
    print("check variable")
    assert os.path.exists(BASE_DIR_PATH), "Unexpected error. {}".format(BASE_DIR_PATH)
    assert os.path.exists(RESOURCES_DIR_PATH), "Resource is required. {}".format(RESOURCES_DIR_PATH)
    
    if not os.path.exists(RESULT_DIR_PATH):
        print("make result directories")
        os.makedirs(RESULT_DIR_PATH)

    value = get_file("values.json", json_value=True)
    html = get_file("index.html")
    css = get_file("index.css")

    html = html.replace("[##_breadcrumb_##]", gen_breadcrumb())

    for k, v in value.items():
        print("replace '{}'".format(k))
        html = html.replace(v["html"], v["python"])
        css = css.replace(v["html"], v["python"])

    with open(os.path.join(RESULT_DIR_PATH, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    with open(os.path.join(RESULT_DIR_PATH, "index.css"), "w", encoding="utf-8") as f:
        f.write(css)