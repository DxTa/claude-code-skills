> **Claude Code Adapted**: This version has been adapted for Claude Code compatibility. The original OpenCode version is at the root of this repository under `core/agent-selection/SKILL.md`.

---
name: agent-selection
description: Decision tree for selecting appropriate tools and task prompts based on task patterns
version: "1.0.0"
---

# Tool & Agent Selection Decision Tree

Complete decision tree for selecting the right tool or task prompt for any task. Use this when you need to decide which specialized approach to invoke.

## Overview

This skill provides a comprehensive decision tree that maps task patterns to the most appropriate:
- Built-in tools (Grep, Glob, Read, Bash)
- Task tool with specialist prompts (frontend, backend, security, etc.)
- MCP reasoning tools (code-reasoning, shannon-thinking)
- Skills (TDD, code review, debugging)

## Decision Tree

<decision-tree name="agent-selection">
  <!-- Built-in search and exploration tools -->
  <case pattern="Find files matching pattern X">
    <tool>Glob</tool>
  </case>
  <case pattern="Search code for keyword Y">
    <tool>Grep</tool>
  </case>
  <case pattern="Where is feature Z defined?">
    <tool>Grep (search for function/class name) + Read (examine matches)</tool>
  </case>
  <case pattern="How does X work?">
    <tool>Grep + Read to trace the code flow</tool>
    <note>architecture - read multiple files to understand patterns</note>
  </case>
  <case pattern="Trace dependencies of module Y">
    <tool>Grep for imports/requires + Read to map dependency chain</tool>
  </case>
  <case pattern="Unfamiliar codebase area">
    <tool>Glob to find relevant files + Read to understand structure</tool>
    <note>map first</note>
  </case>
  <case pattern="Research library/API/pattern">
    <tool>WebSearch / WebFetch / Context7</tool>
    <note>external docs</note>
  </case>
   <case pattern="Complex multi-step analysis">
     <tool>Task tool with appropriate research prompt</tool>
   </case>

   <!-- Spec Analysis -->
   <case pattern="Analyze Jira ticket or spec">
     <prerequisite>Grep for past decisions on the topic</prerequisite>
     <skill>spec-analyzer</skill>
     <note>Search past decisions first for context, then analyze spec</note>
   </case>
   <case pattern="Vague or incomplete requirements">
     <skill>spec-analyzer</skill>
     <note>Socratic questioning to clarify</note>
   </case>
   <case pattern="JIRA-[A-Z0-9]+ ticket needs analysis">
     <skill>spec-analyzer</skill>
     <note>Pull via Atlassian MCP tools if available</note>
   </case>
   <case pattern="Feature request or user story refinement">
     <skill>spec-analyzer</skill>
     <note>Check past decisions before T3+ planning</note>
   </case>

   <!-- Self-Reflection (CRITICAL - currently underutilized) -->
  <case pattern="Validate plan before implementation (T2+)">
    <tool>MCP reasoning tools (code-reasoning or shannon-thinking) or Task tool with self-reflection prompt</tool>
    <tier>T2: recommended, T3+: MANDATORY</tier>
  </case>
  <case pattern="Before claiming task/feature complete">
    <tool>MCP reasoning tools or Task tool with verification prompt</tool>
    <note>Verification gate - assume broken until proven</note>
  </case>
  <case pattern="Review approach after 2 failed fixes">
    <tool>MCP reasoning tools for root cause analysis</tool>
    <note>Two-Strike Rule validation</note>
  </case>

  <!-- Frontend Specialist -->
  <case pattern="React/Vue/Angular component design">
    <tool>Task tool with frontend specialist prompt</tool>
  </case>
  <case pattern="CSS/styling/responsive layout issues">
    <tool>Task tool with frontend specialist prompt</tool>
  </case>
  <case pattern="Frontend state management (Redux/Zustand/Context)">
    <tool>Task tool with frontend specialist prompt</tool>
  </case>
  <case pattern="UI/UX implementation decisions">
    <tool>Task tool with frontend specialist prompt</tool>
  </case>

  <!-- Backend Specialist -->
  <case pattern="API endpoint design (REST/GraphQL/gRPC)">
    <tool>Task tool with backend specialist prompt</tool>
  </case>
  <case pattern="Database schema/query optimization">
    <tool>Task tool with backend specialist prompt</tool>
  </case>
  <case pattern="Server-side authentication/authorization">
    <tool>Task tool with backend specialist prompt</tool>
  </case>
  <case pattern="Microservices architecture decisions">
    <tool>Task tool with backend specialist prompt</tool>
  </case>

  <!-- DevOps Engineer -->
  <case pattern="CI/CD pipeline design (GitHub Actions/GitLab CI)">
    <tool>Task tool with DevOps prompt</tool>
  </case>
  <case pattern="Docker/container configuration">
    <tool>Task tool with DevOps prompt</tool>
  </case>
  <case pattern="Kubernetes/infrastructure setup">
    <tool>Task tool with DevOps prompt</tool>
  </case>
  <case pattern="Deployment strategy/rollback planning">
    <tool>Task tool with DevOps prompt</tool>
  </case>

  <!-- QA Engineer -->
  <case pattern="Test strategy/architecture design">
    <tool>Task tool with QA prompt</tool>
  </case>
  <case pattern="Test coverage analysis/gaps">
    <tool>Task tool with QA prompt</tool>
  </case>
  <case pattern="E2E/integration test planning">
    <tool>Task tool with QA prompt</tool>
  </case>

  <!-- Security Engineer -->
  <case pattern="Authentication/authorization design">
    <tool>Task tool with security prompt</tool>
  </case>
  <case pattern="OWASP vulnerability check">
    <tool>Task tool with security prompt</tool>
  </case>
  <case pattern="Crypto/secrets management">
    <tool>Task tool with security prompt</tool>
  </case>

  <!-- Technical Writer -->
  <case pattern="README/documentation needed">
    <tool>Task tool with technical writing prompt</tool>
  </case>
  <case pattern="API documentation generation">
    <tool>Task tool with technical writing prompt</tool>
  </case>

  <!-- Strategy / Analysis (rare usage) -->
  <case pattern="Product requirements/user stories">
    <tool>Task tool with product owner prompt</tool>
  </case>
  <case pattern="Project timeline/milestone planning">
    <tool>Task tool with project manager prompt</tool>
  </case>
  <case pattern="Technology strategy/roadmap">
    <tool>Task tool with architecture prompt</tool>
  </case>
  <case pattern="Extract reusable insights/patterns">
    <tool>Task tool with knowledge analysis prompt</tool>
  </case>

  <!-- TDD -->
  <case pattern="Implementing new feature or bugfix (T2+)">
    <skill>test-driven-development</skill>
    <enforcement>MANDATORY</enforcement>
  </case>

  <!-- Spec Review -->
  <case pattern="Task implementation complete, before code review">
    <tool>Task tool with spec-reviewer prompt</tool>
    <note>Verify spec compliance FIRST</note>
  </case>

  <!-- Code Review -->
  <case pattern="Spec review passed, ready for code quality review">
    <tool>Task tool with code-review prompt</tool>
    <note>Only after spec compliance passes</note>
  </case>

  <!-- Verification -->
  <case pattern="About to claim work complete or fixed">
    <skill>verification-before-completion</skill>
    <note>Evidence before claims, always</note>
  </case>

  <!-- Debugging -->
  <case pattern="2+ failed fixes, Two-Strike triggered">
    <skill>systematic-debugging</skill>
    <note>Four-phase debugging, question architecture after 3 failures</note>
  </case>

  <!-- Branch Completion -->
  <case pattern="All tasks complete, ready to finish branch">
    <skill>finishing-a-development-branch</skill>
    <note>Tests -> Options -> Execute with quality gates</note>
  </case>
</decision-tree>

## Quick Dispatch Table

For rapid selection, use this condensed table:

| Need | Tool / Approach |
|------|-----------------|
| File patterns, code search | `Grep` / `Glob` |
| Architecture, "how does X work" | `Grep` + `Read` to trace code flow |
| External docs, multi-step research | `WebSearch` / `WebFetch` / `Context7` / `Task` tool |
| Spec analysis, vague requirements | `spec-analyzer` skill |
| Plan validation (T2+: rec, T3+: MANDATORY) | MCP reasoning tools or `Task` tool with self-reflection prompt |
| React/Vue/CSS/UI | `Task` tool with frontend specialist prompt |
| API/DB/Auth backend | `Task` tool with backend specialist prompt |
| CI/CD, Docker, K8s | `Task` tool with DevOps prompt |
| Test strategy, coverage | `Task` tool with QA prompt |
| Security, OWASP, crypto | `Task` tool with security prompt |
| README, API docs | `Task` tool with technical writing prompt |
| TDD implementation (T2+) | `test-driven-development` skill |
| Task complete, before review | `Task` tool with spec-reviewer prompt |
| 2+ failed fixes | `systematic-debugging` skill |
| Branch complete | `finishing-a-development-branch` skill |

## Usage Examples

### Example 1: Unfamiliar Codebase
```
Task: "Implement authentication middleware"
Decision: Use Grep to search for "authentication", "middleware", "auth" patterns + Read key files
Reason: Architecture exploration before coding
```

### Example 2: Plan Validation
```
Task: Created task_plan.md for T3 task
Decision: Use MCP reasoning tools (code-reasoning or shannon-thinking) to review plan
Reason: T3+ MANDATORY self-reflection before implementation
```

### Example 3: Two-Strike Triggered
```
Task: Third failed fix attempt
Decision: Load systematic-debugging skill
Reason: Systematic root cause analysis required
```

## Integration with MASTER CHECKLIST

This skill is referenced in **Step 7 (Exploration)** of the MASTER CHECKLIST:
- **7b. Tool / Agent Selection (use decision tree, not all tools at once)**

Load this skill when you need detailed guidance on which tool or approach to use for a specific task type.
