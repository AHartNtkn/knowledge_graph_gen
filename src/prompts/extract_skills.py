"""Prompt for initial skill extraction"""
import ell
import json
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

@ell.simple(model="claude-3-5-haiku-20241022", max_tokens=1000)
def extract_skills(text: str):
    """You are a skill extraction engine. Your task is to identify truly atomic skills from educational content.

A skill can be demonstrated through a specific action with unambiguous success criteria

Identify two types of skills:
- Observable skills: Concrete actions with specific inputs and outputs
- Intuitive skills: Mental processes that guide problem-solving

I am NOT asking for skills mentioned explicitly in the text. I'm asking for all skills required to understand the text. This will include skills the text implicitly relies on when, for example, writing a demonstration or step of reasoning the reader is expected to understand.

For each skill, create:
- A precise name using action verbs (for observable skills) or mental process verbs (for intuitive skills)
- A clear description explaining exactly what the skill enables a learner to do
- An worked demonstration of the skill, either taken from or inspired by the source material

DO NOT include:
- Abstract concepts like "understand X" or "know about Y"
- Skills not directly taught or required by the source material

The skills should be directly derivable from the content provided, focusing exclusively on the subject domain of the source material.

Be thorough and creative. Err on the side of including more skills.

Respond ONLY with a JSON array. Each object should have 'name', 'description', and 'demonstration' fields.
Do not include any other text before or after the JSON.
"""
    return f"""
Source material:
{text}
"""

def load_existing_skills():
    """Load existing skills from JSON file if it exists"""
    skills_file = Path("data/extracted_skills.json")
    if skills_file.exists():
        with open(skills_file) as f:
            return json.load(f)
    return []

def save_skills(new_skills):
    """Save combined skills list to JSON file"""
    existing_skills = load_existing_skills()
    
    # Add only new skills that aren't already present
    skill_names = {s['name'] for s in existing_skills}
    for skill in new_skills:
        if skill['name'] not in skill_names:
            existing_skills.append(skill)
    
    # Ensure data directory exists
    Path("data").mkdir(exist_ok=True)
    
    # Save updated list
    with open("data/extracted_skills.json", 'w') as f:
        json.dump(existing_skills, f, indent=2)

def process_source_text(source_text: str):
    """Extract skills from source text and save them"""
    logger.info("Extracting skills from source material")
    skills = extract_skills(source_text)
    
    logger.info("Parsing LLM response")
    # Find the JSON array by looking for first '[' and last ']'
    start = skills.find('[')
    end = skills.rfind(']') + 1
    cleaned_json = skills[start:end]
    skills_list = json.loads(cleaned_json)
    
    logger.info("Saving extracted skills")
    save_skills(skills_list)
