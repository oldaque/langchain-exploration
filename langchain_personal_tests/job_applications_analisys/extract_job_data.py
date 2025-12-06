import os
import argparse
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from pydantic import BaseModel, Field
from typing import List, Literal
import langchain
langchain.debug = True

# Load environment variables
load_dotenv()

# Define technical knowledge categories for AI Engineer and Data Science roles
TechnicalKnowledge = Literal[
    # Machine Learning & Deep Learning
    "Machine Learning Modeling",
    "Deep Learning",
    "Model Training",
    "Model Finetuning",
    "Transfer Learning",
    "Model Optimization",
    "Hyperparameter Tuning",
    "Feature Engineering",
    "Model Evaluation",
    "Model Deployment",

    # Natural Language Processing
    "Natural Language Processing (NLP)",
    "Large Language Models (LLMs)",
    "Text Processing",
    "Named Entity Recognition (NER)",
    "Sentiment Analysis",
    "Text Classification",
    "Prompt Engineering",
    "RAG (Retrieval-Augmented Generation)",

    # Computer Vision
    "Computer Vision",
    "Image Processing",
    "Object Detection",
    "Image Classification",
    "Image Segmentation",

    # Generative AI
    "Generative AI",
    "GANs (Generative Adversarial Networks)",
    "Diffusion Models",
    "Text Generation",
    "Image Generation",

    # MLOps & Engineering
    "MLOps",
    "CI/CD",
    "Model Monitoring",
    "A/B Testing",
    "Experiment Tracking",
    "Model Versioning",
    "Pipeline Automation",

    # Data Engineering
    "Data Engineering",
    "ETL/ELT",
    "Data Pipeline Development",
    "Data Warehousing",
    "Stream Processing",
    "Batch Processing",

    # Data Analysis & Statistics
    "Statistical Analysis",
    "Data Analysis",
    "Data Visualization",
    "Exploratory Data Analysis (EDA)",
    "Hypothesis Testing",
    "Time Series Analysis",
    "Predictive Analytics",

    # Software Engineering
    "Software Engineering",
    "API Development",
    "Microservices Architecture",
    "System Design",
    "Code Optimization",
    "Testing & Quality Assurance",

    # Cloud & Infrastructure
    "Cloud Computing",
    "Containerization",
    "Kubernetes Orchestration",
    "Infrastructure as Code",
    "Distributed Systems",

    # Research & Development
    "Research & Development",
    "Algorithm Development",
    "Technical Writing",
    "Paper Implementation",

    # Agile & Project Management
    "Agile Methodologies",
    "Scrum",
    "Project Management"
]

# Define the structured output model
class JobExtraction(BaseModel):
    """Extraction of technical skills and knowledge from job descriptions."""
    skills: List[str] = Field(description="List of technical skills required (e.g., Python, SQL, Java).")
    technologies: List[str] = Field(description="List of specific technologies, libraries, or platforms (e.g., LangChain, PyTorch, AWS, Docker).")
    technical_knowledge: List[TechnicalKnowledge] = Field(description="List of specific technical knowledge or concepts required from the predefined categories. Only select items that are explicitly mentioned or strongly implied in the job description.")

def get_job_data():
    csv_path = "jobs.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return []
    
    try:
        df = pd.read_csv(csv_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def extract_info(jobs, is_test=False):
    model_name = os.environ.get("DEFAULT_MODEL", "google_genai:gemini-2.5-flash")
    print(f"Using model: {model_name}")

    # Define system prompt with rules and instructions
    system_prompt = """You are an expert at analyzing job descriptions and extracting technical requirements.

Your task is to extract technical skills, technologies, and knowledge from job descriptions with high precision.

Guidelines:
- For "skills": List general programming languages or core skills (e.g., Python, SQL, Java).
- For "technologies": List specific libraries, frameworks, or tools (e.g., LangChain, PyTorch, AWS, Docker).
- For "technical_knowledge": List specific concepts or methodologies (e.g., "Machine Learning Modeling", "Model Finetuning", "CI/CD").

IMPORTANT RULES:
- Do NOT infer skills that are not explicitly mentioned or strongly implied by the context.
- If the job mentions "PyTorch" but does not mention "creating models" or "finetuning", do NOT list "Model Finetuning" as knowledge.
- Distinguish between using a tool and understanding the underlying concept if the text makes that distinction.
- Be specific about the context for technical knowledge items."""

    try:
        agent = create_agent(
            model=model_name,
            response_format=ToolStrategy(JobExtraction),
            system_prompt=system_prompt
        )
    except Exception as e:
        print(f"Error creating agent: {e}")
        return

    output_file = "job_analysis_results.csv"
    
    # Initialize CSV with headers if it doesn't exist or if we are starting fresh (optional, but for incremental we usually append)
    # However, if we run the script multiple times, we might want to clear it or append. 
    # For this task, I'll overwrite if it's a new run, but write incrementally.
    
    # actually, let's write headers first
    fieldnames = ["titulo", "empresa", "localizacao", "skills", "technologies", "technical_knowledge"]
    
    # If we are just testing, maybe we don't want to overwrite the main file? 
    # User said "generate a CSV file". I'll use the same name.
    
    with open(output_file, 'w') as f:
        pd.DataFrame(columns=fieldnames).to_csv(f, index=False)

    count = 0
    limit = 5 if is_test else len(jobs)
    
    print(f"Processing {limit} jobs...")

    for i, job in enumerate(jobs):
        if count >= limit:
            break
            
        description = job.get('descricao', '')
        title = job.get('titulo', '')
        
        if not description:
            continue
            
        # User prompt contains only the job description and position title
        prompt = f"""# Position: {title}
---
# Job Description:
{description}"""
        
        try:
            result = agent.invoke({
                "messages": [{"role": "user", "content": prompt}]
            })
            
            extraction = result["structured_response"]
            
            row = {
                "titulo": title,
                "empresa": job.get('empresa'),
                "localizacao": job.get('localizacao'),
                "skills": ", ".join(extraction.skills),
                "technologies": ", ".join(extraction.technologies),
                "technical_knowledge": ", ".join(extraction.technical_knowledge)
            }
            
            # Write incrementally
            pd.DataFrame([row]).to_csv(output_file, mode='a', header=False, index=False)
            
            print(f"[{i+1}/{limit}] Processed: {title}")
            count += 1
            
        except Exception as e:
            print(f"Error processing {title}: {e}")

    print(f"Finished processing. Results saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Extract job data.")
    parser.add_argument("--test", action="store_true", help="Run in test mode (process only 5 jobs).")
    args = parser.parse_args()

    print("Fetching jobs...")
    jobs = get_job_data()
    print(f"Found {len(jobs)} jobs.")
    
    if not jobs:
        print("No jobs found.")
        return

    extract_info(jobs, is_test=args.test)

if __name__ == "__main__":
    main()
