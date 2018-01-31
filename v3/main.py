import json
from html import escape

def processNode(node, data):
    s = "<%s " % node["type"]
    num_attrs = 0
    for a in node["attributes"]:
        num_attrs += 1
        s += a["attr_name"]
        s += "=\"%s\"" % a["attr_data"]
        try:
            if node["attributes"][num_attrs]:
                s += " "
        except:
            s += ">"
            s += data
            s += "</%s>" % node["type"]
    return s

def typicalProcessingOfJSON(node, data):
    if "attributes" in node.keys():
        return processNode(node, data)
    else:
        return "<%s>%s</%s>" % (node["type"], data, node["type"])

def compile2html(s):
    page = json.loads(s)
    html = ""
    for i in page["body"]:
        if i["type"] in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            html += typicalProcessingOfJSON(i, escape(i["body"]))

        elif i["type"] == "br":
            html += "<br>"

        elif i["type"] == "div":
            html += typicalProcessingOfJSON(i, compile2html(json.dumps(i)))

        elif i["type"] == "p":
            html += typicalProcessingOfJSON(i, escape(i["body"]))

        elif i["type"] == "img":
            if i["alt"]:
                html += "<img src=\"%s\" alt=\"%s\">" % (i["src"], i["alt"])
            else:
                html += "<img src=\"%s\">" % i["src"]
    return html