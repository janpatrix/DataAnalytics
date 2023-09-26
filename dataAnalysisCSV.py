import unicodecsv
import dataParser as dP

enrollments_filename = "./CSV/enrollments.csv"
daily_engagement = "./CSV/daily_engagement.csv"
project_submissions = "./CSV/project_submissions.csv"

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

for r in enrollments:
    r['account_key'] = dP.parse_to_int(r['account_key'])
    r['join_date'] = dP.parse_to_date(r['join_date'])
    r['cancel_date'] = dP.parse_to_date(r['cancel_date'])
    r['days_to_cancel'] = dP.parse_to_int(r['days_to_cancel'])
    r['is_udacity'] = dP.parse_to_bool(r['is_udacity'])
    r['is_canceled'] = dP.parse_to_bool(r['is_canceled'])

with open(daily_engagement, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    engagement = list(reader)

for r in engagement:
    
    r['account_key'] = r.pop('acct')
    r['account_key'] = int(r['account_key'])
    r['utc_date'] = dP.parse_to_date(r['utc_date'])
    r['num_courses_visited'] = int(float(r['num_courses_visited']))
    r['total_minutes_visited'] = float(r['total_minutes_visited'])
    r['lessons_completed'] = int(float(r['lessons_completed']))
    r['projects_completed'] = int(float(r['projects_completed']))

with open(project_submissions, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    submissions = list(reader)

for r in submissions:
    r['creation_date'] = dP.parse_to_date(r['creation_date'])
    r['completion_date'] = dP.parse_to_date(r['completion_date'])
    r['account_key'] = dP.parse_to_int(r['account_key'])
    r['lesson_key'] = dP.parse_to_int(r['lesson_key'])

#Questions to answer
#1. How long, did it take the students to work on incomplete Projects
#2. Average time until a studend cancelled the subscription
#3. How many canceled after projects was incomplete?
#4. How many courses and how many minutes? Does that correlate?
#5. Number of courses visited, number of projects comepletes, number of lessons completed

unique_enrolled_students = set([row['account_key'] for row in enrollments])
unique_engaged_acc = set([row['account_key'] for row in engagement])
unique_submission_acc = set([row['account_key'] for row in submissions])

print("Accounts Enrollments: " + str(len(enrollments)))
print("Unique Accounts Enrollments: " + str(len(unique_enrolled_students)))
print("Accounts Engagement: " + str(len(engagement)))
print("Unique Accounts Engagement: " + str(len(unique_engaged_acc)))
print("Accounts Submission: " + str(len(submissions)))
print("Unique Accounts Submission: " + str(len(unique_submission_acc)))

#Problems in the data:
#1. More students in enrollment than in engagement -> should be the same
#2. account_key != acct