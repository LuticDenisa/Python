# xml element
def build_xml_element(tag, content, **attributes):
    opening_tag = f"<{tag}"
    for key, value in attributes.items():
        opening_tag += f' {key}="{value}"'
    opening_tag += ">"
    closing_tag = f"</{tag}>"
    xml = f"{opening_tag}{content}{closing_tag}"

    return xml


tag = "a"
content = "Hello there"
attributes = {
    "href": "http://python.org",
    "_class": "my-link",
    "id": "someid"
}
xml_element = build_xml_element(tag, content, **attributes)
print(xml_element)
