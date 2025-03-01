"""Main entry point for knowledge graph updater"""
import asyncio
import ell
import anthropic
from dotenv import load_dotenv
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

logger.info("Initializing ell with storage")
# Initialize ell with storage and autocommit
ell.init(store='./data/ell_store', autocommit=True)

logger.info("Configuring Anthropic client")
# Create and register Anthropic client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
ell.config.register_model("claude-3-5-haiku-20241022", client)

# Import prompts after client registration
from prompts.extract_skills import process_source_text

async def main():
    while True:
        # Get input file path
        source_file = input("Enter path to source material (relative to data/source_materials/): ")
        full_path = Path("data/source_materials") / source_file
        
        # Check if file exists
        if full_path.exists():
            # Read source material
            logger.info(f"Reading source material from {full_path}")
            with open(full_path) as f:
                source_text = f.read()
            break
        else:
            print(f"File not found: {full_path}")
            continue
    
    process_source_text(source_text)
    print(f"Skills extracted and saved to data/extracted_skills.json")

if __name__ == "__main__":
    asyncio.run(main()) 