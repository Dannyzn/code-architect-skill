# Code Architect Skill

An OpenClaw skill that helps understand open-source code architecture and guides users to build minimal MVP versions step by step.

## Installation

```bash
openclaw skill install code-architect-skill
```

## Usage

This skill activates when you ask about understanding or building from open-source projects:

- "Help me understand how [project] works"
- "Analyze the architecture of [repo URL]"
- "Guide me to build a minimal version of [project]"
- "What are the core components of [project]?"
- "Generate documentation for [project]"

## Features

### 📊 Code Analysis
- Repository structure analysis
- Architecture mapping and explanation
- Core feature identification for MVP
- Design pattern recognition

### 📝 Documentation Generation

Generate comprehensive learning materials in multiple formats:

#### 1. PDF Learning Guide
```bash
python3 scripts/generate_learning_guide.py repo_info.json output.pdf
```

Creates a comprehensive PDF guide with:
- Project overview and tech stack
- Architecture diagrams and explanations
- Core components breakdown
- Implementation steps

**Requirements:** `pandoc` and `texlive-xetex`, or `pip install reportlab` for fallback

#### 2. PowerPoint Presentation
```bash
python3 scripts/generate_presentation.py repo_info.json output.pptx
```

Creates presentation slides with:
- Title and overview
- Architecture visualization
- Core components
- Implementation roadmap

**Requirements:** `pip install python-pptx`

#### 3. Implementation Tutorial
```bash
python3 scripts/generate_implementation_doc.py repo_info.json guide.md
```

Creates step-by-step tutorial with:
- Prerequisites and setup
- Detailed implementation steps with checkpoints
- Code examples
- Testing guidelines
- Next steps and resources

### 🎯 Step-by-Step Implementation Guidance

Get personalized guidance to build your own version:
- Simplified architecture for MVP scope
- Feature prioritization (core vs nice-to-have)
- Incremental implementation plan
- Testing and validation at each step

## Input Format

All generation scripts use a JSON input file:

```json
{
  "name": "Project Name",
  "purpose": "What the project does",
  "tech_stack": "Technologies used",
  "architecture": "Architecture description",
  "components": "Core components",
  "steps": "Implementation steps",
  "examples": "Code examples",
  "next_steps": "Future improvements"
}
```

See `scripts/example_repo_info.json` for a complete example.

## Example Workflow

1. Analyze a repository
2. Generate repo_info.json with analysis results
3. Create documentation in your preferred format:
   - PDF for detailed reading
   - PowerPoint for presentations
   - Markdown for interactive tutorials

## License

MIT
