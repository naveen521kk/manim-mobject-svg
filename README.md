# manim-mobject-svg

Create SVG files from [VMobject](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html).

Install: `pip install manim-mobject-svg`

Here's an example of how to use this plugin:

```python
from manim import *
from manim_mobject_svg import *

a = Square(color=BLUE)
a.to_svg("square.svg")
```
This should create a file `square.svg` in the current directory and return the path to the file. The output should look like this:
![svg square manim](https://user-images.githubusercontent.com/49693820/214828793-bf764d46-93b2-4622-bd1e-c68c42206b46.svg)

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
![svg vgroup manim](https://user-images.githubusercontent.com/49693820/214829098-6680ca28-6f2b-4bb6-b376-f7858532c1c3.svg)
