---
doc_id: CPF_EST_001
title: Codex Prime Framework Master Plan
description: >
  The central document that defines the vision, objectives and guidelines of the Codex Prime Framework
  as a living documentation system for AI agents and humans with hybrid architecture.
type: Strategy
status: Active
owner: Maestro
author: "@ArquitetoDoCodex"
version: "3.0"
language: en-us
created_date: "2025-05-15"
updated_date: "2025-07-23 19:06:07"
tags:
  - codex-prime
  - living-documentation
  - framework
  - diataxis
  - vector-rag
  - graph-rag
  - governance
  - guardian-agents
knowledge_type: declarative
rag_optimization:
  vector_search: true
  graph_relations: true
  semantic_density: high
  context_window: large
governance_level: constitutional
agent_compatibility:
  - reasoning
  - retrieval
  - generation
  - validation
---
# CODEX PRIME FRAMEWORK MASTER PLAN

**Version**: 3.0

**Update Date**: July 23, 2025

## Executive Summary

The **Codex Prime Framework** is a next-generation living documentation system designed to optimize knowledge management for both AI agents and humans. This framework establishes structured standards based on the **Diátaxis Framework** and **Docs-as-Code** principles, incorporating a **hybrid Vector RAG + GraphRAG architecture** for advanced knowledge retrieval, **fundamental governance documents** and **guardian agents** for autonomous quality maintenance, creating a consistent, navigable and self-evolving knowledge base.

## 1. Codex Prime Framework Overview

### 1.1. Definition and Purpose

The **Codex Prime Framework** is a knowledge organization system that combines:

- **Living Documentation**: Dynamic structures that evolve with the project
- **Diátaxis Framework**: Organization based on Tutorial, How-to, Explanation and Reference
- **Docs-as-Code Governance**: Documentation versioning and quality control
- **AI Compatibility**: Structures optimized for consumption by AI agents

### 1.2. Problems Solved

- **Knowledge Fragmentation**: Centralization and structuring of information
- **Documentation Inconsistency**: Uniform documentation standards
- **Navigation Difficulty**: Clear hierarchies and bidirectional links
- **AI-Human Misalignment**: Readable formats for both audiences

### 1.3. Fundamental Components

#### 1.3.1. Diátaxis Structure

The framework organizes knowledge into four main categories:

- **Tutorials**: Step-by-step learning guides
- **How-to Guides**: Practical solutions for specific problems
- **Explanations**: Context and conceptual understanding
- **Reference**: Precise and complete technical information

#### 1.3.2. Living Documentation

- **Continuous Evolution**: Documents that update with the project
- **Bidirectional Links**: Semantic connections between concepts
- **Structured Metadata**: YAML frontmatter for classification
- **Versioning**: Change control via Git

#### 1.3.3. AI Compatibility

- **Structured Format**: Markdown + YAML for automatic parsing
- **Semantic Context**: Tags and categories for retrieval
- **Clear Hierarchy**: Programmatic navigation by agents
- **Consistent Patterns**: Uniform templates for different content types

### 1.4. Hybrid Knowledge Retrieval Architecture

The Codex Prime Framework implements a **hybrid Vector RAG + GraphRAG architecture** that combines the advantages of both approaches:

#### 1.4.1. Vector RAG (Retrieval Augmented Generation)
- **Semantic Search**: Vector embeddings for conceptual similarity
- **Fast Retrieval**: Optimized indexes for real-time queries
- **Scalability**: Support for large documentation volumes
- **Contextual Precision**: Matching based on semantic meaning

#### 1.4.2. GraphRAG (Graph-based RAG)
- **Conceptual Relations**: Mapping connections between entities
- **Multi-step Reasoning**: Navigation through knowledge graphs
- **Expanded Context**: Understanding of dependencies and hierarchies
- **Pattern Discovery**: Identification of implicit relationships

#### 1.4.3. Integration Strategy
- **Parallel Querying**: Vector and Graph RAG executed simultaneously
- **Intelligent Fusion**: Weighted combination of results
- **Adaptive Fallback**: Vector RAG as backup for Graph RAG
- **Dynamic Optimization**: Automatic adjustment based on query type

#### 1.4.4. Executable Knowledge Types
- **Declarative**: Facts and definitions (optimized for Vector RAG)
- **Procedural**: Processes and workflows (optimized for Graph RAG)
- **Heuristic**: Rules and patterns (hybrid Vector + Graph)
- **Contextual**: Domain-specific knowledge (Graph RAG)

## 2. Framework Structure and Organization

### 2.1. Directory Hierarchy

The Codex Prime Framework organizes knowledge in an expanded hierarchical structure based on the Diátaxis Framework:

```
.codex-prime/                    # Universal Framework Engine
├── governance/                  # Fundamental Governance Documents
│   ├── CONSTITUTION.md         # Ecosystem fundamental rules
│   ├── AGENT_PROFILE_TEMPLATE.md
│   ├── CAPABILITY_TEMPLATE.md
│   └── KNOWLEDGE_ARTIFACT_SPEC.md
├── agents/                      # Guardian Agents
│   ├── arquivista/             # Organization and cataloging
│   ├── conector/               # Integration and synchronization
│   └── constitucionalista/     # Compliance and governance
└── templates/                   # Universal templates

.codex/                          # Project-Specific Instance
├── 01_Tutorials/               # Learning guides
├── 02_How_To_Guides/           # Practical solutions
├── 03_Explanations/            # Conceptual context
├── 04_Reference/               # Technical documentation
├── 05_Templates/               # Reusable models
├── 06_Metadata/                # Configurations and indexes
├── 07_Product/                 # Product Management
├── 08_Engineering/             # Development and Architecture
├── 09_Design/                  # UX/UI and System Design
├── 10_Data/                    # Data Science and Engineering
├── 11_Marketing/               # Marketing and Growth
├── 12_People/                  # HR and Human Development
├── 13_Legal/                   # Compliance and Legal Aspects
└── 14_Corporate/               # Strategy and Operations
```

### 2.2. Naming Conventions

#### 2.2.1. Files
- **Format**: `NN_DESCRIPTIVE_NAME.md`
- **Numbering**: Sequential for ordering
- **Language**: Suffix when applicable (`_pt-br`, `_en`)

#### 2.2.2. Extended YAML Frontmatter
```yaml
---
doc_id: CPF_XXX_NNN
title: Document Title
description: Concise description
type: [Tutorial|HowTo|Explanation|Reference]
status: [Draft|Active|Archived]
owner: Responsible Name
author: "@AuthorName"
version: "X.Y"
language: en-us
created_date: "YYYY-MM-DD"
updated_date: "YYYY-MM-DD HH:mm:ss"
tags: [tag1, tag2, tag3]
knowledge_type: [declarative|procedural|heuristic|contextual]
rag_optimization:
  vector_search: [true|false]
  graph_relations: [true|false]
  semantic_density: [low|medium|high]
  context_window: [small|medium|large]
governance_level: [operational|tactical|strategic|constitutional]
agent_compatibility:
  - reasoning
  - retrieval
  - generation
  - validation
related_docs: [doc_id1, doc_id2]
dependencies: [doc_id1, doc_id2]
---
```

### 2.3. Documentation Standards

#### 2.3.1. Document Structure
- **Header**: Mandatory YAML frontmatter
- **Main Title**: Single H1 per document
- **Sections**: Clear hierarchy with H2, H3, H4
- **Links**: Bidirectional references between documents
- **Metadata**: Tags and categories for classification

#### 2.3.2. Templates by Type
- **Tutorials**: Step-by-step with clear objectives
- **How-to**: Problem → Solution → Result
- **Explanations**: Context → Concepts → Implications
- **Reference**: Complete technical specifications
        
## 3. Governance and Best Practices

### 3.1. Docs-as-Code Governance Principles

#### 3.1.1. Version Control
- **Git as Source of Truth**: All knowledge versioned
- **Feature Branches**: Change isolation
- **Pull Requests**: Collaborative content review
- **Semantic Tags**: Structured versioning

#### 3.1.2. Content Quality
- **Peer Review**: Technical accuracy validation
- **Link Testing**: Automatic reference verification
- **Markdown Linting**: Formatting consistency
- **Frontmatter Validation**: Mandatory metadata

### 3.2. Documentation Lifecycle

#### 3.2.1. Creation
1. **Need Identification**: Knowledge gap
2. **Template Selection**: Based on Diátaxis type
3. **Development**: Following established standards
4. **Review**: Technical and editorial validation

#### 3.2.2. Maintenance
1. **Monitoring**: Obsolete content identification
2. **Updates**: Synchronization with changes
3. **Refactoring**: Continuous structure improvement
4. **Archiving**: Legacy content management

### 3.3. AI Systems Integration

#### 3.3.1. Agent Optimization
- **Semantic Structure**: Clear hierarchy for parsing
- **Explicit Context**: Sufficient information for understanding
- **Cross References**: Links to related knowledge
- **Rich Metadata**: Tags and categories for filtering

#### 3.3.2. Feedback Loop
- **Usage Metrics**: Agent access tracking
- **Response Quality**: Effectiveness evaluation
- **Identified Gaps**: Knowledge lacunae
- **Continuous Improvement**: Data-driven refinement

### 3.4. Guardian Agents

The Codex Prime Framework implements **specialized guardian agents** for autonomous quality maintenance and governance:

#### 3.4.1. Archivist (@ArquivistaDoCodex)
- **Responsibility**: Knowledge organization and cataloging
- **Functions**:
  - Detection of duplications and inconsistencies
  - Structural reorganization suggestions
  - Index and metadata maintenance
  - Documentation gap identification

#### 3.4.2. Connector (@ConectorDoCodex)
- **Responsibility**: Integration and synchronization between systems
- **Functions**:
  - Synchronization with external repositories
  - Link and reference validation
  - Development tools integration
  - Dependency monitoring

#### 3.4.3. Constitutionalist (@ConstitucionalistaDoCodex)
- **Responsibility**: Compliance and governance
- **Functions**:
  - Constitutional rule adherence validation
  - Content quality auditing
  - Standards and conventions enforcement
  - Governance conflict resolution

#### 3.4.4. Agent Coordination
- **Decision Hierarchy**: Maestro → Constitutionalist → Archivist → Connector
- **Communication Protocols**: Standardized APIs for interaction
- **Conflict Resolution**: Automatic escalation to higher levels
- **Continuous Auditing**: Log of all actions and decisions
    
## 4. Implementation and Adoption

### 4.1. Implementation Phases

#### 4.1.1. Phase 1: Base Structure
- Directory hierarchy creation
- Standard template definition
- Version control configuration
- Convention establishment

#### 4.1.2. Phase 2: Initial Content
- Existing documentation migration
- Fundamental guide creation
- Technical reference development
- Structure validation

#### 4.1.3. Phase 3: Optimization
- Usage-based refinement
- Process automation
- Tool integration
- Metrics and monitoring

### 4.2. Success Criteria

#### 4.2.1. Quantitative Metrics
- **Coverage**: % of documented knowledge
- **Consistency**: Adherence to established standards
- **Accessibility**: Navigation and search ease
- **Updates**: Content maintenance frequency

#### 4.2.2. Qualitative Metrics
- **Usability**: Ease of use by humans and agents
- **Completeness**: Information sufficiency
- **Clarity**: Content comprehensibility
- **Relevance**: Alignment with real needs

## 5. Benefits and Impacts

### 5.1. For Humans
- **Intuitive Navigation**: Clear and predictable structure
- **Efficient Search**: Semantic knowledge organization
- **Simplified Maintenance**: Standardized processes
- **Improved Collaboration**: Common documentation standards

### 5.2. For AI Agents
- **Structured Parsing**: Consistent format for analysis
- **Rich Context**: Metadata and links for understanding
- **Precise Retrieval**: RAG-optimized organization
- **Continuous Evolution**: Always updated knowledge base

## 6. Glossary

- **Codex Prime Framework**: Diátaxis-based living documentation system
- **Diátaxis**: Documentation organization framework in 4 types
- **Docs-as-Code**: Documentation versioning approach
- **Living Documentation**: Documents that evolve with the project
- **Frontmatter**: YAML metadata at the beginning of Markdown files
- **RAG**: Retrieval Augmented Generation for AI systems

## 7. References

- **Diátaxis Framework**: [diataxis.fr](https://diataxis.fr)
- **Docs-as-Code**: Documentation as code principles
- **Markdown**: Markup language for documentation
- **YAML**: Human-readable data serialization format

## 8. Version History

### v3.0 (July 23, 2025)
- **Hybrid Architecture**: Implementation of Vector RAG + GraphRAG
- **Governance Documents**: Addition of CONSTITUTION.md and fundamental templates
- **Guardian Agents**: Introduction of Archivist, Connector and Constitutionalist
- **Expanded Structure**: New knowledge domains (Design, Data, Marketing, etc.)
- **Advanced Metadata**: Extended YAML frontmatter for RAG optimization
- **Knowledge Types**: Classification into declarative, procedural, heuristic and contextual
- **Dual Structure**: Separation between .codex-prime/ (universal) and .codex/ (specific)
- **Schema Evolution**: Agent-driven adaptation capability

### v2.0 (July 23, 2025)
- Complete refactoring focused on Codex Prime Framework
- Removal of development-specific content
- Emphasis on living documentation for agents and humans
- Simplification and conceptual clarity
- Date updates to reflect correct chronology

### v1.2 (June 2025)
- Post-MVP refinements
- Initial feedback integration

### v1.0 (May 2025)
- Initial document version

---

**Note:** This document establishes the vision and fundamental guidelines of the Codex Prime Framework as a living documentation system optimized for AI agents and humans.