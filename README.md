### mem0-api

#一、仓库结构
mem0-api/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── app/
│   ├── main.py
│   ├── config.py
│   ├── memory.py
│   ├── schemas.py
│   └── security.py
└── README.md
#二、核心设计说明

✔ 架构原则

mem0 作为独立 HTTP 服务
OpenClaw / 其他 Agent 只走 API
多用户 / 多 Agent 隔离

支持后期：
Qdrant / pgvector / Milvus
鉴权
限流
