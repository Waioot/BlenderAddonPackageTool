import json
import websocket
import threading

from ..core.command_executor import CommandExecutor

class WebSocketThread(threading.Thread):
    def __init__(self, url, handlers):
        super().__init__(daemon=True)
        # 开启调试
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            url,
            **handlers
        )
    
    def run(self):
        self.ws.run_forever()

class WebSocketManager:
    def __init__(self):
        self.ws = None
        self.thread = None
        # 连接状态 blender 插件根据这个状态来切换按钮
        self.connected = False
        # 连接地址
        self.ip_address = "localhost"
        # 连接端口
        self.port = 5001

    def connect(self):
        if self.connected:
            return
            
        url = f"ws://{self.ip_address}:{self.port}"
        handlers = {
            'on_message': self.on_message,
            'on_error': self.on_error,
            'on_close': self.on_close,
            'on_open': self.on_open
        }
        
        self.thread = WebSocketThread(url, handlers)
        self.ws = self.thread.ws
        self.thread.start()
        self.connected = True
    def disconnect(self):
        if self.ws:
            self.ws.close()
            self.ws = None
            self.connected = False


    def send_message(self, message):
        if not self.connected:
            print("WebSocket is not connected")
            return False
            
        try:
            self.ws.send(message)
            return True
        except Exception as e:
            print(f"Failed to send message: {e}")
            return False

    def on_message(self, ws, message):
        print(f"Received message: {message}")
        try:
            data = json.loads(message)
            CommandExecutor.execute_command(data)
        except json.JSONDecodeError as e:
            print(f"Failed to parse message: {e}")
        except AttributeError:
            print("Warning: robotic_twin.execute_command operator not found")

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")
        self.connected = False

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")
        self.connected = False

    def on_open(self, ws):
        print("WebSocket connection opened")
        self.connected = True

# Global singleton instance
_websocket_manager_instance = None

def get_websocket_manager():
    global _websocket_manager_instance
    if _websocket_manager_instance is None:
        _websocket_manager_instance = WebSocketManager()
    return _websocket_manager_instance

def cleanup_websocket_manager():
    global _websocket_manager_instance
    if _websocket_manager_instance:
        _websocket_manager_instance.disconnect()
        _websocket_manager_instance = None