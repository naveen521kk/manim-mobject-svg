from manim import VMobject, VGroup
from .svg import *

__all__ = ["create_svg_from_vgroup", "create_svg_from_vmobject"]

VMobject.to_svg = create_svg_from_vmobject
VGroup.to_svg = create_svg_from_vgroup
