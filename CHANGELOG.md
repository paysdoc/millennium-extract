# Changelog

All notable changes to the Millennium Card Producer project.

## [Unreleased]

### Added
- Multi-column sorting for `list-characters` command
  - Primary sort field option: `-s, --sort-by`
  - Secondary sort field option: `-s2, --sort-by-2`
  - Reverse sort option: `-r, --reverse`
  - Supported sort fields: id, name, category, birth_date, death_date, connections

### Fixed
- Import path issues when running CLI directly
- Python 3.13 compatibility with updated Pillow version
- Added missing `requests` dependency for image downloading

### Changed
- Requirements now use `>=` for better version compatibility
- Setup script now includes automated import testing

## [1.0.0] - Initial Release

### Added
- Supabase integration for fetching character and connection data
- Data denormalization (replaces character IDs with names)
- PDF generation with front and back card layouts
- Category-based color coding (10 categories)
- CLI interface with three commands:
  - `generate-all`: Generate PDF with all cards
  - `generate-single`: Preview a single card
  - `list-characters`: View all characters
- Comprehensive documentation (README, QUICK_START, PROJECT_SUMMARY)
- Automated setup script
- Import verification script
