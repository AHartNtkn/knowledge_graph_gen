# Knowledge Graph Updater

## Overview
This project aims to systematically process source materials to identify new skills and apps that can be added to an existing knowledge graph. It implements a workflow for extracting, validating, and integrating skills into comprehensive learning pathways.

## Project Goals
- Extract atomic skills from source materials
- Validate skills through a series of tests to ensure they are truly atomic
- Design and validate associated practice apps
- Integrate new skills and apps into existing knowledge graph
- Validate all prerequisite relationships

## Workflow
The project implements the workflow described in `work_flow_0_1.md`, which processes source materials through:

1. **Skill Extraction & Validation**
   - Extract skill candidates from source material
   - Validate atomic nature of skills
   - Define complete skill specifications

2. **App Design & Validation**
   - Design practice applications
   - Validate app effectiveness
   - Create detailed app specifications

3. **Graph Integration**
   - Map prerequisites to existing skills
   - Validate prerequisite relationships
   - Update knowledge graph explicitly

## Getting Started

### Prerequisites
- Python 3.8+
- ell library (for LLM interactions)
- Access to existing knowledge graph

### Installation
```bash
git clone https://github.com/yourusername/knowledge-graph-updater.git
cd knowledge-graph-updater

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Usage
```bash
python src/main.py --input source_material.txt --graph existing_graph.json
```

## Project Structure
```
knowledge-graph-updater/
├── src/
│   ├── main.py
│   ├── prompts/
│   │   └── extract_skills.py
│   ├── workflow/
│   │   └── phases.py
│   └── utils/
│       └── llm_interface.py
├── tests/
├── data/
│   ├── source_materials/
│   └── knowledge_graphs/
├── docs/
│   ├── workflow.md
│   └── interactables.md
└── README.md
```

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License
[Add your chosen license]
