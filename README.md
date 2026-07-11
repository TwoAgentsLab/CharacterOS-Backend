# CharacterOS

<p align="center">
  <img src="docs/assets/logo.png" width="180" alt="CharacterOS Logo"/>
</p>

<p align="center">
  <strong>AI-Powered NPC Infrastructure for Games</strong>
</p>

<p align="center">
  Build intelligent, persistent, and dynamic NPCs for any game engine through a simple SDK and API.
</p>

<p align="center">
    <img src="https://img.shields.io/badge/status-in%20development-orange"/>
    <img src="https://img.shields.io/badge/python-3.14-blue"/>
    <img src="https://img.shields.io/badge/FastAPI-Backend-green"/>
    <img src="https://img.shields.io/badge/PostgreSQL-Database-blue"/>
    <img src="https://img.shields.io/badge/LangGraph-Orchestration-purple"/>
    <img src="https://img.shields.io/badge/license-MIT-lightgrey"/>
</p>

---

# Overview

CharacterOS is an AI NPC platform that enables game developers to create intelligent, context-aware, and persistent NPCs without building complex AI infrastructure from scratch.

Developers can create NPCs through a dashboard, integrate the SDK into their game engine, and communicate with NPCs through a simple API.

CharacterOS handles:

- NPC personality management
- Dialogue generation
- Multi-project support
- API authentication
- Context orchestration
- Future memory and relationship systems

---

# Vision

Traditional NPCs are static and heavily scripted.

CharacterOS aims to provide:

- Dynamic conversations
- Persistent memories
- Relationship systems
- Emotional states
- Quest awareness
- World-state understanding
- Engine-agnostic integration

The long-term goal is to become an AI infrastructure layer for modern games.

---

# Architecture

```text
Game Engine
      ↓
CharacterOS SDK
      ↓
FastAPI Backend
      ↓
Authentication
      ↓
LangGraph
      ↓
PostgreSQL
      ↓
LLM Provider
```

---

# Current Features

### Authentication

- API Key authentication
- Multi-project support
- Project isolation

### NPC System

- Static NPC personalities
- Dynamic prompt construction
- Database-driven NPC loading

### Backend

- FastAPI
- LangGraph workflow orchestration
- PostgreSQL persistence

### SDK (Planned)

- Godot SDK
- Unity SDK
- Unreal SDK

---

# Tech Stack

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend API |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| LangGraph | AI Workflow Orchestration |
| Groq / OpenAI | LLM Providers |
| Pydantic | Validation |
| Python | Backend Language |

---

# Project Structure

```text
CharacterOS/
│
├── app/
│   ├── api/
│   ├── graph/
│   ├── nodes/
│   ├── database/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── core/
│
├── docs/
├── tests/
├── sdk/
└── README.md
```

---

# LangGraph Flow

Current NPC workflow:

```text
START
   ↓
Load NPC
   ↓
Build Prompt
   ↓
LLM
   ↓
END
```

Future workflow:

```text
START
   ↓
Authentication
   ↓
Load NPC
   ↓
Load Memories
   ↓
Load Relationships
   ↓
Load World State
   ↓
Build Prompt
   ↓
LLM
   ↓
Save Memory
   ↓
END
```

---

# Database Architecture

## Projects

Stores developer projects and API keys.

```text
Project
    ↓
Many NPCs
```

Fields:

- id
- project_code
- name
- api_key

---

## NPCs

Stores NPC information.

Fields:

- id
- project_id
- npc_code
- name
- occupation
- personality
- backstory

---

# Example Request

### Endpoint

```http
POST /chat
```

### Headers

```http
Authorization: Bearer aurix_sk_xxxxxxxxx
```

### Body

```json
{
    "npc_id": "merchant_01",
    "player_id": "player_01",
    "player_message": "Hello Thomas"
}
```

### Response

```json
{
    "response": "Welcome to Oak Village! How may I assist you today?"
}
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/TwoAgentsLab/CharacterOS.git
cd CharacterOS
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=
GROQ_API_KEY=
OPENAI_API_KEY=
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Example SDK Usage (Planned)

```gdscript
CharacterOS.initialize(
    "aurix_sk_xxxxxxxxx"
)

var response = await CharacterOS.chat(
    "merchant_01",
    "player_01",
    "Hello"
)

print(response)
```

---

# Roadmap

## Version 0.x

- [x] FastAPI Backend
- [x] LangGraph Integration
- [x] PostgreSQL Integration
- [x] Multi-Project Architecture
- [x] API Key Authentication
- [x] Static NPC System

---

## Version 1.x

- [ ] Project CRUD APIs
- [ ] NPC CRUD APIs
- [ ] SDK MVP
- [ ] Developer Dashboard
- [ ] NPC Editor

---

## Version 2.x

- [ ] Memory System
- [ ] Relationship System
- [ ] World State Awareness
- [ ] Quest Awareness
- [ ] Dynamic NPC Behaviour

---

## Version 3.x

- [ ] Emotion System
- [ ] Autonomous NPC Actions
- [ ] Multi-Agent NPC Communication
- [ ] Multiplayer Support
- [ ] AI-Driven Storytelling

---

# Documentation

Documentation is maintained using Obsidian.

Topics include:

- Architecture
- Database Design
- SDK Design
- LangGraph Flows
- Future Systems
- Product Vision

---

# Contributing

CharacterOS is currently in active development.

Contributions, discussions, and ideas are welcome.

Please open an issue before submitting major changes.

---

# Philosophy

CharacterOS is built around a simple idea:

> NPCs should feel like living characters rather than dialogue machines.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# Authors

### Two Agents Lab

Building AI infrastructure for the next generation of games.

---

<p align="center">
  Made with ❤️ using FastAPI, LangGraph and PostgreSQL.
</p>
