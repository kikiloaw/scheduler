import json
from advanced_scheduler import AdvancedSchoolScheduler

if __name__ == "__main__":
    with open("schedule.json", "r") as f:
        data = json.load(f)
    scheduler = AdvancedSchoolScheduler()
    scheduler.generate_schedule(data)
    scheduler.export_all_excel_schedules() 