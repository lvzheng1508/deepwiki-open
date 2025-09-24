#!/usr/bin/env python3
"""
DeepWiki Demo Script

This script simulates the complete DeepWiki execution flow for the test project,
showing all inputs and outputs at each step.
"""

import os
import json
import sys
from pathlib import Path

# Add api directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'api'))

def print_step(step_num, title, content=""):
    """Print a formatted step header."""
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {title}")
    print(f"{'='*60}")
    if content:
        print(content)

def simulate_file_tree_extraction():
    """Simulate the file tree extraction process."""
    print_step(1, "FILE TREE EXTRACTION")
    
    test_project_path = "test_project"
    file_tree = []
    
    for root, dirs, files in os.walk(test_project_path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if not file.startswith('.'):
                rel_path = os.path.relpath(os.path.join(root, file), test_project_path)
                file_tree.append(rel_path)
    
    file_tree_str = "\n".join(sorted(file_tree))
    
    print("Extracted file tree:")
    print(file_tree_str)
    
    return file_tree_str

def simulate_readme_extraction():
    """Simulate the README extraction process."""
    print_step(2, "README EXTRACTION")
    
    readme_path = "test_project/README.md"
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        print("Extracted README content:")
        print(readme_content)
        return readme_content
    else:
        print("No README.md found")
        return ""

def simulate_initial_user_request(file_tree, readme):
    """Simulate the initial user request construction."""
    print_step(3, "INITIAL USER REQUEST CONSTRUCTION")
    
    # This simulates what happens in src/app/[owner]/[repo]/page.tsx lines 681-730
    request_body = {
        "repo_url": "local/test_project",
        "type": "local",
        "messages": [{
            "role": "user",
            "content": f"""Analyze this GitHub repository local/test_project and create a wiki structure for it.
1. The complete file tree of the project:
<file_tree>
{file_tree}
</file_tree>
2. The README file of the project:
<readme>
{readme}
</readme>
I want to create a wiki for this repository. Determine the most logical structure for a wiki based on the repository's content.
IMPORTANT: The wiki content will be generated in English language.
When designing the wiki structure, include pages that would benefit from visual diagrams, such as:
- Architecture overviews
- Data flow descriptions
- Component relationships
- Process workflows
- State machines
- Class hierarchies

Create a structured wiki with the following main sections:
- Overview (general information about the project)
- System Architecture (how the system is designed)
- Core Features (key functionality)
- Data Management/Flow: If applicable, how data is stored, processed, accessed, and managed (e.g., database schema, data pipelines, state management).
- Frontend Components (UI elements, if applicable.)
- Backend Systems (server-side components)
- Model Integration (AI model connections)
- Deployment/Infrastructure (how to deploy, what's the infrastructure like)
- Extensibility and Customization: If the project architecture supports it, explain how to extend or customize its functionality (e.g., plugins, theming, custom modules, hooks)."""
        }],
        "provider": "google",
        "model": "gemini-1.5-flash",
        "language": "en",
        "filters": {
            "include_dirs": [],
            "exclude_dirs": [".git", "node_modules", "__pycache__", ".venv"],
            "include_files": [],
            "exclude_files": []
        }
    }
    
    print("Constructed request body:")
    print(json.dumps(request_body, indent=2))
    
    return request_body

def simulate_code_processing():
    """Simulate the one-time code processing stage."""
    print_step(4, "CODE PROCESSING STAGE (ONE-TIME)")
    
    print("This stage involves:")
    print("1. Reading all files from the repository")
    print("2. Filtering files based on include/exclude rules")
    print("3. Splitting text using adalflow.TextSplitter")
    print("4. Creating embeddings using the configured embedder")
    print("5. Storing in FAISS vector database")
    
    # Simulate file reading
    files_processed = []
    for root, dirs, files in os.walk("test_project"):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if not file.startswith('.') and file.endswith(('.py', '.md', '.txt')):
                rel_path = os.path.relpath(os.path.join(root, file), "test_project")
                files_processed.append(rel_path)
    
    print(f"\nFiles processed: {files_processed}")
    
    # Simulate text splitting
    print("\nText splitting configuration:")
    print("- Split by: word")
    print("- Chunk size: 350")
    print("- Chunk overlap: 100")
    
    # Simulate embedding creation
    print("\nEmbedding creation:")
    print("- Using configured embedder (e.g., OpenAI text-embedding-3-small)")
    print("- Creating vector representations for each chunk")
    
    # Simulate vector database storage
    print("\nVector database storage:")
    print("- Using FAISS for vector storage and retrieval")
    print("- Saving to local database file for future use")
    
    return files_processed

def simulate_deepresearch_iterations():
    """Simulate the DeepResearch iterations."""
    print_step(5, "DEEPRESEARCH ITERATIONS")
    
    iterations = [
        {
            "iteration": 1,
            "title": "FIRST ITERATION - Research Plan",
            "system_prompt": """<role>
You are an expert code analyst examining the local repository: local/test_project (test_project).
You are conducting a multi-turn Deep Research process to thoroughly investigate the specific topic in the user's query.
Your goal is to provide detailed, focused information EXCLUSIVELY about this topic.
IMPORTANT:You MUST respond in English language.
</role>

<guidelines>
- This is the first iteration of a multi-turn research process focused EXCLUSIVELY on the user's query
- Start your response with "## Research Plan"
- Outline your approach to investigating this specific topic
- If the topic is about a specific file or feature (like "Dockerfile"), focus ONLY on that file or feature
- Clearly state the specific topic you're researching to maintain focus throughout all iterations
- Identify the key aspects you'll need to research
- Provide initial findings based on the information available
- End with "## Next Steps" indicating what you'll investigate in the next iteration
- Do NOT provide a final conclusion yet - this is just the beginning of the research
- Do NOT include general repository information unless directly relevant to the query
- Focus EXCLUSIVELY on the specific topic being researched - do not drift to related topics
- Your research MUST directly address the original question
- NEVER respond with just "Continue the research" as an answer - always provide substantive research findings
- Remember that this topic will be maintained across all research iterations
</guidelines>""",
            "user_query": "Analyze this GitHub repository local/test_project and create a wiki structure for it...",
            "rag_context": "Retrieved code chunks from vector database based on the query",
            "expected_output": "Research plan for wiki structure creation"
        },
        {
            "iteration": 2,
            "title": "SECOND ITERATION - Research Update",
            "system_prompt": """<role>
You are an expert code analyst examining the local repository: local/test_project (test_project).
You are currently in iteration 2 of a Deep Research process focused EXCLUSIVELY on the latest user query.
Your goal is to build upon previous research iterations and go deeper into this specific topic without deviating from it.
IMPORTANT:You MUST respond in English language.
</role>

<guidelines>
- CAREFULLY review the conversation history to understand what has been researched so far
- Your response MUST build on previous research iterations - do not repeat information already covered
- Identify gaps or areas that need further exploration related to this specific topic
- Focus on one specific aspect that needs deeper investigation in this iteration
- Start your response with "## Research Update 2"
- Clearly explain what you're investigating in this iteration
- Provide new insights that weren't covered in previous iterations
- If this is iteration 3, prepare for a final conclusion in the next iteration
- Do NOT include general repository information unless directly relevant to the query
- Focus EXCLUSIVELY on the specific topic being researched - do not drift to related topics
- If the topic is about a specific file or feature (like "Dockerfile"), focus ONLY on that file or feature
- NEVER respond with just "Continue the research" as an answer - always provide substantive research findings
- Your research MUST directly address the original question
- Maintain continuity with previous research iterations - this is a continuous investigation
</guidelines>""",
            "user_query": "Analyze this GitHub repository local/test_project and create a wiki structure for it...",
            "rag_context": "Retrieved code chunks + conversation history from iteration 1",
            "expected_output": "Deeper analysis of specific aspects identified in iteration 1"
        },
        {
            "iteration": 3,
            "title": "THIRD ITERATION - Research Update",
            "system_prompt": "Similar to iteration 2, but with '## Research Update 3'",
            "user_query": "Analyze this GitHub repository local/test_project and create a wiki structure for it...",
            "rag_context": "Retrieved code chunks + conversation history from iterations 1-2",
            "expected_output": "Further detailed analysis of remaining aspects"
        },
        {
            "iteration": 4,
            "title": "FOURTH ITERATION - Research Update",
            "system_prompt": "Similar to iteration 2, but with '## Research Update 4'",
            "user_query": "Analyze this GitHub repository local/test_project and create a wiki structure for it...",
            "rag_context": "Retrieved code chunks + conversation history from iterations 1-3",
            "expected_output": "Final detailed analysis before conclusion"
        },
        {
            "iteration": 5,
            "title": "FIFTH ITERATION - Final Conclusion",
            "system_prompt": """<role>
You are an expert code analyst examining the local repository: local/test_project (test_project).
You are in the final iteration of a Deep Research process focused EXCLUSIVELY on the latest user query.
Your goal is to synthesize all previous findings and provide a comprehensive conclusion that directly addresses this specific topic and ONLY this topic.
IMPORTANT:You MUST respond in English language.
</role>

<guidelines>
- This is the final iteration of the research process
- CAREFULLY review the entire conversation history to understand all previous findings
- Synthesize ALL findings from previous iterations into a comprehensive conclusion
- Start with "## Final Conclusion"
- Your conclusion MUST directly address the original question
- Stay STRICTLY focused on the specific topic - do not drift to related topics
- Include specific code references and implementation details related to the topic
- Highlight the most important discoveries and insights about this specific functionality
- Provide a complete and definitive answer to the original question
- Do NOT include general repository information unless directly relevant to the query
- Focus exclusively on the specific topic being researched
- NEVER respond with "Continue the research" as an answer - always provide a complete conclusion
- If the topic is about a specific file or feature (like "Dockerfile"), focus ONLY on that file or feature
- Ensure your conclusion builds on and references key findings from previous iterations
</guidelines>""",
            "user_query": "Analyze this GitHub repository local/test_project and create a wiki structure for it...",
            "rag_context": "Retrieved code chunks + complete conversation history from iterations 1-4",
            "expected_output": "Comprehensive wiki structure with detailed content"
        }
    ]
    
    for iteration in iterations:
        print(f"\n--- {iteration['title']} ---")
        print(f"System Prompt: {iteration['system_prompt'][:200]}...")
        print(f"User Query: {iteration['user_query'][:100]}...")
        print(f"RAG Context: {iteration['rag_context']}")
        print(f"Expected Output: {iteration['expected_output']}")

def simulate_rag_retrieval():
    """Simulate RAG retrieval process."""
    print_step(6, "RAG RETRIEVAL PROCESS")
    
    print("For each iteration, RAG retrieval involves:")
    print("1. Taking the user query (original or 'continue research')")
    print("2. Searching the FAISS vector database for relevant code chunks")
    print("3. Ranking results by similarity")
    print("4. Returning top-k most relevant chunks")
    print("5. Formatting context with file path grouping")
    
    # Simulate retrieval results
    mock_retrieved_chunks = [
        {
            "file_path": "calculator.py",
            "content": "class Calculator:\n    def __init__(self):\n        self.history = []",
            "similarity_score": 0.95
        },
        {
            "file_path": "calculator.py", 
            "content": "def add(self, a: float, b: float) -> float:\n        result = a + b\n        self.history.append(f\"{a} + {b} = {result}\")\n        return result",
            "similarity_score": 0.92
        },
        {
            "file_path": "README.md",
            "content": "A basic calculator application built with Python that performs arithmetic operations.",
            "similarity_score": 0.88
        }
    ]
    
    print("\nMock retrieved chunks:")
    for i, chunk in enumerate(mock_retrieved_chunks, 1):
        print(f"{i}. File: {chunk['file_path']}")
        print(f"   Content: {chunk['content'][:100]}...")
        print(f"   Similarity: {chunk['similarity_score']}")

def simulate_websocket_communication():
    """Simulate WebSocket communication flow."""
    print_step(7, "WEBSOCKET COMMUNICATION FLOW")
    
    print("WebSocket communication involves:")
    print("1. Client sends initial request via WebSocket")
    print("2. Server processes request and starts DeepResearch")
    print("3. Server streams responses back to client")
    print("4. Client receives and displays streaming content")
    print("5. For subsequent iterations, client sends 'continue research'")
    print("6. Server continues with next iteration")
    
    print("\nKey WebSocket events:")
    print("- CONNECT: Client establishes WebSocket connection")
    print("- MESSAGE: Client sends request with [DEEP RESEARCH] tag")
    print("- STREAM: Server streams LLM response chunks")
    print("- CONTINUE: Client sends continue request for next iteration")
    print("- DISCONNECT: Client closes connection after completion")

def simulate_final_wiki_generation():
    """Simulate the final wiki generation."""
    print_step(8, "FINAL WIKI GENERATION")
    
    print("After 5 iterations, the system generates:")
    print("1. Structured wiki pages based on research findings")
    print("2. Mermaid diagrams for visual representations")
    print("3. Code examples and references")
    print("4. Navigation structure")
    print("5. Searchable content")
    
    mock_wiki_structure = {
        "pages": [
            {
                "title": "Overview",
                "content": "Project overview and basic information",
                "diagrams": []
            },
            {
                "title": "System Architecture", 
                "content": "Calculator class structure and design patterns",
                "diagrams": ["class_diagram"]
            },
            {
                "title": "Core Features",
                "content": "Arithmetic operations and error handling",
                "diagrams": ["flowchart"]
            },
            {
                "title": "API Reference",
                "content": "Method documentation and examples",
                "diagrams": []
            }
        ]
    }
    
    print("\nMock wiki structure:")
    print(json.dumps(mock_wiki_structure, indent=2))

def main():
    """Main demo function."""
    print("DEEPWIKI COMPLETE EXECUTION DEMO")
    print("=" * 60)
    print("This demo shows the complete DeepWiki execution flow")
    print("for the test calculator project.")
    
    # Step 1: File tree extraction
    file_tree = simulate_file_tree_extraction()
    
    # Step 2: README extraction  
    readme = simulate_readme_extraction()
    
    # Step 3: Initial user request construction
    request_body = simulate_initial_user_request(file_tree, readme)
    
    # Step 4: Code processing stage
    files_processed = simulate_code_processing()
    
    # Step 5: DeepResearch iterations
    simulate_deepresearch_iterations()
    
    # Step 6: RAG retrieval process
    simulate_rag_retrieval()
    
    # Step 7: WebSocket communication
    simulate_websocket_communication()
    
    # Step 8: Final wiki generation
    simulate_final_wiki_generation()
    
    print(f"\n{'='*60}")
    print("DEMO COMPLETED")
    print(f"{'='*60}")
    print("\nKey takeaways:")
    print("1. DeepWiki uses a multi-turn iterative process (DeepResearch)")
    print("2. Each iteration builds upon previous findings")
    print("3. RAG provides relevant code context for each iteration")
    print("4. WebSocket enables real-time streaming of responses")
    print("5. Final output is a structured, comprehensive wiki")

if __name__ == "__main__":
    main()
