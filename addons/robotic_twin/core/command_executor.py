import bpy
import json

class CommandExecutor:
    @staticmethod
    def execute_command(message):
        """
        根据传入的 json 执行命令
        命令格式: {"action": 0, "x": 1, "y": 2, "z": 3} 含义: 随机移动物体到(1,2,3)
        """
        # 将收到命令的json打印到控制台
        print(f"Received command: {message}")

        # 执行命令
        if 'action' in message:
            if message['action'] == 0:
                if CommandExecutor.move_cube_randomly(message):
                    print("Command executed successfully")
                else:
                    print("Command execution failed")

    @staticmethod
    def move_cube_randomly(message):
        """随机移动立方体"""
        if "Cube" in bpy.data.objects:  # 检查场景中是否存在名为 "Cube" 的物体
            obj = bpy.data.objects["Cube"]  # 获取名为 "Cube" 的物体对象
            if 'x' in message:
                obj.location.x = message['x']  # 如果 JSON 数据中包含 'x' 键，则更新立方体的 X 坐标
            if 'y' in message:
                obj.location.y = message['y']  # 如果 JSON 数据中包含 'y' 键，则更新立方体的 Y 坐标
            if 'z' in message:
                obj.location.z = message['z']  # 如果 JSON 数据中包含 'z' 键，则更新立方体的 Z 坐标
            return True
        return False