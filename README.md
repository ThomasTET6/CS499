# CS499

Welcome to my Computer Science Capstone ePortfolio.

## Student
Thomas Thystrup

## Contents
- Professional Self-Assessment
- Code Review
- Software Engineering Enhancement
- Algorithms and Data Structures Enhancement
- Database Enhancement

---

## Code Review

Link to video code review: https://youtu.be/P2MVOY0nEBo

---

# CS499 Enhancement - Software Engineering and Design

## Original Artifact

The original artifact was created in CS340: Advanced Programming Concepts as a Jupyter Notebook application using Dash and MongoDB. The project was designed to display animal rescue data through an interactive dashboard with database filtering, charts, and geographic visualization.

## Software Engineering Improvements

For the CS499 enhancement, the Jupyter Notebook application was converted into a standalone Python Dash application with a modular structure.

Improvements made:

- Converted Jupyter Notebook code into a maintainable Python application
- Separated application components into independent modules
- Created dedicated files for:
  - Dashboard layout
  - Callback functions
  - Database interactions
  - Query logic
- Improved organization, readability, and maintainability
- Prepared the application for future database and security enhancements

---

# CS499 Enhancement - Algorithms and Data Structures

## Algorithm Enhancement

The original dashboard contained repeated conditional logic inside the callback functions to determine which MongoDB query should be executed based on the selected rescue type.

For this enhancement, the filtering logic was redesigned using a dictionary-based query builder.

## Improvements Made

- Removed repeated if/elif query selection logic
- Created a centralized query configuration structure
- Implemented a reusable query builder function
- Improved scalability by allowing new rescue filters to be added without modifying callback logic
- Improved maintainability by separating query generation from dashboard functionality

## Algorithm Concepts Demonstrated

- Dictionary-based data structures
- Efficient key-based lookup operations
- Improved code organization through separation of responsibilities
- Reduced unnecessary conditional branching

---

# Future Enhancements

- Reconnect MongoDB database functionality
- Improve database security by removing hardcoded credentials
- Add additional validation and error handling
- Expand testing coverage
- Improve database operations and CRUD functionality
- Add additional dashboard filtering capabilities