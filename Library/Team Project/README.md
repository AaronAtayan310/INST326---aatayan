# Crime Data Research Pipeline Framework

A comprehensive Python framework for automated processing, analysis, and visualization of crime datasets to support evidence-based policy making and criminal justice research.

## Team Members

| Name | Role | Responsibilities |
|------|------|------------------|
| [Aaron Atayan] | Project Lead | Project coordinator and designer |
| [Vyvyan Mai] | Visualizations Lead | Visualization function designer |
| [Sean McLean] | Functionality Tester | Developer and designer |

## Domain Focus and Problem Statement

### Domain
Criminal justice analytics and urban crime pattern analysis

### Problem Statement
Law enforcement agencies and researchers face significant challenges in processing and analyzing crime data due to:

- **Data Fragmentation**: Crime data exists across multiple departments, formats, and systems with inconsistent structures
- **Manual Processing**: Current workflows require extensive manual cleaning and transformation, creating bottlenecks
- **Limited Reproducibility**: Ad-hoc analysis scripts are difficult to share, validate, and reproduce across research teams
- **Scalability Issues**: Growing datasets overwhelm existing tools, making comprehensive temporal and spatial analysis difficult

### Solution
This framework provides a standardized, reproducible pipeline that:
- Automates data ingestion from multiple sources (FBI UCR, NIBRS, local departments)
- Performs consistent validation and quality checks
- Enables modular analysis workflows
- Generates standardized outputs for reporting and further analysis
- Supports collaborative research through version-controlled, documented processes

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git for version control
- 4GB+ RAM recommended for larger datasets

### Installation Steps

FILL IN HERE

## Usage Examples

FILL IN HERE (from the main_functions)

## Function Library Overview

### Core Modules

```
crime_pipeline/
├── __init__.py                 # Package initialization
├── pipeline.py                 # Main Pipeline orchestrator
│
├── loaders/                    # Data ingestion modules
│   ├── __init__.py
│   ├── base.py                 # BaseLoader abstract class
│   ├── csv_loader.py           # CSV file loader
│   ├── json_loader.py          # JSON file loader
│   ├── api_loader.py           # REST API loader
│   └── database_loader.py      # SQL database loader
│
├── cleaners/                   # Data cleaning modules
│   ├── __init__.py
│   ├── data_cleaner.py         # Main cleaning functions
│   ├── validators.py           # Data validation checks
│   └── standardizers.py        # Format standardization
│
├── transformers/               # Data transformation modules
│   ├── __init__.py
│   ├── base.py                 # BaseTransformer abstract class
│   ├── feature_engineering.py  # Feature creation
│   ├── aggregators.py          # Data aggregation functions
│   └── normalizers.py          # Data normalization
│
├── analyzers/                  # Analysis modules
│   ├── __init__.py
│   ├── temporal.py             # Time-series analysis
│   ├── spatial.py              # Geographic analysis
│   ├── statistical.py          # Statistical methods
│   └── patterns.py             # Pattern detection
│
├── visualizers/                # Visualization modules
│   ├── __init__.py
│   ├── charts.py               # Statistical charts
│   ├── maps.py                 # Geographic maps
│   └── dashboards.py           # Interactive dashboards
│
└── utils/                      # Utility functions
    ├── __init__.py
    ├── config.py               # Configuration management
    ├── logging.py              # Logging utilities
    └── helpers.py              # Helper functions
```

### Key Classes and Functions

#### Pipeline Class (`pipeline.py`)
- `Pipeline(config)` - Initialize pipeline with configuration
- `.run(steps)` - Execute pipeline stages
- `.add_transformer(transformer)` - Add custom transformation
- `.export(format, path)` - Export results

#### DataLoader (`loaders/`)
- `load()` - Load data from source
- `validate_source()` - Check source availability
- `get_schema()` - Return data schema

#### DataCleaner (`cleaners/`)
- `remove_duplicates()` - Remove duplicate records
- `handle_missing_values(strategy)` - Handle nulls/NaNs
- `standardize_dates(format)` - Normalize date formats
- `validate_coordinates()` - Check geographic coordinates

#### Analyzers (`analyzers/`)
- **TemporalAnalyzer**: Time-based analysis functions
- **SpatialAnalyzer**: Geographic analysis functions
- **StatisticalAnalyzer**: Descriptive and inferential statistics

#### Visualizers (`visualizers/`)
- `create_time_series()` - Generate temporal charts
- `create_heatmap()` - Geographic heat maps
- `create_dashboard()` - Interactive dashboards

## Contribution Guidelines for Team Members

#### Getting Started
1. Ensure you have the latest code
2. Make your changes in the appropriate module
4. Write tests for new functionality
5. Update documentation as needed

#### Code Standards
- Follow PEP 8 style guidelines
- Use type hints for function parameters and returns
- Write docstrings for all public functions (Google style)
- Keep functions focused and under 50 lines when possible
- Use meaningful variable names (avoid single letters except in loops)
