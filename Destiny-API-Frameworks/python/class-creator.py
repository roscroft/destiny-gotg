import json
import re
import requests

spc = "    "
api_headers_public = '{\"X-API-Key\": api_key, \"Origin\": origin_header}'
api_headers_private = '{\"X-API-Key\": api_key, \"Origin\": origin_header, \"Authorisation: Bearer:\": access_token}'
request_session = requests.session()
first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def convert(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def get_scrape():
    url = "https://destinydevs.github.io/BungieNetPlatform/data/api-data.json"
    r = request_session.get(url, headers='')
    scrape = r.json()
    return scrape


# Method: GET
"""

:param param2: 
:type param2: 
:param param1: 
:type param1: 
:return: 
:rtype: 
"""


scrape = get_scrape()
c = open("endpoints.py", "w+")
class_import = "import requests\n\n"
class_import += "api_key = \"<your api key here>\"\n"
class_import += "origin_header = \"<your origin header here>\"\n"
class_import += 'api_headers_public = {\"X-API-Key\": api_key, \"Origin\": origin_header}\n'
class_import += 'api_headers_private = {\"X-API-Key\": api_key, \"Origin\": origin_header, \"Authorization: Bearer\": access_token}\n'
# class_import += "request_session = requests.session()\n"
c.write(class_import)
for category in scrape:
    class_header = "\n\nclass "+category+"(object):\n"
    class_header += spc+"def __init__(self):\n"
    class_header += spc+spc+"pass\n"
    c.write(class_header)
    for module in scrape[category]:
        if module['name'].find("-"):
            sep = '-'
            this_name = module['name'].split(sep, 1)[0]
        else:
            this_name = module['name'].lower()
        this_name = convert(this_name)
        if category == "DestinyService":
            this_url = "https://www.bungie.net/d1/Platform"+module['endpoint']
        else:
            this_url = "https://www.bungie.net/Platform" + module['endpoint']
        this_param = ""
        this_docstring = '\"\"\"See https://destinydevs.github.io/BungieNetPlatform/docs/'+category+'/'+module['name']+'\n'
        this_docstring += spc + spc + 'Access: ' + module['access']+'  Method: ' + module['method'] + '\n'
        if module['method'] == "POST":
            this_param += ", access_token"
            this_headers = 'api_headers_private'
        else:
            this_headers = 'api_headers_public'
        for each in module['path']:
            this_variable = "{"+each+"}"
            if this_variable in this_url:
                this_param += ", "+each
                this_regex = r"(\{" + re.escape(each) + r"\})"
                this_url = re.sub(this_regex, '\" + '+each+' + \"', this_url)
                this_docstring += spc + spc + ':param ' + each + ': ' + '\n'
        if len(module['post']) > 0:
            this_param += ", **kwargs"
            this_url += '?**kwargs'
            this_docstring += spc + spc + 'KWARGS values should be \"param=value\"\n'
        for each in module['post']:
            # this_variable = "{" + each + "}"
            # if this_variable in this_url:
            this_docstring += spc + spc + ':param ' + each + ': ' + '\n'
        this_docstring += spc + spc + ':return: Returns JSON\n'
        this_docstring += spc + spc + ':rtype: Dict\n'
        this_docstring += spc + spc + '\"\"\"\n'
        this_function = ("\n" + spc + "def " + this_name + "(self" + this_param + "):\n"
                         + spc + spc + this_docstring
                         + spc + spc + "request_session = requests.session()\n"
                         + spc + spc + "url = \"" + this_url + "\"\n"
                         + spc + spc + "r = request_session.get(url, headers="+this_headers+")\n"
                         + spc + spc + "this_json = r.json()\n"
                         + spc + spc + "return this_json\n")
        c.write(this_function)

c.close()
