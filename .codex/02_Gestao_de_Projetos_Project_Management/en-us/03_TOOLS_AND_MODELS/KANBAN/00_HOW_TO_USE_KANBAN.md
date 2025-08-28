---
sticker: lucide//shield-question
---
# 📋 HOW TO USE KANBAN IN OBSIDIAN ([PROJECT_NAME])

This document aims to clarify the use and standards of Kanban in Obsidian for the [PROJECT_NAME] project, focusing on compatibility and best practices for the Obsidian Kanban and Obsidian Tasks plugins.

## 💡 Understanding Kanban in Obsidian

Obsidian, through the Kanban plugin, allows creating Kanban boards directly in Markdown files. However, it's crucial to understand how the Markdown structure interacts with the Kanban visualization to avoid problems.

### ❌ The Problem with `##` (H2) Titles and Columns

A fundamental point of attention is the use of second-level titles (`##`). In Obsidian's Kanban plugin, **each `##` title is interpreted as a new Kanban column**.

**Problem Example:**

```markdown
# My Kanban

## Column 1
- Task A
- Task B

## Column 2
- Task C

## Subsection Within Column 2
This would create a new unwanted column in the Kanban, instead of being a subsection of Column 2.
```

**Impact:** If you use `##` to organize subsections within a column (for example, to group tasks by type or subtopic), the Kanban plugin will create a new column for each `##`, completely disorganizing the board and making visualization and management difficult.

### ✅ Solution: Use `###` (H3) Titles or Lower Levels for Subsections

To organize content within a Kanban column without creating new columns, use third-level titles (`###`) or lower (`####`, etc.). These are interpreted as subtitles within the existing column.

**Correct Solution Example:**

```markdown
# My Kanban

## Task Column

### Priority Tasks
- [ ] Important Task 1
- [ ] Important Task 2

### Low Priority Tasks
- [ ] Minor Task 1
- [ ] Minor Task 2

## Completed Column
- [x] Finished Task
```

In this example, "Priority Tasks" and "Low Priority Tasks" will appear as subtitles within the "Task Column", keeping the Kanban structure intact.

## 🎯 Standards and Understandings for [PROJECT_NAME] Project

To ensure consistency and functionality of our Kanbans, we will follow these standards:

### 1. Column Structure (`##` Titles)

The main Kanban columns (and therefore the `##` titles) should represent workflow stages or project phases:

- `## CURRENT SESSION (In Progress)`
- `## PHASE 0: RAG + AGENTS FOUNDATION`
- `## PHASE 1: TECHNICAL AND STRATEGIC VALIDATION`
- `## BACKLOG (Not Prioritized)`
- `## COMPLETED`

### 2. Internal Column Organization (`###` or `####` Titles)

To organize tasks or information within a column, use `###` (third-level titles) or `####` (fourth-level titles). **Never use `##` within an existing column.**

Examples:
```markdown
## PHASE 0: RAG + AGENTS FOUNDATION

### RAG Configuration
- [ ] Configure ChromaDB
- [ ] Implement ingestion pipeline

### Tier 1 Agents
- [ ] Configure PM Mentor Agent
- [ ] Configure UX/UI Mentor Agent
```

### 3. Integration with Obsidian Tasks Plugin

The Obsidian Tasks Plugin offers advanced functionalities for task management:

#### Task Syntax:
- **Open tasks:** `- [ ] My task`
- **Completed tasks:** `- [x] My task`
- **Cancelled tasks:** `- [-] My task`

#### Task Metadata:
- **Due dates:** `📅 YYYY-MM-DD`
- **Start dates:** `🛫 YYYY-MM-DD`
- **Scheduled dates:** `⏳ YYYY-MM-DD`
- **Recurring tasks:** `🔁 every week`
- **Priority:** `🔺` (high), `⏫` (medium), `🔽` (low)

#### Complete Example:
```markdown
- [ ] Implement JWT authentication 📅 2024-01-15 🔺 #development #MVP
- [ ] Create login screen mockups ⏳ 2024-01-10 ⏫ #design #UX
- [x] Configure database ✅ 2024-01-05 #infrastructure
```

### 4. Tags and Categorization

Use tags (`#`) consistently to categorize tasks:

- **By area:** `#development`, `#design`, `#architecture`, `#testing`
- **By phase:** `#Phase0`, `#Phase1`, `#MVP`
- **By component:** `#RAG`, `#agents`, `#frontend`, `#backend`
- **By priority:** `#critical`, `#important`, `#nice-to-have`

### 5. Internal Links and References

Whenever referencing other project documents, use Obsidian internal links:

```markdown
- [ ] Review [[docs/02_Requirements/01_ERS.md|ERS]] to validate requirements
- [ ] Implement according to [[docs/03_Architecture_and_Design/01_HLD.md|HLD]]
```

### 6. Transclusion and Embedding

The Kanban plugin allows transcluding columns from other Kanban boards:

```markdown
## Development Tasks
![[INTERNAL_PROJECT_KANBAN#CURRENT SESSION (In Progress)]]
```

### 7. Visualization and Editing

The Kanban plugin offers multiple visualization forms:

- **Kanban View:** Visual interface with columns and cards
- **Markdown View:** Direct Markdown code editing
- **Table View:** Tabular format for analysis
- **List View:** Simple list format

## 🚀 Best Practices

### ✅ Do:
- Use `##` only for main columns
- Use `###` or `####` for subsections within columns
- Keep tags consistent throughout the project
- Use Tasks Plugin metadata for advanced tracking
- Reference related documents with internal links
- Keep structure simple and functional

### ❌ Avoid:
- Using `##` for subsections within columns
- Creating too many columns (maximum 6-8 for good visualization)
- Inconsistent or overly specific tags
- Overly complex structures that hinder navigation
- Mixing different organization patterns in the same board

## 🔧 Recommended Configuration

For the [PROJECT_NAME] project, we use a system of **5 specialized Kanbans**:

### 📋 Main Kanbans (Always Active):

1. **Operational Kanban** (`01_OPERATIONAL_KANBAN_SESSIONS.md`):
   - **Purpose:** Daily task and work session management
   - **Focus:** Current session tasks and next actions
   - **Columns:** Maximum 6 columns for good visualization
   - **Update:** Daily, every work session
   - **Responsible:** @Maestro, @OrchestratorAgent

2. **Strategic Kanban** (`02_STRATEGIC_KANBAN_PHASES.md`):
   - **Purpose:** Long-term vision organized by project phases
   - **Focus:** Strategic objectives and main milestones
   - **Organization:** By phases (Phase 0, Phase 1, Phase 2, etc.)
   - **Update:** Weekly/biweekly
   - **Responsible:** @Maestro, @OrchestratorAgent

### 🎯 Specialized Kanbans (Activated as Needed):

3. **Bugs & Issues Kanban** (`03_BUGS_ISSUES_KANBAN.md`):
   - **When to use:** When bug volume justifies a dedicated board (post-MVP)
   - **Purpose:** Specific management of bugs, technical issues and fixes
   - **Organization:** By priority (P0-P3) and resolution status
   - **Responsible:** @DevFastAPIAgent, @DevFlutterAgent, @ITArchitectAgent

4. **Research & Insights Kanban** (`04_RESEARCH_INSIGHTS_KANBAN.md`):
   - **When to use:** For continuous research and validation demand (post-MVP)
   - **Purpose:** Management of market research, user insights and strategic discoveries
   - **Organization:** From research backlog to implemented insights
   - **Responsible:** @OrchestratorAgent, @UXDesignerAgent, @Maestro

5. **Marketing & GTM Kanban** (`05_MARKETING_GTM_KANBAN.md`):
   - **When to use:** Post-MVP, when starting marketing and acquisition activities
   - **Purpose:** Management of marketing activities, go-to-market and growth
   - **Organization:** From campaign planning to implemented results
   - **Responsible:** @Maestro, @OrchestratorAgent, Marketing Team (future)

### 🔄 Usage Guidelines by Phase:

#### **Phase 0-1 (Current):** 
- **Active:** Operational + Strategic
- **Focus:** RAG foundation, agent configuration, technical validation

#### **Phase 2 (MVP):**
- **Active:** Operational + Strategic + Bugs & Issues
- **Focus:** Development, testing, fixes

#### **Phase 3+ (Post-MVP):**
- **Active:** All 5 Kanbans as needed
- **Focus:** Growth, continuous research, marketing

### 🔗 Synchronization between Kanbans:

- **Consistent Tags:** Use the same tag system across all boards
- **Transclusion:** Connect related boards when necessary
- **Cross-Reference:** Reference tasks between boards when there are dependencies
- **Synchronization Routine:** Define regular routine for alignment between boards
- **Shared Responsibility:** @OrchestratorAgent maintains overall view of all boards

By following these guidelines, we ensure our Kanbans are functional, organized and compatible with Obsidian tools, facilitating efficient management of the [PROJECT_NAME] project.

---

**References:**
- Obsidian Tasks Plugin Documentation
- Obsidian Kanban Plugin Documentation
- Obsidian Community on Reddit

--- END OF HOW_TO_USE_KANBAN.md DOCUMENT ---