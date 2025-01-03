import bpy
import json
from ..core.websocket_manager import get_websocket_manager

# 获取全局websocket管理器
ws_manager = get_websocket_manager()


# 连接websocket
class WSConnectOperator(bpy.types.Operator):
    bl_label = "Connect WebSocket"
    bl_idname = "robotic_twin.connect_websocket"
    ip_address: bpy.props.StringProperty(name="IP Address", default="localhost")
    port: bpy.props.IntProperty(name="Port", default=5001)

    # 检查是否可以执行操作
    @classmethod
    def poll(cls, context: bpy.types.Context):
        """
        当未连接时，可以执行操作
        """
        return not ws_manager.connected

    def invoke(self, context, event):
        if ws_manager.connected:
            ws_manager.disconnect()
            return {'FINISHED'}
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        ws_manager.ip_address = self.ip_address
        ws_manager.port = self.port
        ws_manager.connect()
        return {'FINISHED'}
    
# 断开websocket连接
class WSDisconnectOperator(bpy.types.Operator):
    bl_label = "Disconnect WebSocket"
    bl_idname = "robotic_twin.disconnect_websocket"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return ws_manager.connected

    def execute(self, context):
        # 断开连接
        ws_manager.disconnect()
        return {'FINISHED'}

# 随机移动物体
class WSSenderRandom(bpy.types.Operator):
    '''
    随机移动物体
    发送命令：{"action": 0}
    服务端返回: x , y , z
    执行命令: bpy.ops.object.move(x=x, y=y, z=z)
    '''
    bl_label = "Move Cube Randomly"
    bl_idname = "robotic_twin.move_cube_random"

    def execute(self, context):
        if not ws_manager.connected:
            self.report({'ERROR'}, "WebSocket is not connected")
            return {'CANCELLED'}
        # 生成命令json
        command = json.dumps({
            'action': 0,
        })
        # 发送命令
        ws_manager.send_message(command)
        self.report({'INFO'}, "Command sent successfully")
        return {'FINISHED'}



# 面板发送命令操作
class WSSendCommandOperator(bpy.types.Operator):
    bl_label = "Send Command"
    bl_idname = "robotic_twin.send_command"
    
    command: bpy.props.StringProperty(
        name="Command",
        description="Command to send",
        default="{}"
    )

    def execute(self, context):
        if not ws_manager.connected:
            self.report({'ERROR'}, "WebSocket is not connected")
            return {'CANCELLED'}
        
        try:
            # 验证是否为有效的 JSON
            json.loads(self.command)
            if ws_manager.send_message(self.command):
                self.report({'INFO'}, "Command sent successfully")
                # 强制更新UI以显示新状态
                for area in context.screen.areas:
                    if area.type == 'VIEW_3D':
                        area.tag_redraw()
                return {'FINISHED'}
            return {'CANCELLED'}
        except json.JSONDecodeError:
            self.report({'ERROR'}, "Invalid JSON format")
            return {'CANCELLED'}
        except Exception as e:
            self.report({'ERROR'}, f"Failed to send command: {str(e)}")
            return {'CANCELLED'}