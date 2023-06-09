from manim import VMobject, VGroup
from .svg import *

__all__ = ["create_svg_from_vgroup", "create_svg_from_vmobject"]

VMobject.to_svg = create_svg_from_vmobject
VGroup.to_svg = create_svg_from_vgroup

# Set rich display for manim objects on Jupyter
VMobject._repr_svg_ = lambda self: create_svg_from_vmobject(self).read_text()
VGroup._repr_svg_ = lambda self: create_svg_from_vgroup(self).read_text()
