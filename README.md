# llm-internship-30days

这是一个 30 天 LLM 实习学习仓库，用来练习 Python 项目基础、命令行参数、日志记录、Git 提交和项目文档编写。

## 学习目标

本仓库用于练习以下内容：

- venv / conda 环境
- requirements.txt
- git commit
- README.md
- argparse
- logging

## 当前环境

本项目当前使用 conda 环境：

```bash
conda activate ai
```

## 项目结构

```text
llm-internship-30days/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── main.py
└── logs/
    └── .gitkeep
```

## 运行方式

在项目根目录执行：

```bash
python src/main.py --name Alice --days 30
```

Windows PowerShell 也可以执行：

```powershell
python .\src\main.py --name Alice --days 30
```

## 示例输出

```text
Hello Alice, welcome to llm-internship-30days!
You will study for 30 days.
```

## 日志说明

程序使用 Python 标准库 logging 记录日志。

运行程序后，会生成日志文件：

```text
logs/app.log
```

注意：`.gitignore` 中配置了 `*.log`，所以日志文件不会提交到 GitHub。

## Git 常用命令

查看状态：

```bash
git status
```

添加修改：

```bash
git add .
```

提交修改：

```bash
git commit -m "add README"
```

推送到 GitHub：

```bash
git push
```

## Day 1

完成内容：

- 创建 GitHub 仓库
- 初始化本地 Git 仓库
- 配置 conda 环境
- 创建 requirements.txt
- 编写 README.md
- 学习 argparse
- 学习 logging
- 完成第一次 git commit 和 git push
