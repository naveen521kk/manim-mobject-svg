# manim-mobject-svg

Create SVG files from [VMobject](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html) and [VGroup](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html).

Install: `pip install manim-mobject-svg`

Here's an example of how to use this plugin:

```python
from manim import *
from manim_mobject_svg import *

a = Square(color=BLUE)
a.to_svg("square.svg")
```
This should create a file `square.svg` in the current directory and return the path to the file. The output should look like this:

![svg square manim](https://github.com/naveen521kk/manim-mobject-svg/assets/49693820/ba232f4c-7a11-4d6f-b36e-7c49867bc6a8)

It's also possible to create a SVG file for VGroup.

```python
from manim import *
from manim_mobject_svg import *

a = Square(color=BLUE)
b = Circle(color=RED)
c = VGroup(a, b)
c.to_svg("group.svg")
```
It'll create a SVG file like this:

![svg vgroup manim](https://github.com/naveen521kk/manim-mobject-svg/assets/49693820/4073c65f-0397-450a-90d6-6a2226dade15)

## Parameters for `to_svg()`

`to_svg()` takes the following parameters:
- `path`: Path to the SVG file to be created. If not specified, it'll create a temporary file and return the path to the file.
- `crop`: Crop the SVG file to the bounding box of the VMobject. Default: `True`
- `padding`: Padding around the VMobject. Default: `0.5`

This method returns the path to the SVG file.
