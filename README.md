# MORF → RailMeets Automation

Automates the process of taking the MORF race schedule from
Midwest Open Racing Fleet and converting it into a properly formatted bulk upload CSV for RailMeets.

This replaces manual data entry with a fully reproducible Python workflow.

# What This Project Does
1. Scrapes the MORF schedule from
https://morfracing.net/wpmocha/schedule
2. Classifies race types (Buoy, Distance nearshore, Distance port-to-port, Double)
3. Transforms the data into the exact CSV format required by RailMeets bulk upload
4. Outputs a ready-to-upload file

## Project Structure
project/
│
├── morf_schedule/
│   ├── morf_schedule_YYYY.csv
│   └── railmeets_upload_YYYY.csv
│
├── 1_morf_schedule_scraper.ipynb
├── 2_morf_to_railmeets.ipynb
└── README.md

## Notebook 1 — MORF Schedule Scraper

**Goal:** Pull the full MORF schedule table and clean it.

### Key steps
- Scrape the schedule table (shows all regattas)
- Waterfall missing dates downward
- Drop rows with blank Course
- Remove Beer Can races
- Create `Race Type`.

**Output**
```
morf_schedule/morf_schedule_YYYY.csv
```
Clean, normalized MORF schedule.

## Notebook 2 — MORF → RailMeets Formatter

**Goal:** Convert MORF schedule into RailMeets bulk upload format.

**RailMeets Required Columns**

```
Event Date
Event Time
Timezone
Fleet
Sponsoring Club
Series
Event
Race Type
Location
Website Link
```

**Mapping Logic**

|    RailMeets    |      Source     |            Rule           |
|:---------------:|:---------------:|:-------------------------:|
| Event Date      | Date            | YYYY-MM-DD                |
| Event Time      | Start Time      | 24-hour HH:MM             |
| Timezone        | Static          | America/Chicago           |
| Fleet           | Static          | MORF                      |
| Sponsoring Club | Static          | Midwest Open Racing Fleet |
| Series          | Series Type     | "MORF " + Series Type     |
| Event           | Event - Results | merged race names         |
| Race Type       | Derived         | from earlier logic        |
| Location        | Static          | Chicago IL USA            |
| Website Link    | Static          | MORF site                 |

