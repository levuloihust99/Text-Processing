import re
from lxml import html as html_parser, etree

tagRE = re.compile(
    r"(.*?)<(/?[a-zA-Z0-9]+)[^>]*>(?:([^<]*)(?:<(.*?)>)?)?(\s*)", re.DOTALL)
cmtRE = re.compile(r"(<!--.*?-->)", re.DOTALL)


def clean_html(text, remove_script: bool = True):
    if remove_script:
        text = do_remove_script(text)
    text = re.sub(r"<![Dd][Oo][Cc][Tt][Yy][Pp][Ee][^>]*>", "", text)
    text = cmtRE.sub("", text)
    text = tagRE.sub("\g<1> \g<3> \g<5>", text)
    return text


def do_remove_script(text):
    try:
        html = html_parser.fromstring(text)
        scripts = html.xpath(".//script")
        for script in scripts:
            script.getparent().remove(script)
        html_text = etree.tostring(html, encoding='unicode')
        return html_text
    except Exception as e:
        return text
