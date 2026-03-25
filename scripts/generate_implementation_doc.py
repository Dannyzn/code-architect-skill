#!/usr/bin/env python3
"""
Generate step-by-step implementation documentation.
Creates a detailed tutorial with code examples and checkpoints.
"""

import sys
import json
from pathlib import Path

def generate_implementation_markdown(repo_info, output_path):
    """Generate implementation guide in markdown format."""
    
    md_content = f"""# {repo_info['name']} - Implementation Guide

## 🎯 Goal

Build a minimal viable product (MVP) version of {repo_info['name']}.

**What you'll learn:**
- Understanding the core architecture
- Implementing key features step by step
- Testing and validating your implementation

---

## 📋 Prerequisites

**Tech Stack:**
{repo_info.get('tech_stack', 'N/A')}

**Required Knowledge:**
- Basic programming concepts
- Familiarity with the tech stack above

---

## 🏗️ Architecture Overview

{repo_info.get('architecture', 'Architecture details...')}

---

## 🔧 Core Components

{repo_info.get('components', 'Component details...')}

---

"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return output_path

def add_implementation_steps(md_content, repo_info):
    """Add detailed implementation steps."""
    
    steps = repo_info.get('steps', '').split('\n')
    
    md_content += "## 📝 Implementation Steps\n\n"
    
    for i, step in enumerate(steps, 1):
        if step.strip():
            step_clean = step.strip().lstrip('0123456789. ')
            md_content += f"### Step {i}: {step_clean}\n\n"
            md_content += f"**What to do:**\n"
            md_content += f"- Implement {step_clean.lower()}\n"
            md_content += f"- Test the functionality\n\n"
            md_content += f"**Checkpoint:** ✅ Verify that {step_clean.lower()} works correctly\n\n"
            md_content += "---\n\n"
    
    return md_content

def add_code_examples(md_content, repo_info):
    """Add code examples section."""
    
    md_content += "## 💻 Code Examples\n\n"
    md_content += repo_info.get('examples', 'Code examples will be added here...')
    md_content += "\n\n---\n\n"
    
    return md_content

def add_testing_section(md_content):
    """Add testing and validation section."""
    
    md_content += """## 🧪 Testing & Validation

**Test each component:**
1. Unit tests for individual functions
2. Integration tests for component interactions
3. End-to-end tests for complete workflows

**Validation checklist:**
- [ ] All core features work as expected
- [ ] Error handling is in place
- [ ] Code is clean and documented
- [ ] Performance is acceptable

---

"""
    return md_content

def add_next_steps(md_content, repo_info):
    """Add next steps and resources."""
    
    md_content += """## 🚀 Next Steps

"""
    md_content += repo_info.get('next_steps', '- Continue learning\n- Build more features\n- Share your work')
    md_content += "\n\n"
    md_content += """
**Resources:**
- Original repository for reference
- Documentation and tutorials
- Community forums and discussions

---

## 🎉 Congratulations!

You've built a working MVP! Keep iterating and improving.
"""
    
    return md_content

def main():
    if len(sys.argv) < 2:
        print("Usage: generate_implementation_doc.py <repo_info.json> [output.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_md = sys.argv[2] if len(sys.argv) > 2 else "implementation_guide.md"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        repo_info = json.load(f)
    
    md_path = generate_implementation_markdown(repo_info, output_md)
    
    # Read and enhance the content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    md_content = add_implementation_steps(md_content, repo_info)
    md_content = add_code_examples(md_content, repo_info)
    md_content = add_testing_section(md_content)
    md_content = add_next_steps(md_content, repo_info)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"✓ Generated implementation guide: {md_path}")

if __name__ == '__main__':
    main()
