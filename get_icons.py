#!/usr/bin/env python3

import urllib.request
import sys
import re

def get_code(icon):
    url = "http://fortawesome.github.io/Font-Awesome/icon/" + icon
    req = urllib.request.Request(url);
    html = str(urllib.request.urlopen(req).read())
    off = html.find("Unicode: <span class=\"upper\">")
    return html[off+29:off+33]

def camel_case(name):
    ret = name.replace('-', ' ')
    ret = ret.title()
    ret = ret.replace(' ', '')
    return ret

def get_icons():
    ret = []
    url = "http://fortawesome.github.io/Font-Awesome/icons/"
    req = urllib.request.Request(url);
    html = str(urllib.request.urlopen(req).read())
    ic = re.finditer('<a href=\"../icon/[^\"]*\"><i class=\"fa fa-([^<]*)<', html)
    for x in ic:
        sub = html[x.start():x.end()]
        it = re.search('class=\"fa [^>]*>', sub)
        name = sub[it.start() + 13 : it.end() - 2]
        it = re.search('../icon/[^\"]*\"', sub)
        icon = sub[it.start() + 8 : it.end() - 1]
        tex_name = camel_case(name)
        print("Retrieve: " + name + " (" + icon + ")")
        code = get_code(icon)
        ret.append((name, tex_name, icon, code))
    return ret

def gen_sty(icons):
    f = open('out.sty', 'w')
    for ic in icons:
        f.write(("\expandafter\def\csname faicon@" + ic[0] + " \endcsname").ljust(63)
                + ("{\symbol{\"" + ic[3] + "}}  \\def\\fa" + ic[1]).ljust(44)
                + " {{\FA\csname faicon@" + ic[0] + "\endcsname}}\n")
    f.close()

def gen_tex(icons):
    f = open('out.tex', 'w')
    for ic in icons:
        f.write("\showcaseicon{" + ic[0] + "}{fa" + ic[1] + "}")
        if ic[0] == ic[2]:
            f.write("{alias}")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    icons = get_icons()
    gen_sty(icons)
    gen_tex(icons)
