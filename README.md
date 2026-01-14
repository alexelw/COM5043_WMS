# COM5043_WMS – Tooling, Setup, and Marking Alignment

## Requirements

* **Java 17**
* **Maven 3.9+**
* **Git**
* **GitHub account** (for CI and PR workflows)

## Installation

```bash
# Clone repository
git clone https://github.com/alexelw/COM5043_WMS.git
cd COM5043_WMS

# Verify build toolchain
java -version
mvn -version
```

## Run Instructions

```bash
# Run full build, tests, and static analysis
mvn clean verify

# Check formatting only
mvn spotless:check
```

---

## Marking Criteria Alignment

### Design (20%)


### Implementation (50%)

* **Java 17** selected to leverage a modern, strongly-typed OO language.
* Build pipeline enforces correctness via compilation, testing, and analysis.
* Tooling configured to scale as additional classes, packages, and features are added.

### Testing & Reflection (30%)

* **JUnit 5** integrated into the build lifecycle.
* **Static analysis tools** (Checkstyle, SpotBugs) used to reduce runtime error risk.
* **Automated CI via GitHub Actions** ensures consistent verification on every push and pull request.
* **PR review bot (reviewdog)** posts inline comments directly on pull requests, providing immediate, actionable feedback during development.
* **SonarCloud** used as an external quality gate to reflect on maintainability and code quality trends over time.

---

## DevOps & CASE Tooling Summary

* **GitHub Actions** – continuous integration and automated quality checks.
* **Checkstyle & SpotBugs** – CASE tools for static code analysis.
* **Spotless** – automated formatting enforcement.
* **PR Comment Bots** – simulated industry-style code review feedback.

