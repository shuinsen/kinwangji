# 皇極經世占卜系统

本项目提供基于「皇極經世」的排盘与占卜功能，当前代码保留核心算法，并计划改造为**前后端分离**的架构，同时演示微信小程序的接入：

- **后端**：使用 FastAPI 封装排盘逻辑，提供 REST API。
- **前端**：使用 React 构建网页，向后端发送八字信息并展示运势、吉方向、穿衣颜色等结果。
- **微信小程序**：示例小程序调用同一 API，实现移动端输入与展示。

## 功能概述
- 输入年、月、日、时（即八字），计算次日卦象与运势。
- 基于日干五行返回吉凶、吉方向与推荐颜色。
- 计划支持微信小程序等多终端调用同一 API。

## 开发环境
- Python 3.10+
- 依赖见 `requirements.txt`
- Node.js（前端开发时使用）

## 快速开始
1. 安装 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行 FastAPI 开发服务器：
   ```bash
   uvicorn backend.main:app --reload
   ```
3. 打开 `frontend/index.html`，在浏览器中填写八字并调用接口。

4. 使用微信开发者工具导入 `miniapp/` 目录，可在真机或模拟器中填写八字并查询结果。

## 目录说明
- `backend/`：FastAPI 后端代码。
- `frontend/`：React 前端示例页面。
- `miniapp/`：微信小程序示例，展示如何调用后端 API。
- `wanji.py`：皇極經世核心排盘算法。
- `jieqi.py`：节气计算工具。
- `app.py`：旧版 Streamlit 示例，后续会被 FastAPI 替代。
- `data.pkl`：卦象基础数据。
- `DEV_PLAN.md`：前后端分离的开发计划。

## 许可证
本项目采用 MIT License。

