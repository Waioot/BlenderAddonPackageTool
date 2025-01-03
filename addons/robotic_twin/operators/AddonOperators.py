import bpy
from bpy.props import StringProperty, IntProperty

from ..config import __addon_name__
from ..preference.AddonPreferences import ExampleAddonPreferences

class ExampleOperator(bpy.types.Operator):
    '''ExampleAddon'''
    bl_idname = "object.example_ops"
    bl_label = "ExampleOperator"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        addon_prefs = bpy.context.preferences.addons[__addon_name__].preferences
        assert isinstance(addon_prefs, ExampleAddonPreferences)
        context.active_object.scale *= addon_prefs.number
        return {'FINISHED'}
