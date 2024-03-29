# simple_template

A templating library for simple placeholder filling. Useful when the full might
of [Jinja](https://palletsprojects.com/p/jinja/) and friends is unnecessary.

## Installation

simple_template can be installed from
[PyPI](https://pypi.org/project/simple_template/) or
[conda-forge](https://anaconda.org/conda-forge/simple_template).

### Install from PyPI

```sh
pip install simple_template
```

### Install from conda-forge

```sh
conda install -c conda-forge simple_template
```

## Usage

Usage information can be found by running `help(simple_template)`.

```manpage
Help on module simple_template:

NAME
    simple_template - Fills in placeholder values in a string or file.

DESCRIPTION
    Intended for HTML files. Simple substitution only, with an easy API

CLASSES
    class TemplateError(builtins.KeyError)
        Rendering a template failed due a placeholder without a value.

FUNCTIONS
    render(template: str, /, **variables) -> str
        Render the template with the provided variables.

        The template should contain placeholders that will be replaced. These
        placeholders consist of the placeholder name within double curly braces. The
        name of the placeholder should be a valid python identifier. Whitespace
        between the braces and the name is ignored. E.g.: `{{ placeholder_name }}`

        An exception will be raised if there are placeholders without corresponding
        values. It is acceptable to provide unused values; they will be ignored.

        Parameters
        ----------
        template: str
            Template to fill with variables.

        **variables: Any
            Keyword arguments for the placeholder values. The argument name should
            be the same as the placeholder's name. You can unpack a dictionary of
            value with `render(template, **my_dict)`.

        Returns
        -------
        rendered_template: str
            Filled template.

        Raises
        ------
        TemplateError
            Value not given for a placeholder in the template.
        TypeError
            If the template is not a string, or a variable cannot be casted to a
            string.

        Examples
        --------
        >>> template = "<p>Hello {{myplaceholder}}!</p>"
        >>> simple_template.render(template, myplaceholder="World")
        "<p>Hello World!</p>"

    render_file(template_path: str, /, **variables) -> str
        Render a template directly from a file.

        Otherwise the same as `simple_template.render()`.

        Examples
        --------
        >>> simple_template.render_file("/path/to/template.html", myplaceholder="World")
        "<p>Hello World!</p>"
```

## Licence

simple_template is licenced under the BSD0 licence, so you can do whatever you
like with it. See the full licence text in the [LICENCE](LICENCE) file.
