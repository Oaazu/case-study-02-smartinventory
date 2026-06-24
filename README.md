# SmartInventory — Demand-Driven Inventory Analytics for QuickMart

> A data analytics system that identifies stockout risk, models demand patterns, and delivers reorder recommendations from 90 days of sales data.

---

## The Business Problem

QuickMart was losing measurable revenue every week to preventable stockouts on its highest-demand grocery items — with shortages concentrated on weekends and seasonal peaks.

The root cause wasn't supply. It was a fixed reorder schedule that ignored actual sales velocity, day-of-week demand, and seasonal trends. Shelves ran empty precisely when customer traffic was highest.

**This project replaces schedule-based inventory management with a data-driven system that puts replenishment ahead of demand, not behind it.**

---

## What the System Does

- Analyzes **8,100 sales records across 90 products over a 90-day window**
- Detects **weekend demand surges** (1.2x–2.5x baseline) and flags high-risk SKUs
- Identifies **seasonal peaks** in July and December (30–80% above daily averages)
- Surfaces **top stockout-exposed categories**: Dairy, Meat, and Produce
- Generates **dynamic reorder recommendations** tied to each product's actual sales velocity
- Exports findings to CSV for reporting and further analysis

---

## Key Findings

| Finding | Detail |
|---|---|
| Weekend surge | Saturday/Sunday sales 1.2x–2.5x weekday baseline across all categories |
| Seasonal peaks | July and December run 30–80% above normal daily units sold |
| Most exposed categories | Dairy, Meat, Produce — highest velocity, highest stockout risk |
| Root cause | Fixed reorder schedule structurally misaligned with actual demand patterns |

---

## Recommendations Delivered

1. **Switch to demand-driven reordering** — dynamic triggers tied to each product's base sale rate and weekend multiplier
2. **Implement weekend pre-stocking** — lift Thursday/Friday reorder quantities by 50%+ for items with weekend multiplier above 1.5x
3. **Build seasonal buffers** — raise safety stock 40% across Dairy, Meat, and Produce beginning mid-June and mid-November

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Data modeling | SQLAlchemy, SQLite |
| Data generation | Faker (realistic synthetic sales data) |
| Dashboard | Streamlit |
| Data processing | pandas |
| Export | CSV via Python standard library |

---

## Project Structure

```
case-study-02-smartinventory/
├── app.py              # Streamlit dashboard — main entry point
├── database.py         # Database connection and session management
├── models.py           # SQLAlchemy ORM models (products, sales, inventory)
├── seed.py             # Synthetic data generation with Faker
├── export.py           # CSV export functionality
├── quickmart_sales.csv # Exported sales dataset
├── requirement.txt     # Python dependencies
├── QuickMart_Business_Memo.docx        # Full business memorandum
└── QuickMart_SmartInventory_Presentation.pptx  # Stakeholder presentation
```

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Oaazu/case-study-02-smartinventory.git
cd case-study-02-smartinventory

# 2. Install dependencies
pip install -r requirement.txt

# 3. Seed the database with synthetic sales data
python seed.py

# 4. Launch the dashboard
streamlit run app.py
```

---

## Deliverables

This project was delivered as a full business case, not just a technical build:

- **Business memo** — executive-ready findings and recommendations for store management
- **Stakeholder presentation** — visual walkthrough of the analysis and proposed changes
- **Interactive dashboard** — live Streamlit app for ongoing inventory monitoring
- **Exported dataset** — `quickmart_sales.csv` for downstream reporting

---

## Context

Built as part of the AI Engineering Fellowship at **The Knowledge House** — a program focused on applying data and AI skills to real business problems.

The scenario is fictional (QuickMart), but the methodology is directly applicable to any retail or grocery operation managing high-velocity SKUs across fluctuating demand cycles.

---

*Jeffrey Arzu · https://github.com/Oaazu/case-study-02-smartinventory · LinkedIn: https://www.linkedin.com/in/jarzu-jeffrey/*
