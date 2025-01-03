## 功能

1. websocket 连接管理：
   - ✓ 通过 websocket 连接，与 websocket 服务器进行通信。
   - ✓ 面板提供一个提示框，用于显示 websocket 连接状态。当连接成功时，显示"已连接"；当连接失败时，显示"未连接"。
   - ✓ 面板中提供一个按钮，用于连接/断开 websocket 服务器。
     - ✓ 当未连接时，按钮文本显示"连接"，点击按钮后，会连接 websocket 服务器。
     - ✓ 当已连接时，按钮文本显示"断开"，点击按钮后，会断开 websocket 服务器。
2. 命令发送：
   - ✓ 已实现随机移动物体的命令发送功能
   - ✓ 添加了通用的命令输入框和发送按钮
   - ✓ 添加了命令发送状态提示
3. 命令接收：
   - ✓ 可以接收服务器发送的命令
   - ❌ 缺少接收命令的显示界面
   - ❌ 缺少接收状态提示
4. 命令执行：
   - ✓ 可以执行接收到的 JSON 格式命令
   - ✓ 在控制台打印执行结果
   - ✓ 支持移动物体的基础命令执行

## 实现日志

1. 完成了基础的 WebSocket 连接管理功能，包括连接状态显示和连接/断开控制
2. 实现了随机移动物体的命令发送功能
3. 实现了基础的命令接收和执行功能，支持移动物体的命令
4. 添加了通用命令输入界面和发送功能，支持发送自定义 JSON 命令
5. 添加了命令发送状态提示功能，实时显示命令发送结果

## 待完成功能

1. 添加命令接收显示界面
2. 添加命令接收状态提示

- 修复了 WebSocket 断开连接的问题，确保连接能够完全关闭并正确清理资源
