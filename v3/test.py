from main import compile2html
import json
with open("case.json") as a:
    b = json.loads(json.dumps(a.read()))
    c = compile2html(b)
    d = "<h1>Hello, world!</h1><p>It works! FANTASTIC!</p><div class=\"container\"><p>lorem ipsum</p><p>I am running out of dummy phrases.</p></div>"
    if c != d:
        print("test failed: \"%s\" != \"%s\"" % (c, d))
    else:
        print("test succeeded")
