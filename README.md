<img src="/static/AppleComputerRainbow.svg" alt="Logo" width="15%"/>


# Apple ID 验证系统

本项目提供一个用于检验 Apple ID 有效性的网页接口。它使用 Flask 框架来构建一个网页应用程序，允许用户验证他们的凭证、检查验证结果、管理用户账户（管理员用）以及导出结果。

😋 在线访问：[http://8.134.157.203:5001](http://8.134.157.203:5001)

🌏 TG交流群：[加入群组](https://t.me/+m7x3s4caiQQ4MmVl)

<img src="/static/screenshot_home.jpeg" width="60%" />

<details>
<summary>Screenshots</summary>
<p float="left">
  <img src="/static/screenshot_data.jpg" width="50%" />
  <img src="/static/screenshot_admin.jpg" width="50%" />
</p>
</details>

## 功能

- 用户登录认证
- 管理员界面用于管理用户额度和信息
- 检查 Apple ID 验证结果
- 将验证结果导出为 CSV 格式
- 批量验证多个 Apple ID

## 安装

克隆仓库并安装所需的 Python 包:

```bash
git clone https://github.com/kangvcar/AppleIdChecker.git
cd AppleIdChecker
pip install -r requirements.txt
```

## 使用

使用以下命令运行 Flask 应用程序：

```bash
python app.py
```

# 使用 Docker （推荐）

1. 构建 Docker 镜像:

```bash
docker build -t appleid-checker .
```

2. 运行 Docker 容器:

```bash
docker run -d -p 5000:5000 appleid-checker
```

这将在后台启动一个容器，并将本地的 5000 端口映射到容器内运行的 Flask 应用程序的 5000 端口。

在您的网页浏览器中导航到 `http://localhost:5000` 以访问网页应用程序。

## 管理员管理

管理员界面位于 `http://localhost:5000/admin`，可执行以下管理任务：

- 修改用户验证限制
- 查看所有用户信息
- 创建新用户
- 删除用户

## 验证结果

用户可以在 `my_verification_results.html` 页面上查看他们的验证结果，并且可以基于账号状态（密码正确/错误、账号锁定、未知错误）进行筛选，并下载筛选后的结果为 CSV 文件。

## 贡献

我们欢迎贡献。如果您有改进应用程序的建议，请 Fork 仓库并创建一个 Pull Request，或者开一个带有 "enhancement" 标签的问题。

请确保适当更新测试。

## 许可证

本项目根据 MIT 许可证授权 - 详情请见 `LICENSE` 文件。

## 致谢

- 感谢 Flask 框架，使得网页开发变得容易。
- 感谢 Python 社区的持续支持。

## 联系方式

- **项目维护者:** [Kangvcar](https://github.com/kangvcar)
- **电子邮箱:**  kangvcar@gmail.com

## 项目状态

该项目目前处于开发阶段。用户和贡献者应预期会有快速的变化和功能改进。
