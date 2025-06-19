from advanced_scheduler import AdvancedSchoolScheduler
from sample_data import sample_class_data

scheduler = AdvancedSchoolScheduler()
scheduler.generate_schedule(sample_class_data)
scheduler.export_schedule_csv("advanced_schedule.csv")
scheduler.export_schedule_timegrid_csv("advanced_schedule_timegrid.csv")
print("CSV export complete!")