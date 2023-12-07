class Solution:
    def entityParser(self, text: str) -> str:
        text = text.replace("&quot;",  "\"")
        text = text.replace("&apos;",  "'")
        # handle &amp; at the end to avoid problems with single "&"
        text = text.replace("&gt;",    ">")
        text = text.replace("&lt;",    "<")
        text = text.replace("&frasl;", "/")
        text = text.replace("&amp;",   "&")
        return text
