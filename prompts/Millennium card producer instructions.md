<context>
# Overview  
Create a comprehensive Product Requirements Document (PRD) for the Millennium card producer. This document should outline the key features, user experience, technical architecture, development roadmap, and any potential risks associated with the project.

# Core Features  
The project should include the following core features:
- Data Integration from Supabase
- PDF Generation for Printing

# User Experience  
- the user starts a CLI command to generate the cards
</context>
<PRD>
# Technical Architecture  
Consider the following implementation details:
- For Supabase integration see .env file for connection details
- Data models can be found in src/types/supabase_types.py
- PDF generation should be handled in src/cards.py
- each card layout, front and back, should be defined in src/card.py
- CLI application entry point is in src/main.py

# Development Roadmap  
There will be only one phase containing the following milestones:
- A PDF generation function that creates the card layout
- Integration with Supabase to fetch card data
- A CLI command to trigger the card generation process

# Logical Dependency Chain
- Card information is fetched from Supabase
- Card information is denormalised: all connections containing the current character's id are fetched and joined to the character
- Character Id's on connections are replaced with the character's name for display on the card
- The card layout is generated using the fetched and denormalised data
- The card layout should be based on Sample_layout.jpg for front and back
- the category colours are as follows: 
  - Royalty (R): red
  - Statesman (S): orange
  - Philosopher (P): yellow
  - Mathematical Scientist (M): green
  - Natural Scientist (N): turquoise
  - Artist (A): blue
  - Builders and Engineers (B): indigo
  - Composer (C): violet
  - Dramatist (D): pink
  - Towns and cities (T): brown

- The PDF is created with all cards and saved to disk
- Getting as quickly as possible to something usable/visible front end that works
- Properly pacing and scoping each feature so it is atomic but can also be built upon and improved as development approaches]

# Risks and Mitigations  

# Appendix  
- The code should be written in python
</PRD>
