#!/bin/bash
cd "$(dirname "$0")"
# 绑定到 0.0.0.0 以允许 Windows 访问
nohup python3 -c "
import sys, os
sys.path.append(os.path.expanduser('~/.openclaw/workspace/skills'))
from server import app
# 绑定 0.0.0.0 让 Windows 浏览器也能访问
app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
" > /tmp/frontend.log 2>&1 &
echo "✅ 前端服务已启动"
echo "   WSL 内访问: http://127.0.0.1:5000"
echo "   Windows 访问: http://172.23.15.109:5000"
