---
name: code-architect-skill
description: Analyze open-source code repositories to understand architecture, implementation patterns, and guide users through building minimal MVP versions step-by-step. Use when users want to (1) understand how an open-source project works, (2) learn the architecture and design patterns, (3) build a simplified MVP version of an existing project, or (4) get step-by-step guidance on implementing similar functionality.
---

# Code Architect Skill

This skill helps users understand open-source codebases and guides them through building minimal viable product (MVP) versions.

## Workflow

### 1. Repository Analysis

When given a repository URL or path:

1. Clone or access the repository
2. Identify the project structure and key directories
3. Locate entry points (main files, package.json, setup files)
4. Map out the core architecture

### 2. Architecture Understanding

Analyze and explain:

- **Project structure**: Directory organization and purpose
- **Core components**: Main modules and their responsibilities
- **Data flow**: How information moves through the system
- **Dependencies**: Key libraries and their roles
- **Design patterns**: Architectural patterns used

### 3. MVP Planning

Help users build a minimal version by:

1. Identifying core features vs nice-to-haves
2. Simplifying the architecture for MVP scope
3. Listing essential dependencies only
4. Creating a step-by-step implementation plan

### 4. Step-by-Step Implementation

Guide users through building the MVP:

- Start with project setup and basic structure
- Implement one feature at a time
- Provide code examples and explanations
- Test each component before moving forward
- Iterate based on user feedback

## Analysis Approach

For each repository:

1. **Quick scan**: README, package files, main entry points
2. **Structure mapping**: Create a mental model of the codebase
3. **Core identification**: Find the 20% that does 80% of the work
4. **Simplification**: Determine what can be stripped for MVP

## Output Format

When analyzing a project, provide:

```markdown
## Project Overview
- Purpose and main functionality
- Tech stack

## Architecture
- High-level structure
- Key components and their roles
- Data flow diagram (text-based)

## Core Features
- Essential features for MVP
- Optional features to skip

## Implementation Plan
1. Setup and dependencies
2. Core component A
3. Core component B
...
```

## Document Generation

Generate learning materials to help non-technical users understand projects:

### PDF Learning Guide

Use `scripts/generate_learning_guide.py` to create comprehensive PDF guides:

```bash
python3 scripts/generate_learning_guide.py repo_info.json output.pdf
```

**Input format** (`repo_info.json`):
```json
{
  "name": "Project Name",
  "purpose": "What it does",
  "tech_stack": "Technologies used",
  "architecture": "Architecture description",
  "components": "Core components",
  "steps": "Implementation steps",
  "examples": "Code examples"
}
```

**Fallback option**: If pandoc is unavailable, use `scripts/generate_pdf_simple.py` (requires `pip install reportlab`).

## Tips

- Focus on understanding before building
- Start simple, add complexity later
- Use the original code as reference, not as copy-paste source
- Explain the "why" behind architectural decisions
- Generate documentation for non-technical stakeholders
