import json
def compile2html(s):
    page = json.loads(s)
    html = ""
    for i in page["body"]:
        if i["type"] in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            h = i["type"]
            if i["attributes"]:
                s = "<%s " % h
                num_attrs = 0
                for a in i["attributes"]:
                    num_attrs += 1
                    s += a["attr_name"]
                    s += "=\"%s\"" % a["attr_data"]
                    try:
                        if i["attributes"][num_attrs]:
                            s += " "
                    except:
                        s += ">"
                s += i["body"]
                s += "</%s>" % h
                html += s
            else:
                html += "<h1>%s</h1>" % i["body"]
        elif i["type"] == "br":
            html += "<br>"
        elif i["type"] == "div":
            body = compile2html(json.dumps(i))
            if i["attributes"]:
                s = "<div "
                num_attrs = 0
                for a in i["attributes"]:
                    num_attrs += 1
                    s += a["attr_name"]
                    s += "=\"%s\"" % a["attr_data"]
                    try:
                        if i["attributes"][num_attrs]:
                            s += " "
                    except:
                        s += ">"
                s += body
                s += "</div>"
                html += s
            else:
                html += "<div>%s</div>" % body
        elif i["type"] == "p":
            if i["attributes"]:
                s = "<p "
                num_attrs = 0
                for a in i["attributes"]:
                    num_attrs += 1
                    s += a["attr_name"]
                    s += "=\"%s\"" % a["attr_data"]
                    try:
                        if i["attributes"][num_attrs]:
                            s += " "
                    except:
                        s += ">"
                s += "%s</p>" % i["body"]
                html += s
            else:
                html += "<p>%s</p>" % i["body"]
        elif i["type"] == "img":
            if i["alt"]:
                html += "<img src=\"%s\" alt=\"%s\">" % (i["src"], i["alt"])
            else:
                html += "<img src=\"%s\">" % i["src"]
    return html