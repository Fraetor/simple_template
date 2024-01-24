"""Fills in placeholder values in a string or file.

Intended for HTML files. Simple substitution only, with an easy API
"""

import re


class TemplateError(KeyError):
    """Rendering a template failed."""


def render(template: str, strict=True, /, **variables) -> str:
    """Renders the template with the provided variables.

    The template should contain placeholders that will be replaced. These
    placeholders consist of language appropriate comments containing a dollar
    (`$`) prefixed name. The name of the placeholder should be a valid python
    identifier. Within the comment whitespace is ignored but there may be no
    other content. There must not be whitespace between the dollar and the name.

    The following placeholder styles are supported:

    HTML Style:
        <!-- $placeholder_name -->

    CSS/JS Style:
        /* $placeholder_name */

    Depending on the value of the strict argument, an exception might be raised
    if there are placeholders without corresponding values. It is acceptable to
    provide unused values; they will be ignored.

    Parameters
    ==========
    template: str
        Template to fill with variables.
    strict: bool, optional
        Disallow missing values for placeholders. If True an exception is raised
        if any placeholders are missing values, otherwise they are ignored.
        Defaults to True.

    **variables: Any
        Keyword arguments for the placeholder values. The argument name should
        be the same as the placeholder's name. You can unpack a dictionary of
        value with `render(template, **my_dict)`.

    Returns
    =======
    rendered_template: str
        Filled template.

    Raises
    ======
    TypeError
        If the template is not a string, or a variable cannot be casted to a
        string.
    TemplateError
        Value not given for a placeholder in the template in strict mode.

    Examples
    ========
    >>> template = "<p>Hello <!-- $myplaceholder -->!</p>"
    >>> simple_template.render(template, myplaceholder="World")
    "<p>Hello World!</p>"
    """

    def isidentifier(s: str):
        return s.isidentifier()

    def process_placeholder_style(template, pattern):
        def extract_placeholders():
            return filter(
                isidentifier, set(re.findall(pattern.format("[^$]*"), template))
            )

        def substitute_placeholder(name):
            try:
                value = variables[name]
            except KeyError as err:
                if strict:
                    raise TemplateError("Placeholder missing value", name) from err
            return re.sub(pattern.format(re.escape(name)), value, template)

        for name in extract_placeholders():
            template = substitute_placeholder(name)
        return template

    # Patterns with the placeholder name as `{0}`.
    html_pattern = r"<!--\s*\${0}\s*-->"
    js_pattern = r"/\*\s*\${0}\s*\*/"
    template = process_placeholder_style(template, html_pattern)
    template = process_placeholder_style(template, js_pattern)
    return template


def render_file(template_path: str, strict=True, /, **variables) -> str:
    """Render a template directly from a file.

    Otherwise the same as `simple_template.render()`.

    Examples
    ========
    >>> simple_template.render_file("/path/to/template.html", myplaceholder="World")
    "<p>Hello World!</p>"
    """
    with open(template_path, "rt", encoding="UTF-8") as fp:
        template = fp.read()
    return render(template, strict, **variables)
