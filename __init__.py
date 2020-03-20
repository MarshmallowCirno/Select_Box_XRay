# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Box Select (X-Ray)",
    "author": "MarshmallowCirno",
    "version": (2, 0, 0),
    "blender": (2, 82, 0),
    "location": "Toolbar > Selection Tools",
    "description": "Select items using box selection. Upon selection temporary enable x-ray, hide mirror and solidify modifiers in edit mode",
    "warning": "Beta version",
    "category": "3D View",
    "wiki_url": "",
}


if "bpy" in locals():
    import importlib
    reloadable_modules = [
        "functions",
        "operators",
        "tools",
        "ui",
        "keymaps",
        "utils"
    ]
    for module in reloadable_modules:
        if module in locals():
            importlib.reload(locals()[module])
else:
    from . import operators, tools, ui, keymaps


import bpy


def register():
    operators.register()
    ui.register()
    tools.register()
    keymaps.register()


def unregister():
    operators.unregister()
    ui.unregister()
    tools.unregister()
    keymaps.unregister()