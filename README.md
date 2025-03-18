# Database Migration Project Structure

database-migration/
├── src/                      # Source code directory
│   ├── config/              # Configuration files
│   │   ├── __init__.py
│   │   └── database.py      # Database connection settings, environment handling
│   │
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   └── tables.py        # SQLAlchemy table definitions (Staff, WorkProfile, etc.)
│   │
│   ├── migrations/          # Migration management
│   │   ├── __init__.py
│   │   ├── versions/        # Individual migration scripts
│   │   └── env.py          # Migration environment configuration
│   │
│   └── utils/              # Utility functions
│       ├── __init__.py
│       └── helpers.py       # Common functions (password encoding, backup naming)
│
├── tests/                   # Test directory
│   ├── __init__.py
│   └── test_migrations.py   # Test cases for migrations
│
├── scripts/                 # Executable scripts
│   ├── backup.py           # Database backup functionality
│   └── migrate.py          # Main migration script
│
├── logs/                    # Log directory
│   └── migration.log       # Migration logs
│
├── .env                     # Environment variables
├── requirements.txt         # Project dependencies
├── README.md               # Project documentation
└── alembic.ini             # Alembic configuration

Key Components:

1. src/config/

   - Manages database connections
   - Handles environment variables
   - Configures logging
2. src/models/

   - Defines table structures
   - Manages relationships between tables
   - Contains schema definitions
3. src/migrations/

   - Stores migration scripts
   - Manages version control
   - Handles upgrades and rollbacks
4. src/utils/

   - Common helper functions
   - Shared utilities
   - Reusable code
5. tests/

   - Unit tests
   - Integration tests
   - Test fixtures
6. scripts/

   - Backup automation
   - Migration execution
   - Maintenance tasks
7. logs/

   - Migration history
   - Error tracking
   - Audit trails
