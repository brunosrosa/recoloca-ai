---
title: "ADR Template - Architecture Decision Record"
doc_id: "ADR-TEMPLATE"
version: "1.0"
last_updated: "2025-01-20 15:30:00"
timezone: "America/Sao_Paulo"
status: "Template"
owner: "@ArchitectureTeam"
tags: [adr, template, architecture, decision-record]
description: "Template for creating Architecture Decision Records (ADRs) to document important architectural decisions and their rationale."
---

# ADR-XXX: [Decision Title]

## Status

**Status**: [Proposed | Accepted | Deprecated | Superseded]  
**Date**: [YYYY-MM-DD]  
**Decision Makers**: [List of people involved in the decision]  
**Consulted**: [List of people consulted]  
**Informed**: [List of people informed]  

## Context

[Describe the architectural problem or opportunity that requires a decision. Include:
- What is the current situation?
- What forces are at play?
- What constraints exist?
- What are the business/technical drivers?]

## Decision

[State the architectural decision that was made. Be clear and concise about what was decided.]

## Rationale

[Explain why this decision was made. Include:
- What alternatives were considered?
- What were the trade-offs?
- What factors influenced the decision?
- What assumptions were made?]

## Consequences

### Positive Consequences
- [List the positive outcomes expected from this decision]
- [Include benefits, improvements, or opportunities created]

### Negative Consequences
- [List the negative outcomes or trade-offs]
- [Include risks, limitations, or challenges introduced]

### Neutral Consequences
- [List outcomes that are neither clearly positive nor negative]
- [Include changes that are necessary but don't add direct value]

## Implementation

### Action Items
- [ ] [Specific tasks required to implement this decision]
- [ ] [Include timelines and responsible parties]
- [ ] [Consider dependencies and prerequisites]

### Success Criteria
- [How will we know this decision was successful?]
- [What metrics or indicators will we use?]

## Alternatives Considered

### Alternative 1: [Name]
**Description**: [Brief description of the alternative]
**Pros**: [Advantages of this alternative]
**Cons**: [Disadvantages of this alternative]
**Reason for rejection**: [Why this wasn't chosen]

### Alternative 2: [Name]
**Description**: [Brief description of the alternative]
**Pros**: [Advantages of this alternative]
**Cons**: [Disadvantages of this alternative]
**Reason for rejection**: [Why this wasn't chosen]

## Related Decisions

- [ADR-XXX: Related Decision Title] - [Brief description of relationship]
- [ADR-XXX: Another Related Decision] - [Brief description of relationship]

## References

- [Link to relevant documentation]
- [Link to research or analysis]
- [Link to external resources]

## Notes

[Any additional notes, assumptions, or context that doesn't fit elsewhere]

---

**Review Schedule**: [When should this decision be reviewed?]  
**Next Review Date**: [YYYY-MM-DD]  
**Superseded By**: [ADR-XXX if this decision has been superseded]

---

## ADR Guidelines

### When to Create an ADR

Create an ADR when making decisions about:
- **Architecture patterns** (microservices, monolith, event-driven, etc.)
- **Technology choices** (frameworks, databases, cloud services, etc.)
- **Design principles** (API design, data modeling, security approaches, etc.)
- **Process decisions** (deployment strategies, testing approaches, etc.)
- **Trade-offs** (performance vs. maintainability, cost vs. features, etc.)

### ADR Numbering

- Use sequential numbering: ADR-001, ADR-002, etc.
- Numbers are never reused, even if an ADR is deprecated
- Use leading zeros for better sorting (ADR-001, not ADR-1)

### Status Definitions

- **Proposed**: Decision is under consideration
- **Accepted**: Decision has been approved and should be implemented
- **Deprecated**: Decision is no longer relevant but kept for historical context
- **Superseded**: Decision has been replaced by a newer ADR

### Writing Tips

1. **Be concise but complete** - Include all necessary information without being verbose
2. **Use clear language** - Avoid jargon and explain technical terms
3. **Focus on the decision** - Don't get lost in implementation details
4. **Include context** - Future readers need to understand why the decision was made
5. **Consider the audience** - Write for developers who will work with this decision
6. **Update status** - Keep the status current as decisions evolve

### Review Process

1. **Draft**: Author creates initial ADR
2. **Review**: Technical team reviews and provides feedback
3. **Discussion**: Address concerns and refine the decision
4. **Approval**: Architecture team approves the ADR
5. **Implementation**: Development team implements the decision
6. **Monitoring**: Track the outcomes and effectiveness

---

**Template Version**: 1.0  
**Last Updated**: 2025-01-20  
**Maintained By**: @ArchitectureTeam