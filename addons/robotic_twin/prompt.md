1. 你当前熟悉 python 语法，也熟悉 blender 插件开发所涉及到的相关 api
2. 你了解 websocket 的基本原理和使用方法
3. 注意模块化开发，将功能拆分成多个模块，提高代码的可读性和可维护性
4. 插件分为：面板绘制、管理、websocket 连接管理、命令解析与执行 3 个模块
    - 面板绘制：绘制面板，包括提示框、按钮、输入框、文本框等
    - 面板管理：管理面板中的各个控件，包括按钮点击事件、输入框输入事件等
    - websocket 连接管理：管理 websocket 连接，包括连接、断开、命令发送、命令接收
    - 发送和接收到命令后，通过命令解析，调用命令执行方法执行对应命令