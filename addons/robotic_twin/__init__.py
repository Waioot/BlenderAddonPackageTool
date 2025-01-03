import bpy

from .config import __addon_name__
from .i18n.dictionary import dictionary
from ...common.class_loader import auto_load
from ...common.class_loader.auto_load import add_properties, remove_properties
from ...common.i18n.dictionary import common_dictionary
from ...common.i18n.i18n import load_dictionary

# Add-on info
bl_info = {
    "name": "机器人孪生",
    "author": "[yingshuming]",
    "blender": (3, 5, 0),
    "version": (0, 0, 1),
    "description": "This is a template for building addons",
    "warning": "",
    "doc_url": "[documentation url]",
    "tracker_url": "[contact email]",
    "support": "COMMUNITY",
    "category": "3D View"
}

_addon_properties = {}

def register():
    # Register classes
    auto_load.init()
    auto_load.register()
    add_properties(_addon_properties)

    # Internationalization
    load_dictionary(dictionary)
    try:
        bpy.app.translations.register(__addon_name__, common_dictionary)
    except ValueError:
        # 如果已经注册过，就先取消注册再重新注册
        bpy.app.translations.unregister(__addon_name__)
        bpy.app.translations.register(__addon_name__, common_dictionary)

    print("{} addon is installed.".format(__addon_name__))

def unregister():
    # Internationalization
    try:
        bpy.app.translations.unregister(__addon_name__)
    except ValueError:
        pass  # 如果已经取消注册了就忽略错误
    
    # Unregister classes
    auto_load.unregister()
    remove_properties(_addon_properties)
    
    print("{} addon is uninstalled.".format(__addon_name__))
