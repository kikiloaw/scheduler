from advanced_scheduler import AdvancedSchoolScheduler
from sample_data import sample_class_data

if __name__ == "__main__":
    # Print first two courses from section 3A to confirm data
    for class_group in sample_class_data:
        for course in class_group['Courses']:
            if course['section'] == '3A':
                print(f"Sample 3A course: {course['coursename']} | classschedule: {course['classschedule']}")
    scheduler = AdvancedSchoolScheduler()
    schedule = scheduler.generate_schedule(sample_class_data)
    scheduler.export_schedule("schedule.json")
    print(f"Scheduled classes: {len(schedule)}")
    # Print unscheduled classes for section 3A (and IT 402 specifically)
    print("\nUnscheduled classes for section 3A:")
    for class_group in sample_class_data:
        for course in class_group['Courses']:
            if course['section'] == '3A':
                for sched in course['classschedule']:
                    found = False
                    for s in schedule:
                        if s['section'] == '3A' and s['coursename'] == course['coursename'] and s['roomid'] == sched['roomid'] and s['employee_id'] == sched['employeeid'] and s['duration'] == scheduler.parse_duration(sched['duration']):
                            found = True
                            break
                    if not found:
                        print(f"  {course['coursename']} | Room: {sched['roomid']} | Emp: {sched['employeeid']} | Duration: {sched['duration']}")
    scheduler.export_all_weekly_grids() 