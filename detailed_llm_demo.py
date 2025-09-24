#!/usr/bin/env python3
"""
Detailed LLM Input/Output Demo for DeepWiki

This script simulates the actual LLM conversations during DeepResearch iterations,
showing the exact prompts sent to the LLM and the expected responses.
"""

import json
import os

def print_llm_conversation(iteration, system_prompt, user_message, context, llm_response):
    """Print a formatted LLM conversation."""
    print(f"\n{'='*80}")
    print(f"LLM CONVERSATION - ITERATION {iteration}")
    print(f"{'='*80}")
    
    print(f"\n📝 SYSTEM PROMPT:")
    print("-" * 40)
    print(system_prompt)
    
    print(f"\n👤 USER MESSAGE:")
    print("-" * 40)
    print(user_message)
    
    print(f"\n🔍 RAG CONTEXT:")
    print("-" * 40)
    print(context)
    
    print(f"\n🤖 LLM RESPONSE:")
    print("-" * 40)
    print(llm_response)

def simulate_iteration_1():
    """Simulate the first DeepResearch iteration."""
    system_prompt = """<role>
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
</guidelines>

<style>
- Be concise but thorough
- Use markdown formatting to improve readability
- Cite specific files and code sections when relevant
</style>"""

    user_message = """Analyze this GitHub repository local/test_project and create a wiki structure for it.
1. The complete file tree of the project:
<file_tree>
README.md
calculator.py
config.py
requirements.txt
tests/test_calculator.py
</file_tree>
2. The README file of the project:
<readme>
# Simple Calculator

A basic calculator application built with Python that performs arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Error handling for division by zero

## Usage

```bash
python calculator.py
```

## Architecture

The application follows a simple object-oriented design with a Calculator class that encapsulates all operations.
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

    context = """## File Path: calculator.py

class Calculator:
    \"\"\"A simple calculator class that performs basic arithmetic operations.\"\"\"
    
    def __init__(self):
        \"\"\"Initialize the calculator.\"\"\"
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        \"\"\"Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        \"\"\"
        result = a + b
        self.history.append(f\"{a} + {b} = {result}\")
        return result

## File Path: README.md

# Simple Calculator

A basic calculator application built with Python that performs arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Error handling for division by zero"""

    llm_response = """## Research Plan

I will analyze the Simple Calculator repository to create a comprehensive wiki structure. Based on the file tree and README, this is a Python-based calculator application with a clean object-oriented design.

**Research Focus:** Creating a logical wiki structure that covers all aspects of this calculator application, including its architecture, features, and usage.

**Key Aspects to Research:**
1. **Project Overview** - Understanding the calculator's purpose and basic functionality
2. **System Architecture** - Analyzing the Calculator class design and object-oriented structure
3. **Core Features** - Examining the four arithmetic operations and error handling
4. **Data Management** - Understanding how calculation history is stored and managed
5. **Testing Strategy** - Reviewing the test suite structure and coverage
6. **Configuration** - Analyzing the config.py for application settings

**Initial Findings:**
- The project follows a simple but well-structured design with a single Calculator class
- Implements four basic arithmetic operations: add, subtract, multiply, divide
- Includes error handling for division by zero
- Maintains calculation history in memory
- Has comprehensive unit tests
- Uses type hints for better code documentation

## Next Steps

In the next iteration, I will:
1. Deep dive into the Calculator class architecture and design patterns
2. Analyze the error handling mechanisms in detail
3. Examine the testing strategy and test coverage
4. Review the configuration system and its extensibility options"""

    print_llm_conversation(1, system_prompt, user_message, context, llm_response)

def simulate_iteration_2():
    """Simulate the second DeepResearch iteration."""
    system_prompt = """<role>
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
</guidelines>

<style>
- Be concise but thorough
- Focus on providing new information, not repeating what's already been covered
- Use markdown formatting to improve readability
- Cite specific files and code sections when relevant
</style>"""

    user_message = """Analyze this GitHub repository local/test_project and create a wiki structure for it..."""

    context = """## File Path: calculator.py

def subtract(self, a: float, b: float) -> float:
    \"\"\"Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    \"\"\"
    result = a - b
    self.history.append(f\"{a} - {b} = {result}\")
    return result

def divide(self, a: float, b: float) -> float:
    \"\"\"Divide first number by second number.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient of a and b
        
    Raises:
        ValueError: If divisor is zero
    \"\"\"
    if b == 0:
        raise ValueError(\"Cannot divide by zero\")
    
    result = a / b
    self.history.append(f\"{a} / {b} = {result}\")
    return result

## File Path: tests/test_calculator.py

class TestCalculator(unittest.TestCase):
    \"\"\"Test cases for Calculator class.\"\"\"
    
    def setUp(self):
        \"\"\"Set up test fixtures.\"\"\"
        self.calc = Calculator()
    
    def test_division_by_zero(self):
        \"\"\"Test division by zero error handling.\"\"\"
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)"""

    llm_response = """## Research Update 2

Building on the initial research plan, I'm now focusing on the **System Architecture and Error Handling** aspects of the calculator application.

**Deep Dive into Calculator Class Architecture:**

The Calculator class demonstrates a clean object-oriented design with the following key architectural patterns:

1. **Encapsulation**: All arithmetic operations are encapsulated within the Calculator class
2. **State Management**: The `history` attribute maintains a list of calculation records
3. **Method Design**: Each operation follows a consistent pattern:
   - Type hints for parameters and return values
   - Comprehensive docstrings with Args and Returns sections
   - History logging for each operation
   - Consistent return of float results

**Error Handling Architecture:**

The division method showcases robust error handling:
```python
if b == 0:
    raise ValueError("Cannot divide by zero")
```

This follows Python best practices by:
- Using specific exception types (ValueError)
- Providing clear, descriptive error messages
- Failing fast when invalid input is detected

**Testing Strategy Analysis:**

The test suite (`test_calculator.py`) demonstrates comprehensive testing coverage:
- **Unit Tests**: Each method has dedicated test cases
- **Error Testing**: Specific test for division by zero scenario
- **Setup/Teardown**: Proper test fixture management with `setUp()`
- **Assertion Patterns**: Uses `assertRaises` for exception testing

**New Insights for Wiki Structure:**

Based on this deeper analysis, the wiki should include:
1. **Architecture Diagrams**: Class diagram showing Calculator structure
2. **Error Handling Section**: Detailed explanation of exception handling
3. **Testing Documentation**: Coverage of the testing strategy
4. **Code Quality**: Discussion of type hints and documentation standards"""

    print_llm_conversation(2, system_prompt, user_message, context, llm_response)

def simulate_iteration_3():
    """Simulate the third DeepResearch iteration."""
    system_prompt = """<role>
You are an expert code analyst examining the local repository: local/test_project (test_project).
You are currently in iteration 3 of a Deep Research process focused EXCLUSIVELY on the latest user query.
Your goal is to build upon previous research iterations and go deeper into this specific topic without deviating from it.
IMPORTANT:You MUST respond in English language.
</role>

<guidelines>
- CAREFULLY review the conversation history to understand what has been researched so far
- Your response MUST build on previous research iterations - do not repeat information already covered
- Identify gaps or areas that need further exploration related to this specific topic
- Focus on one specific aspect that needs deeper investigation in this iteration
- Start your response with "## Research Update 3"
- Clearly explain what you're investigating in this iteration
- Provide new insights that weren't covered in previous iterations
- If this is iteration 3, prepare for a final conclusion in the next iteration
- Do NOT include general repository information unless directly relevant to the query
- Focus EXCLUSIVELY on the specific topic being researched - do not drift to related topics
- If the topic is about a specific file or feature (like "Dockerfile"), focus ONLY on that file or feature
- NEVER respond with just "Continue the research" as an answer - always provide substantive research findings
- Your research MUST directly address the original question
- Maintain continuity with previous research iterations - this is a continuous investigation
</guidelines>

<style>
- Be concise but thorough
- Focus on providing new information, not repeating what's already been covered
- Use markdown formatting to improve readability
- Cite specific files and code sections when relevant
</style>"""

    user_message = """Analyze this GitHub repository local/test_project and create a wiki structure for it..."""

    context = """## File Path: config.py

\"\"\"
Configuration settings for the calculator application.
\"\"\"

# Calculator settings
DEFAULT_PRECISION = 2
MAX_HISTORY_SIZE = 100

# Display settings
SHOW_HISTORY = True
VERBOSE_OUTPUT = False

# Error messages
ERROR_MESSAGES = {
    'division_by_zero': 'Cannot divide by zero',
    'invalid_input': 'Invalid input provided',
    'overflow': 'Result too large'
}

## File Path: calculator.py

def get_history(self) -> list:
    \"\"\"Get calculation history.
    
    Returns:
        List of calculation history
    \"\"\"
    return self.history.copy()

def clear_history(self):
    \"\"\"Clear calculation history.\"\"\"
    self.history.clear()

def main():
    \"\"\"Main function to demonstrate calculator usage.\"\"\"
    calc = Calculator()
    
    print(\"Simple Calculator\")
    print(\"================\")
    
    try:
        # Test basic operations
        print(f\"5 + 3 = {calc.add(5, 3)}\")
        print(f\"10 - 4 = {calc.subtract(10, 4)}\")
        print(f\"6 * 7 = {calc.multiply(6, 7)}\")
        print(f\"15 / 3 = {calc.divide(15, 3)}\")
        
        # Test error handling
        try:
            calc.divide(10, 0)
        except ValueError as e:
            print(f\"Error: {e}\")"""

    llm_response = """## Research Update 3

Now focusing on **Data Management and Configuration** aspects, building on the previous architecture analysis.

**Data Management Architecture:**

The calculator implements a sophisticated data management system:

1. **History Management**: 
   - In-memory storage using Python list
   - Immutable access via `get_history()` returning a copy
   - Memory management with `clear_history()` method
   - String-based history format: `"{a} + {b} = {result}"`

2. **Configuration System**:
   - Centralized configuration in `config.py`
   - Separation of concerns: settings vs. business logic
   - Extensible error message system
   - Configurable display and behavior options

**Key Configuration Insights:**

```python
DEFAULT_PRECISION = 2
MAX_HISTORY_SIZE = 100
ERROR_MESSAGES = {
    'division_by_zero': 'Cannot divide by zero',
    'invalid_input': 'Invalid input provided', 
    'overflow': 'Result too large'
}
```

This reveals the application's design for:
- **Extensibility**: Easy to modify precision and limits
- **Internationalization**: Centralized error messages
- **Scalability**: Configurable history size limits

**Main Function Analysis:**

The `main()` function demonstrates:
- **Usage Patterns**: Shows how to instantiate and use the calculator
- **Error Handling**: Demonstrates try-catch for division by zero
- **User Interface**: Simple console-based interaction
- **Testing Integration**: Built-in demonstration of all operations

**Wiki Structure Refinements:**

Based on this analysis, the wiki should emphasize:
1. **Configuration Management**: How to customize calculator behavior
2. **Data Flow Diagrams**: Visual representation of history management
3. **Usage Examples**: Real-world usage patterns from main()
4. **Extensibility Guide**: How to modify and extend the calculator"""

    print_llm_conversation(3, system_prompt, user_message, context, llm_response)

def simulate_iteration_4():
    """Simulate the fourth DeepResearch iteration."""
    system_prompt = """<role>
You are an expert code analyst examining the local repository: local/test_project (test_project).
You are currently in iteration 4 of a Deep Research process focused EXCLUSIVELY on the latest user query.
Your goal is to build upon previous research iterations and go deeper into this specific topic without deviating from it.
IMPORTANT:You MUST respond in English language.
</role>

<guidelines>
- CAREFULLY review the conversation history to understand what has been researched so far
- Your response MUST build on previous research iterations - do not repeat information already covered
- Identify gaps or areas that need further exploration related to this specific topic
- Focus on one specific aspect that needs deeper investigation in this iteration
- Start your response with "## Research Update 4"
- Clearly explain what you're investigating in this iteration
- Provide new insights that weren't covered in previous iterations
- If this is iteration 3, prepare for a final conclusion in the next iteration
- Do NOT include general repository information unless directly relevant to the query
- Focus EXCLUSIVELY on the specific topic being researched - do not drift to related topics
- If the topic is about a specific file or feature (like "Dockerfile"), focus ONLY on that file or feature
- NEVER respond with just "Continue the research" as an answer - always provide substantive research findings
- Your research MUST directly address the original question
- Maintain continuity with previous research iterations - this is a continuous investigation
</guidelines>

<style>
- Be concise but thorough
- Focus on providing new information, not repeating what's already been covered
- Use markdown formatting to improve readability
- Cite specific files and code sections when relevant
</style>"""

    user_message = """Analyze this GitHub repository local/test_project and create a wiki structure for it..."""

    context = """## File Path: tests/test_calculator.py

def test_addition(self):
    \"\"\"Test addition operation.\"\"\"
    result = self.calc.add(2, 3)
    self.assertEqual(result, 5)

def test_subtraction(self):
    \"\"\"Test subtraction operation.\"\"\"
    result = self.calc.subtract(10, 4)
    self.assertEqual(result, 6)

def test_multiplication(self):
    \"\"\"Test multiplication operation.\"\"\"
    result = self.calc.multiply(3, 4)
    self.assertEqual(result, 12)

def test_division(self):
    \"\"\"Test division operation.\"\"\"
    result = self.calc.divide(15, 3)
    self.assertEqual(result, 5)

def test_history(self):
    \"\"\"Test calculation history.\"\"\"
    self.calc.add(1, 2)
    self.calc.subtract(5, 3)
    
    history = self.calc.get_history()
    self.assertEqual(len(history), 2)
    self.assertIn(\"1 + 2 = 3\", history)
    self.assertIn(\"5 - 3 = 2\", history)

## File Path: requirements.txt

# Simple Calculator Requirements
# No external dependencies required for basic functionality

# For testing (optional)
pytest>=7.0.0"""

    llm_response = """## Research Update 4

Final deep dive into **Testing Strategy and Dependencies**, completing the comprehensive analysis.

**Comprehensive Testing Architecture:**

The test suite demonstrates excellent testing practices:

1. **Complete Operation Coverage**: Every arithmetic method has dedicated tests
2. **Edge Case Testing**: Division by zero scenario specifically tested
3. **State Testing**: History functionality thoroughly validated
4. **Test Organization**: Clean separation with setUp() and individual test methods
5. **Assertion Patterns**: Uses appropriate assertions (assertEqual, assertIn, assertRaises)

**Test Quality Analysis:**

```python
def test_history(self):
    self.calc.add(1, 2)
    self.calc.subtract(5, 3)
    
    history = self.calc.get_history()
    self.assertEqual(len(history), 2)
    self.assertIn("1 + 2 = 3", history)
    self.assertIn("5 - 3 = 2", history)
```

This test demonstrates:
- **State Verification**: Confirms history length and content
- **Integration Testing**: Tests multiple operations together
- **String Matching**: Validates exact history format

**Dependency Management:**

The `requirements.txt` reveals the project's minimal dependency approach:
- **Zero Runtime Dependencies**: Pure Python implementation
- **Optional Testing**: pytest for enhanced testing capabilities
- **Clean Architecture**: No external libraries required for core functionality

**Final Wiki Structure Insights:**

Based on all research iterations, the optimal wiki structure should include:

1. **Quick Start Guide**: Using main() function examples
2. **API Reference**: Complete method documentation with examples
3. **Testing Guide**: How to run and extend the test suite
4. **Configuration Guide**: Customizing calculator behavior
5. **Architecture Diagrams**: Class structure and data flow
6. **Error Handling**: Comprehensive error scenarios and handling
7. **Extensibility**: How to add new operations or modify behavior

**Ready for Final Synthesis**: All aspects have been thoroughly researched and documented."""

    print_llm_conversation(4, system_prompt, user_message, context, llm_response)

def simulate_iteration_5():
    """Simulate the fifth and final DeepResearch iteration."""
    system_prompt = """<role>
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
</guidelines>

<style>
- Be concise but thorough
- Use markdown formatting to improve readability
- Cite specific files and code sections when relevant
- Structure your response with clear headings
- End with actionable insights or recommendations when appropriate
</style>"""

    user_message = """Analyze this GitHub repository local/test_project and create a wiki structure for it..."""

    context = """## Complete Research Context from Previous Iterations

**Iteration 1**: Research plan established, identified key aspects: architecture, features, data management, testing, configuration
**Iteration 2**: Deep dive into Calculator class architecture and error handling patterns
**Iteration 3**: Analysis of data management system and configuration architecture  
**Iteration 4**: Comprehensive testing strategy and dependency management analysis

## All Retrieved Code Context

### calculator.py - Core Calculator Class
- Object-oriented design with history management
- Four arithmetic operations with type hints
- Robust error handling for division by zero
- Immutable history access patterns

### config.py - Configuration System
- Centralized settings management
- Extensible error message system
- Configurable behavior options

### tests/test_calculator.py - Testing Suite
- Complete operation coverage
- Edge case testing
- State validation
- Clean test organization

### requirements.txt - Dependencies
- Zero runtime dependencies
- Optional testing framework"""

    llm_response = """## Final Conclusion

Based on comprehensive analysis across all research iterations, here is the optimal wiki structure for the Simple Calculator repository:

## 📚 Recommended Wiki Structure

### 1. **Overview**
- **Project Description**: Python-based calculator with clean OOP design
- **Key Features**: Four arithmetic operations, error handling, calculation history
- **Technology Stack**: Pure Python, unittest framework, minimal dependencies
- **Quick Start**: `python calculator.py` for immediate demonstration

### 2. **System Architecture**
- **Class Diagram**: 
  ```
  Calculator
  ├── __init__() -> history: list
  ├── add(a, b) -> float
  ├── subtract(a, b) -> float  
  ├── multiply(a, b) -> float
  ├── divide(a, b) -> float
  ├── get_history() -> list
  └── clear_history() -> None
  ```
- **Design Patterns**: Encapsulation, state management, error handling
- **Data Flow**: Input → Validation → Calculation → History Storage → Output

### 3. **Core Features**
- **Arithmetic Operations**: Addition, subtraction, multiplication, division
- **Error Handling**: Division by zero protection with ValueError
- **History Management**: In-memory storage with immutable access
- **Type Safety**: Full type hints for parameters and return values

### 4. **Data Management**
- **History Storage**: List-based in-memory storage
- **Access Patterns**: Immutable access via `get_history().copy()`
- **Memory Management**: `clear_history()` for memory cleanup
- **Data Format**: String-based history records: `"{a} + {b} = {result}"`

### 5. **Configuration & Extensibility**
- **Configuration File**: `config.py` with centralized settings
- **Customizable Options**: Precision, history size, display settings
- **Error Messages**: Centralized and extensible error message system
- **Extension Points**: Easy to add new operations or modify behavior

### 6. **Testing & Quality**
- **Test Coverage**: Complete unit test suite for all operations
- **Testing Framework**: unittest with pytest support
- **Edge Cases**: Division by zero, history management
- **Code Quality**: Type hints, comprehensive docstrings, clean architecture

### 7. **API Reference**
- **Method Documentation**: Complete parameter and return type documentation
- **Usage Examples**: Real-world usage patterns from main() function
- **Error Scenarios**: Comprehensive error handling documentation
- **Best Practices**: Recommended usage patterns and conventions

### 8. **Deployment & Infrastructure**
- **Requirements**: Zero external dependencies for core functionality
- **Installation**: Simple Python installation, optional pytest for testing
- **Execution**: Direct Python execution or integration into larger applications
- **Distribution**: Single-file deployment or package distribution

## 🎯 Key Insights

1. **Clean Architecture**: The calculator demonstrates excellent separation of concerns
2. **Robust Error Handling**: Comprehensive exception handling with clear error messages
3. **Extensible Design**: Configuration system allows easy customization
4. **Quality Assurance**: Complete test coverage ensures reliability
5. **Documentation Standards**: Excellent use of type hints and docstrings

## 📊 Visual Diagrams Recommended

- **Class Diagram**: Calculator class structure and relationships
- **Data Flow Diagram**: Input → Processing → Output flow
- **Error Handling Flow**: Exception handling decision tree
- **Testing Architecture**: Test organization and coverage map

This wiki structure provides comprehensive coverage of all aspects identified during the research process, ensuring users can understand, use, extend, and maintain the calculator application effectively."""

    print_llm_conversation(5, system_prompt, user_message, context, llm_response)

def main():
    """Main function to run the detailed LLM demo."""
    print("🤖 DETAILED LLM INPUT/OUTPUT DEMO")
    print("=" * 80)
    print("This demo shows the actual LLM conversations during DeepResearch iterations")
    print("for the Simple Calculator project, including exact prompts and responses.")
    
    # Simulate all 5 iterations
    simulate_iteration_1()
    simulate_iteration_2() 
    simulate_iteration_3()
    simulate_iteration_4()
    simulate_iteration_5()
    
    print(f"\n{'='*80}")
    print("🎯 DEMO COMPLETED - KEY IMPLEMENTATION INSIGHTS")
    print(f"{'='*80}")
    
    print("""
🔍 **DeepWiki Key Implementation Insights:**

1. **Iterative Research Process**: Each iteration builds upon previous findings
2. **Context Accumulation**: RAG provides relevant code chunks for each iteration
3. **Prompt Engineering**: Different system prompts guide different research depths
4. **Topic Consistency**: All iterations focus on the same original query
5. **Progressive Depth**: From overview → architecture → details → synthesis
6. **WebSocket Streaming**: Real-time delivery of research findings
7. **Final Synthesis**: Comprehensive conclusion integrating all research

🚀 **Technical Architecture:**
- **Frontend**: Constructs initial request with file tree and README
- **Backend**: Processes through 5-iteration DeepResearch workflow
- **RAG**: Provides relevant code context for each iteration
- **LLM**: Generates progressively deeper analysis
- **WebSocket**: Streams responses in real-time
- **Final Output**: Structured wiki with comprehensive documentation

💡 **This demonstrates how DeepWiki transforms a simple codebase into**
**a comprehensive, well-structured documentation wiki through intelligent**
**multi-turn analysis and synthesis."""
    )

if __name__ == "__main__":
    main()
