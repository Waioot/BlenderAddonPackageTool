import bpy
from ..core.websocket_manager import get_websocket_manager

from ..config import __addon_name__
from ..operators.AddonOperators import ExampleOperator
from ....common.i18n.i18n import i18n
from ....common.types.framework import reg_order

# 使用函数获取单例
ws_manager = get_websocket_manager()

class BasePanel(object):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ExampleAddon"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True

@reg_order(0)
class ExampleAddonPanel(BasePanel, bpy.types.Panel):
    bl_label = "Example Addon Side Bar Panel"
    bl_idname = "SCENE_PT_sample"

    def draw(self, context: bpy.types.Context):
        addon_prefs = context.preferences.addons[__addon_name__].preferences

        layout = self.layout

        layout.label(text=i18n("Example Functions") + ": " + str(addon_prefs.number))
        layout.prop(addon_prefs, "filepath")
        layout.separator()

        row = layout.row()
        row.prop(addon_prefs, "number")
        row.prop(addon_prefs, "boolean")

        layout.operator(ExampleOperator.bl_idname)

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True

@reg_order(1)
class ExampleAddonPanel2(BasePanel, bpy.types.Panel):
    bl_label = "Example Addon Side Bar Panel"
    bl_idname = "SCENE_PT_sample2"

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        layout.label(text="Second Panel")
        layout.operator(ExampleOperator.bl_idname)

@reg_order(2)
class OBJECT_PT_CustomPanel(BasePanel, bpy.types.Panel):
    bl_label = "Websocket连接"
    bl_idname = "OBJECT_PT_custom_panel"


    @classmethod
    def poll(self,context):
        return True

    def draw(self, context):
        layout = self.layout

        # 定义状态对应的配置
        status_config = {
            True: {
                'alert': False,
                'text': "已连接",
                'icon': 'CHECKMARK',
                'operator': "robotic_twin.disconnect_websocket",
                'op_text': "断开连接"
            },
            False: {
                'alert': True,
                'text': "未连接",
                'icon': 'CANCEL',
                'operator': "robotic_twin.connect_websocket",
                'op_text': "连接WebSocket"
            }
        }

        # 获取当前状态的配置
        config = status_config[ws_manager.connected]
        
        
        # 应用配置
        row = layout.row()
        row.alert = config['alert']
        row.label(text=config['text'], icon=config['icon'])
        # 添加断开/连接按钮
        layout.operator(config['operator'], text=config['op_text'])
        layout.separator()
        layout.operator("robotic_twin.move_cube_random", text="随机移动物体")
