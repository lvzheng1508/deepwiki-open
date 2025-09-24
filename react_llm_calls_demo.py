#!/usr/bin/env python3
"""
DeepWiki ReAct (DeepResearch) 完整LLM调用记录演示
展示5轮迭代中每次LLM调用的详细输入和输出
"""

import os
import json
from datetime import datetime

def print_separator(title):
    print("\n" + "="*80)
    print(f" {title}")
    print("="*80)

def print_llm_call(iteration, call_type, input_data, output_data):
    print(f"\n【第{iteration}轮 - {call_type}】")
    print("-" * 60)
    print("📥 LLM输入:")
    print(input_data)
    print("\n📤 LLM输出:")
    print(output_data)
    print("-" * 60)

def main():
    print_separator("DeepWiki ReAct (DeepResearch) 完整LLM调用记录")
    
    # 项目路径信息
    project_path = "/Users/lvzheng/cursor/deepwiki-open/test_project"
    print(f"📁 测试项目路径: {project_path}")
    print(f"📁 项目结构:")
    print("""
test_project/
├── README.md
├── src/
│   ├── main.py
│   ├── utils.py
│   └── models/
│       └── user.py
├── tests/
│   └── test_main.py
└── requirements.txt
    """)
    
    # 模拟RAG检索的代码片段
    rag_contexts = {
        1: """
<context>
<file path="src/main.py">
def main():
    \"\"\"主程序入口\"\"\"
    print("Hello, World!")
    user = create_user("Alice", 25)
    print(f"Created user: {user.name}")

def create_user(name, age):
    \"\"\"创建用户对象\"\"\"
    from models.user import User
    return User(name, age)
</file>

<file path="src/models/user.py">
class User:
    \"\"\"用户模型类\"\"\"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        \"\"\"获取用户信息\"\"\"
        return f"{self.name}, {self.age} years old"
</file>
</context>
        """,
        2: """
<context>
<file path="src/utils.py">
def validate_user(user):
    \"\"\"验证用户数据\"\"\"
    if not user.name:
        return False
    if user.age < 0 or user.age > 150:
        return False
    return True

def format_user_info(user):
    \"\"\"格式化用户信息\"\"\"
    return f"User: {user.name} (Age: {user.age})"
</file>

<file path="tests/test_main.py">
import unittest
from src.main import create_user
from src.models.user import User

class TestMain(unittest.TestCase):
    def test_create_user(self):
        user = create_user("Bob", 30)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.age, 30)
</file>
</context>
        """,
        3: """
<context>
<file path="requirements.txt">
requests==2.28.1
pytest==7.2.0
flask==2.2.2
</file>

<file path="README.md">
# Test Project

这是一个简单的Python项目，用于演示用户管理功能。

## 功能特性
- 用户创建和管理
- 数据验证
- 单元测试

## 安装
pip install -r requirements.txt

## 运行
python src/main.py
</file>
</context>
        """,
        4: """
<context>
<file path="src/main.py">
def main():
    \"\"\"主程序入口\"\"\"
    print("Hello, World!")
    user = create_user("Alice", 25)
    print(f"Created user: {user.name}")

def create_user(name, age):
    \"\"\"创建用户对象\"\"\"
    from models.user import User
    return User(name, age)
</file>

<file path="src/models/user.py">
class User:
    \"\"\"用户模型类\"\"\"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        \"\"\"获取用户信息\"\"\"
        return f"{self.name}, {self.age} years old"
</file>
</context>
        """,
        5: """
<context>
<file path="src/main.py">
def main():
    \"\"\"主程序入口\"\"\"
    print("Hello, World!")
    user = create_user("Alice", 25)
    print(f"Created user: {user.name}")

def create_user(name, age):
    \"\"\"创建用户对象\"\"\"
    from models.user import User
    return User(name, age)
</file>

<file path="src/models/user.py">
class User:
    \"\"\"用户模型类\"\"\"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        \"\"\"获取用户信息\"\"\"
        return f"{self.name}, {self.age} years old"
</file>

<file path="src/utils.py">
def validate_user(user):
    \"\"\"验证用户数据\"\"\"
    if not user.name:
        return False
    if user.age < 0 or user.age > 150:
        return False
    return True
</file>
</context>
        """
    }
    
    # 模拟对话历史
    conversation_history = ""
    
    # 第1轮：研究计划
    print_separator("第1轮：研究计划 (Research Plan)")
    
    system_prompt_1 = """You are an expert software engineer and technical writer. Your task is to analyze a GitHub repository and create a comprehensive wiki structure.

**IMPORTANT INSTRUCTIONS:**
1. **Language Detection**: Detect the primary programming language(s) used in the repository
2. **Markdown Formatting**: Use proper markdown syntax with headers, code blocks, and lists
3. **Structured Thinking**: Organize your analysis into clear sections
4. **Code Examples**: Include relevant code snippets when explaining functionality
5. **Architecture Overview**: Provide a high-level view of the system architecture

**Your Response Format:**
- Start with a brief repository overview
- Identify key components and their relationships
- Suggest a wiki structure with main sections
- Highlight important files and their purposes
- Note any patterns or architectural decisions

Remember: Focus on creating a research plan for comprehensive analysis, not the final wiki content."""
    
    user_message_1 = """Analyze this GitHub repository test_project and create a wiki structure that covers:

1. **Project Overview**: Purpose, main features, and key technologies
2. **Architecture**: System design, components, and data flow
3. **Code Structure**: Directory organization and file purposes
4. **API Documentation**: Function signatures, parameters, and return values
5. **Usage Examples**: How to use the main features
6. **Development Guide**: Setup, testing, and contribution guidelines

Please provide a comprehensive analysis and suggest a detailed wiki structure.

**File Tree:**
```
test_project/
├── README.md
├── src/
│   ├── main.py
│   ├── utils.py
│   └── models/
│       └── user.py
├── tests/
│   └── test_main.py
└── requirements.txt
```

**README Content:**
# Test Project

这是一个简单的Python项目，用于演示用户管理功能。

## 功能特性
- 用户创建和管理
- 数据验证
- 单元测试

## 安装
pip install -r requirements.txt

## 运行
python src/main.py"""
    
    llm_input_1 = f"{system_prompt_1}\n\n{rag_contexts[1]}\n\n{user_message_1}"
    llm_output_1 = """# Research Plan for test_project

## Repository Overview
This is a Python-based user management system with a clean, modular architecture. The project demonstrates basic object-oriented programming principles and includes testing infrastructure.

## Key Components Analysis

### 1. Core Architecture
- **Entry Point**: `src/main.py` - Contains the main application logic
- **Data Models**: `src/models/user.py` - Defines the User class with basic properties
- **Utilities**: `src/utils.py` - Provides validation and formatting functions
- **Testing**: `tests/test_main.py` - Unit tests for core functionality

### 2. Technology Stack
- **Language**: Python 3.x
- **Dependencies**: requests, pytest, flask (from requirements.txt)
- **Testing Framework**: unittest/pytest

### 3. Suggested Wiki Structure

#### A. Project Overview
- Purpose and goals
- Key features
- Technology stack
- Installation and setup

#### B. Architecture Documentation
- System design overview
- Component relationships
- Data flow diagrams
- Module dependencies

#### C. Code Documentation
- API reference for all modules
- Function signatures and parameters
- Usage examples
- Code patterns and conventions

#### D. Development Guide
- Setup instructions
- Testing procedures
- Contribution guidelines
- Code style standards

## Research Focus Areas
1. **User Model Analysis**: Understanding the User class structure and methods
2. **Main Application Flow**: Tracing the execution path from main() to user creation
3. **Utility Functions**: Examining validation and formatting logic
4. **Test Coverage**: Analyzing test cases and coverage areas
5. **Dependency Management**: Understanding external library usage

## Next Steps
- Deep dive into each component's implementation
- Analyze code patterns and best practices
- Document API interfaces and usage examples
- Create comprehensive usage documentation"""
    
    print_llm_call(1, "研究计划", llm_input_1, llm_output_1)
    
    # 更新对话历史
    conversation_history = f"""<conversation_history>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_1}</assistant>
</conversation_history>"""
    
    # 第2轮：研究更新
    print_separator("第2轮：研究更新 (Research Update)")
    
    system_prompt_2 = """You are an expert software engineer and technical writer. Your task is to analyze a GitHub repository and create a comprehensive wiki structure.

**IMPORTANT INSTRUCTIONS:**
1. **Language Detection**: Detect the primary programming language(s) used in the repository
2. **Markdown Formatting**: Use proper markdown syntax with headers, code blocks, and lists
3. **Structured Thinking**: Organize your analysis into clear sections
4. **Code Examples**: Include relevant code snippets when explaining functionality
5. **Architecture Overview**: Provide a high-level view of the system architecture

**Your Response Format:**
- Build upon previous findings
- Provide detailed analysis of specific components
- Include code examples and explanations
- Identify patterns and architectural decisions
- Suggest improvements or highlight best practices

Remember: This is a research update - deepen the analysis based on previous findings."""
    
    user_message_2 = """Analyze this GitHub repository test_project and create a wiki structure that covers:

1. **Project Overview**: Purpose, main features, and key technologies
2. **Architecture**: System design, components, and data flow
3. **Code Structure**: Directory organization and file purposes
4. **API Documentation**: Function signatures, parameters, and return values
5. **Usage Examples**: How to use the main features
6. **Development Guide**: Setup, testing, and contribution guidelines

Please provide a comprehensive analysis and suggest a detailed wiki structure.

**File Tree:**
```
test_project/
├── README.md
├── src/
│   ├── main.py
│   ├── utils.py
│   └── models/
│       └── user.py
├── tests/
│   └── test_main.py
└── requirements.txt
```

**README Content:**
# Test Project

这是一个简单的Python项目，用于演示用户管理功能。

## 功能特性
- 用户创建和管理
- 数据验证
- 单元测试

## 安装
pip install -r requirements.txt

## 运行
python src/main.py"""
    
    llm_input_2 = f"{system_prompt_2}\n\n{conversation_history}\n\n{rag_contexts[2]}\n\n{user_message_2}"
    llm_output_2 = """# Research Update: Detailed Component Analysis

## Deep Dive into Core Components

### 1. User Model Analysis (`src/models/user.py`)

The User class represents the core data model with the following characteristics:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name}, {self.age} years old"
```

**Key Observations:**
- Simple data class with two properties: name and age
- Includes a utility method `get_info()` for formatted output
- No validation logic in the model itself (separation of concerns)
- Follows Python naming conventions

### 2. Utility Functions Analysis (`src/utils.py`)

The utility module provides two key functions:

```python
def validate_user(user):
    if not user.name:
        return False
    if user.age < 0 or user.age > 150:
        return False
    return True

def format_user_info(user):
    return f"User: {user.name} (Age: {user.age})"
```

**Architectural Patterns:**
- **Separation of Concerns**: Validation logic separated from the model
- **Single Responsibility**: Each function has a clear, single purpose
- **Input Validation**: Comprehensive validation for user data
- **Consistent Formatting**: Standardized output format

### 3. Main Application Flow (`src/main.py`)

The main application demonstrates a clean execution flow:

```python
def main():
    print("Hello, World!")
    user = create_user("Alice", 25)
    print(f"Created user: {user.name}")

def create_user(name, age):
    from models.user import User
    return User(name, age)
```

**Design Patterns:**
- **Factory Pattern**: `create_user()` acts as a factory function
- **Dependency Injection**: User creation is abstracted
- **Clear Entry Point**: `main()` function provides clear application start

### 4. Testing Infrastructure (`tests/test_main.py`)

The test suite demonstrates good testing practices:

```python
class TestMain(unittest.TestCase):
    def test_create_user(self):
        user = create_user("Bob", 30)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.age, 30)
```

**Testing Patterns:**
- **Unit Testing**: Focused on individual functions
- **Assertion Coverage**: Tests both type and value correctness
- **Clear Test Names**: Descriptive test method names
- **Isolated Tests**: Each test is independent

## Updated Wiki Structure

### A. Project Overview
- **Purpose**: Simple user management demonstration
- **Key Features**: User creation, validation, formatting
- **Technology Stack**: Python 3.x, unittest, pytest
- **Target Audience**: Learning Python OOP concepts

### B. Architecture Documentation
- **Component Diagram**: User Model ↔ Utils ↔ Main
- **Data Flow**: Input → Validation → Creation → Formatting
- **Design Patterns**: Factory, Separation of Concerns
- **Module Dependencies**: Clear import structure

### C. API Reference
- **User Class**: Constructor, get_info() method
- **Utility Functions**: validate_user(), format_user_info()
- **Main Functions**: main(), create_user()
- **Parameter Specifications**: Type hints and validation rules

### D. Usage Examples
- **Basic Usage**: Creating and validating users
- **Error Handling**: Invalid input scenarios
- **Testing**: Running unit tests
- **Integration**: End-to-end workflow

## Next Research Areas
1. **Error Handling**: How the system handles invalid inputs
2. **Extensibility**: Potential for adding new user properties
3. **Performance**: Memory usage and execution efficiency
4. **Security**: Input sanitization and validation
5. **Documentation**: Code comments and docstring quality"""
    
    print_llm_call(2, "研究更新", llm_input_2, llm_output_2)
    
    # 更新对话历史
    conversation_history = f"""<conversation_history>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_1}</assistant>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_2}</assistant>
</conversation_history>"""
    
    # 第3轮：研究更新
    print_separator("第3轮：研究更新 (Research Update)")
    
    llm_input_3 = f"{system_prompt_2}\n\n{conversation_history}\n\n{rag_contexts[3]}\n\n{user_message_2}"
    llm_output_3 = """# Research Update: Dependencies and Project Configuration

## Dependency Analysis (`requirements.txt`)

The project dependencies reveal the intended use cases:

```
requests==2.28.1
pytest==7.2.0
flask==2.2.2
```

**Dependency Analysis:**
- **requests**: HTTP client library (not currently used in core code)
- **pytest**: Modern testing framework (alternative to unittest)
- **flask**: Web framework (suggests potential web interface)

**Implications:**
- Project is designed for web application development
- Modern testing practices with pytest
- HTTP communication capabilities available
- Potential for API development

## README Analysis

The README provides clear project documentation:

```markdown
# Test Project

这是一个简单的Python项目，用于演示用户管理功能。

## 功能特性
- 用户创建和管理
- 数据验证
- 单元测试

## 安装
pip install -r requirements.txt

## 运行
python src/main.py
```

**Documentation Quality:**
- **Multilingual**: Chinese description with English commands
- **Clear Structure**: Features, installation, usage
- **Practical Instructions**: Step-by-step setup guide
- **Feature Overview**: Concise feature list

## Enhanced Architecture Understanding

### 1. Project Scope
- **Current State**: Standalone console application
- **Potential Expansion**: Web application with Flask
- **Testing Strategy**: Both unittest and pytest support
- **External Integration**: HTTP capabilities via requests

### 2. Development Workflow
- **Setup**: `pip install -r requirements.txt`
- **Execution**: `python src/main.py`
- **Testing**: pytest or unittest
- **Web Development**: Flask integration ready

### 3. Code Quality Indicators
- **Dependencies**: Modern, well-maintained libraries
- **Version Pinning**: Specific versions for reproducibility
- **Testing**: Comprehensive testing framework
- **Documentation**: Clear README with usage instructions

## Updated Wiki Structure

### A. Project Overview
- **Purpose**: User management system with web potential
- **Key Features**: User CRUD, validation, testing, web-ready
- **Technology Stack**: Python 3.x, Flask, pytest, requests
- **Development Status**: Core functionality complete, web features planned

### B. Architecture Documentation
- **Current Architecture**: Console application with modular design
- **Future Architecture**: Web application with API endpoints
- **Component Relationships**: User Model ↔ Utils ↔ Main ↔ Web Layer
- **Data Flow**: Input → Validation → Processing → Output/API Response

### C. API Reference
- **Core API**: User creation, validation, formatting
- **Future API**: REST endpoints for user management
- **Testing API**: Unit test interfaces
- **External API**: HTTP client capabilities

### D. Development Guide
- **Environment Setup**: Python 3.x, pip, virtual environment
- **Dependency Management**: requirements.txt, version pinning
- **Testing**: pytest configuration, test discovery
- **Web Development**: Flask integration, API development
- **Deployment**: Production considerations

## Research Insights
1. **Scalability**: Architecture supports web application expansion
2. **Testing**: Comprehensive testing strategy with multiple frameworks
3. **Documentation**: Good documentation practices
4. **Modern Practices**: Up-to-date dependencies and tools
5. **Internationalization**: Multilingual documentation support

## Next Research Areas
1. **Web Integration**: How Flask would integrate with current architecture
2. **API Design**: RESTful endpoint structure
3. **Testing Strategy**: pytest vs unittest usage patterns
4. **Deployment**: Production deployment considerations
5. **Performance**: Scalability and optimization opportunities"""
    
    print_llm_call(3, "研究更新", llm_input_3, llm_output_3)
    
    # 更新对话历史
    conversation_history = f"""<conversation_history>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_1}</assistant>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_2}</assistant>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_3}</assistant>
</conversation_history>"""
    
    # 第4轮：研究更新
    print_separator("第4轮：研究更新 (Research Update)")
    
    llm_input_4 = f"{system_prompt_2}\n\n{conversation_history}\n\n{rag_contexts[4]}\n\n{user_message_2}"
    llm_output_4 = """# Research Update: Code Quality and Best Practices

## Code Quality Analysis

### 1. Code Organization and Structure

The project demonstrates excellent code organization:

```
src/
├── main.py          # Application entry point
├── utils.py         # Utility functions
└── models/
    └── user.py      # Data models
```

**Best Practices Observed:**
- **Separation of Concerns**: Clear separation between models, utilities, and main logic
- **Modular Design**: Each module has a single responsibility
- **Logical Grouping**: Related functionality grouped together
- **Clean Imports**: Minimal, necessary imports only

### 2. Code Documentation Quality

**Docstring Analysis:**
```python
def main():
    \"\"\"主程序入口\"\"\"
    # Implementation

def create_user(name, age):
    \"\"\"创建用户对象\"\"\"
    # Implementation

class User:
    \"\"\"用户模型类\"\"\"
    # Implementation
```

**Documentation Strengths:**
- **Consistent Style**: All functions have docstrings
- **Multilingual**: Chinese docstrings for clarity
- **Concise**: Brief but descriptive
- **Complete Coverage**: All public methods documented

### 3. Error Handling and Validation

The validation logic demonstrates robust error handling:

```python
def validate_user(user):
    if not user.name:
        return False
    if user.age < 0 or user.age > 150:
        return False
    return True
```

**Validation Patterns:**
- **Input Validation**: Comprehensive validation rules
- **Boundary Testing**: Age limits (0-150)
- **Null Safety**: Name existence check
- **Return Values**: Clear boolean responses

### 4. Testing Strategy

The test suite shows good testing practices:

```python
class TestMain(unittest.TestCase):
    def test_create_user(self):
        user = create_user("Bob", 30)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.age, 30)
```

**Testing Best Practices:**
- **Unit Testing**: Focused on individual functions
- **Type Checking**: isinstance() validation
- **Value Assertions**: Specific value testing
- **Clear Test Names**: Descriptive method names
- **Isolated Tests**: Independent test cases

## Architecture Patterns

### 1. Factory Pattern Implementation
```python
def create_user(name, age):
    from models.user import User
    return User(name, age)
```

**Benefits:**
- **Encapsulation**: User creation logic centralized
- **Flexibility**: Easy to modify creation logic
- **Testability**: Easy to mock and test
- **Consistency**: Standardized object creation

### 2. Separation of Concerns
- **Models**: Data structure and basic methods
- **Utils**: Business logic and validation
- **Main**: Application flow and coordination
- **Tests**: Verification and quality assurance

### 3. Dependency Management
- **Lazy Imports**: Import only when needed
- **Minimal Dependencies**: Only necessary external libraries
- **Version Control**: Pinned dependency versions
- **Clear Requirements**: Explicit dependency list

## Enhanced Wiki Structure

### A. Project Overview
- **Purpose**: Well-structured user management system
- **Key Features**: Modular design, comprehensive testing, web-ready
- **Technology Stack**: Python 3.x, Flask, pytest, requests
- **Code Quality**: High-quality, well-documented codebase

### B. Architecture Documentation
- **Design Patterns**: Factory, Separation of Concerns
- **Code Organization**: Modular, hierarchical structure
- **Dependency Management**: Clean, minimal dependencies
- **Testing Strategy**: Comprehensive unit testing

### C. Code Quality Guide
- **Documentation Standards**: Docstring conventions
- **Code Style**: Python best practices
- **Testing Practices**: Unit testing patterns
- **Error Handling**: Validation and error management

### D. Development Workflow
- **Setup**: Environment configuration
- **Development**: Code organization and patterns
- **Testing**: Test-driven development
- **Quality Assurance**: Code review and validation

## Research Insights
1. **Code Quality**: High-quality, professional codebase
2. **Best Practices**: Follows Python and software engineering best practices
3. **Maintainability**: Well-structured, easy to maintain and extend
4. **Testability**: Comprehensive testing strategy
5. **Documentation**: Good documentation practices

## Next Research Areas
1. **Performance Analysis**: Code efficiency and optimization
2. **Security Considerations**: Input validation and security
3. **Scalability**: Architecture scalability and performance
4. **Integration**: External system integration patterns
5. **Deployment**: Production deployment and monitoring"""
    
    print_llm_call(4, "研究更新", llm_input_4, llm_output_4)
    
    # 更新对话历史
    conversation_history = f"""<conversation_history>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_1}</assistant>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_2}</assistant>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_3}</assistant>
<user>Analyze this GitHub repository test_project and create a wiki structure...</user>
<assistant>{llm_output_4}</assistant>
</conversation_history>"""
    
    # 第5轮：最终结论
    print_separator("第5轮：最终结论 (Final Conclusion)")
    
    system_prompt_5 = """You are an expert software engineer and technical writer. Your task is to analyze a GitHub repository and create a comprehensive wiki structure.

**IMPORTANT INSTRUCTIONS:**
1. **Language Detection**: Detect the primary programming language(s) used in the repository
2. **Markdown Formatting**: Use proper markdown syntax with headers, code blocks, and lists
3. **Structured Thinking**: Organize your analysis into clear sections
4. **Code Examples**: Include relevant code snippets when explaining functionality
5. **Architecture Overview**: Provide a high-level view of the system architecture

**Your Response Format:**
- Synthesize all previous findings
- Provide comprehensive final analysis
- Create complete wiki structure
- Include all necessary documentation sections
- Ensure completeness and accuracy

Remember: This is the final conclusion - provide a complete, comprehensive wiki structure."""
    
    llm_input_5 = f"{system_prompt_5}\n\n{conversation_history}\n\n{rag_contexts[5]}\n\n{user_message_2}"
    llm_output_5 = """# Final Wiki Structure for test_project

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Code Structure](#code-structure)
4. [API Documentation](#api-documentation)
5. [Usage Examples](#usage-examples)
6. [Development Guide](#development-guide)
7. [Testing](#testing)
8. [Dependencies](#dependencies)
9. [Contributing](#contributing)

---

## 🎯 Project Overview

### Purpose
A simple Python-based user management system designed to demonstrate object-oriented programming principles, modular architecture, and best practices in software development.

### Key Features
- **User Creation**: Simple user object creation with name and age
- **Data Validation**: Comprehensive input validation for user data
- **Modular Design**: Clean separation of concerns across modules
- **Testing**: Comprehensive unit testing with unittest framework
- **Web-Ready**: Flask integration ready for web application development

### Technology Stack
- **Language**: Python 3.x
- **Web Framework**: Flask 2.2.2
- **Testing**: pytest 7.2.0, unittest
- **HTTP Client**: requests 2.28.1
- **Package Management**: pip, requirements.txt

---

## 🏗️ Architecture

### System Design
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Main Module   │───▶│  Utility Module │───▶│   User Model    │
│   (main.py)     │    │   (utils.py)    │    │  (user.py)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Application    │    │   Validation    │    │   Data Storage  │
│     Flow        │    │   & Formatting  │    │   & Methods     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Design Patterns
- **Factory Pattern**: `create_user()` function for object creation
- **Separation of Concerns**: Clear module responsibilities
- **Single Responsibility**: Each function has one clear purpose
- **Dependency Injection**: Modular import structure

### Data Flow
1. **Input**: User provides name and age
2. **Validation**: Utility functions validate input data
3. **Creation**: Factory function creates User object
4. **Processing**: User object provides formatted output
5. **Output**: Application displays user information

---

## 📁 Code Structure

### Directory Organization
```
test_project/
├── README.md              # Project documentation
├── requirements.txt       # Dependency specifications
├── src/                   # Source code directory
│   ├── main.py           # Application entry point
│   ├── utils.py          # Utility functions
│   └── models/           # Data models
│       └── user.py       # User model class
└── tests/                # Test directory
    └── test_main.py      # Unit tests
```

### File Purposes
- **`src/main.py`**: Application entry point and main execution flow
- **`src/utils.py`**: Validation and formatting utility functions
- **`src/models/user.py`**: User data model and methods
- **`tests/test_main.py`**: Unit tests for core functionality
- **`requirements.txt`**: Python package dependencies
- **`README.md`**: Project documentation and setup instructions

---

## 📚 API Documentation

### User Model (`src/models/user.py`)

#### Class: User
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name}, {self.age} years old"
```

**Constructor Parameters:**
- `name` (str): User's name
- `age` (int): User's age

**Methods:**
- `get_info()`: Returns formatted user information string

### Utility Functions (`src/utils.py`)

#### Function: validate_user
```python
def validate_user(user):
    if not user.name:
        return False
    if user.age < 0 or user.age > 150:
        return False
    return True
```

**Parameters:**
- `user` (User): User object to validate

**Returns:**
- `bool`: True if user data is valid, False otherwise

**Validation Rules:**
- Name must not be empty
- Age must be between 0 and 150

#### Function: format_user_info
```python
def format_user_info(user):
    return f"User: {user.name} (Age: {user.age})"
```

**Parameters:**
- `user` (User): User object to format

**Returns:**
- `str`: Formatted user information string

### Main Functions (`src/main.py`)

#### Function: main
```python
def main():
    print("Hello, World!")
    user = create_user("Alice", 25)
    print(f"Created user: {user.name}")
```

**Purpose:** Application entry point and main execution flow

#### Function: create_user
```python
def create_user(name, age):
    from models.user import User
    return User(name, age)
```

**Parameters:**
- `name` (str): User's name
- `age` (int): User's age

**Returns:**
- `User`: New User object instance

---

## 💡 Usage Examples

### Basic Usage
```python
# Import required modules
from src.main import create_user
from src.utils import validate_user, format_user_info

# Create a user
user = create_user("Alice", 25)

# Validate user data
if validate_user(user):
    print("User data is valid")
    print(format_user_info(user))
else:
    print("User data is invalid")
```

### Error Handling
```python
# Create user with invalid data
user = create_user("", -5)  # Empty name, negative age

# Validate and handle errors
if not validate_user(user):
    print("Invalid user data:")
    print(f"Name: '{user.name}' (should not be empty)")
    print(f"Age: {user.age} (should be 0-150)")
```

### Testing
```python
# Run unit tests
import unittest
from tests.test_main import TestMain

# Create test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```

---

## 🛠️ Development Guide

### Environment Setup
1. **Python Version**: Python 3.7 or higher
2. **Virtual Environment**: Recommended for isolation
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Dependencies**: Install required packages
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
```bash
# Navigate to project directory
cd test_project

# Run main application
python src/main.py
```

### Development Workflow
1. **Code Changes**: Modify source files in `src/`
2. **Testing**: Run tests to verify functionality
3. **Validation**: Ensure code follows project standards
4. **Documentation**: Update relevant documentation

### Code Style Guidelines
- **PEP 8**: Follow Python PEP 8 style guide
- **Docstrings**: Include docstrings for all functions and classes
- **Type Hints**: Consider adding type hints for better code clarity
- **Comments**: Add comments for complex logic

---

## 🧪 Testing

### Test Structure
```python
class TestMain(unittest.TestCase):
    def test_create_user(self):
        user = create_user("Bob", 30)
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.age, 30)
```

### Running Tests
```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_main

# Run with pytest (if available)
pytest tests/
```

### Test Coverage
- **User Creation**: Tests user object creation
- **Type Validation**: Verifies object types
- **Value Validation**: Checks property values
- **Functionality**: Tests core application features

---

## 📦 Dependencies

### Core Dependencies
- **requests==2.28.1**: HTTP client library
- **pytest==7.2.0**: Modern testing framework
- **flask==2.2.2**: Web framework for future web features

### Development Dependencies
- **unittest**: Built-in testing framework
- **pip**: Package management
- **venv**: Virtual environment support

### Installation
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

### Getting Started
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Contribution Guidelines
- **Code Quality**: Maintain high code quality standards
- **Testing**: Add tests for new features
- **Documentation**: Update documentation as needed
- **Style**: Follow project coding standards
- **Review**: Participate in code reviews

### Development Standards
- **Version Control**: Use meaningful commit messages
- **Branching**: Use feature branches for development
- **Testing**: Maintain test coverage
- **Documentation**: Keep documentation up to date

---

## 📊 Project Summary

### Strengths
- **Clean Architecture**: Well-organized, modular design
- **Best Practices**: Follows Python and software engineering best practices
- **Comprehensive Testing**: Good test coverage and testing strategy
- **Documentation**: Clear documentation and code comments
- **Extensibility**: Easy to extend and modify

### Future Enhancements
- **Web Interface**: Flask-based web application
- **Database Integration**: Persistent data storage
- **API Development**: RESTful API endpoints
- **Advanced Validation**: More sophisticated validation rules
- **Performance Optimization**: Code efficiency improvements

### Learning Outcomes
This project demonstrates:
- Object-oriented programming principles
- Modular software architecture
- Testing strategies and best practices
- Documentation and code quality standards
- Python development workflow

---

*This wiki provides a comprehensive overview of the test_project codebase, covering all aspects from basic usage to advanced development practices.*"""
    
    print_llm_call(5, "最终结论", llm_input_5, llm_output_5)
    
    # 总结
    print_separator("ReAct流程总结")
    print("""
🔄 ReAct (DeepResearch) 完整流程总结:

📊 调用统计:
- 总轮次: 5轮
- LLM调用次数: 5次
- 每次调用都包含: 系统提示词 + 对话历史 + RAG上下文 + 用户消息

 流程特点:
1. 第1轮: 研究计划 - 建立分析框架
2. 第2-4轮: 研究更新 - 逐步深入分析
3. 第5轮: 最终结论 - 综合所有发现

 上下文累积:
- 对话历史逐轮累积
- RAG上下文每轮更新
- 分析深度逐轮递增

 输出质量:
- 从概览到详细分析
- 从计划到完整文档
- 从简单到复杂结构

 项目路径: {project_path}
    """.format(project_path=project_path))

if __name__ == "__main__":
    main()
