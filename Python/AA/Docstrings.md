## 📁 Project Module Architecture for Battery Test Tool

This structure breaks down the desktop app into clean, scalable modules:

---

### 1. **File Watcher**

**Purpose:** Monitors designated folders (e.g., company server share) for new `.mdc` or `.mf4` measurement files.

**Docstring:**

```python
"""
Module: FileWatcher
Watches a specific directory for new measurement files.
Triggers analysis jobs when new files are detected.
"""
```

**Key Tasks:**

* Periodically scan for new files
* Match naming patterns (e.g., category/date)
* Notify Analyzer of new input

---

### 2. **Analyzer**

**Purpose:** Handles core analysis logic — decodes measurements and validates them against test category parameters.

**Docstring:**

```python
"""
Module: Analyzer
Loads measurement files (.mdc/.mf4) and applies logic per test category.
Performs value checks, signal verification, and results packaging.
"""
```

**Key Tasks:**

* Load file (using `asammdf` or similar)
* Apply checks (ranges, tolerances, missing signals)
* Generate output (flags, summary, raw data subset)

---

### 3. **Inspector** (UI)

**Purpose:** User interface for exploring analyzed results, flags, and detailed signal data.

**Docstring:**

```python
"""
Module: Inspector
Graphical interface for viewing and reviewing processed test results.
Enables inspection of signals, errors, and metadata.
"""
```

**Key Tasks:**

* Show list of available results (local DB or file cache)
* Allow signal plotting (if needed)
* Highlight flagged issues or out-of-range signals

---

### 4. **Test Builder**

**Purpose:** Allows definition and editing of test templates — category name, required signals, expected ranges, mapping rules, etc.

**Docstring:**

```python
"""
Module: TestBuilder
Creates and manages test definitions (templates).
Maps signal names, ranges, and test-specific validation rules.
"""
```

**Key Tasks:**

* Load/save template files (JSON, YAML, DB)
* GUI (optional) for mapping signals
* Tag test categories based on filename patterns
* Provide validation helpers

---

### Example Flow:

```
┌────────────┐
│ FileWatcher│
└────┬───────┘
     │  detects
     ▼
┌────────────┐
│  Analyzer  │
└────┬───────┘
     │  produces
     ▼
┌────────────┐
│  Inspector │ ◄── allows navigation, inspection, filtering
└────┬───────┘
     ▲
     │ reads definitions from
┌────────────┐
│TestBuilder │
└────────────┘
```

Each module can live in its own folder with a clean `__init__.py`, plus a `main.py` or `run.py` script that ties them together.
