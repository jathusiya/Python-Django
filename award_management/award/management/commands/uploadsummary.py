# award/management/commands/uploadmodel.py
import csv
import os
from django.core.management.base import BaseCommand
from award.models import Summary

class Command(BaseCommand):
    help = 'Extract data from CSV and update Summary model'

    def handle(self, *args, **options):
        csv_file_path = 'interview.csv'  # Replace with the actual path to your CSV file

        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR('CSV file does not exist'))
            return

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            record_count = 0  # Initialize a counter to keep track of the number of records processed
            max_records = 100  # Define the maximum number of records to process

            for row in csv_reader:
                if record_count >= max_records:
                    break 

                # Extract data from CSV row
                school_name = row['School_Name']
                year = int(row['year'])
                student_id = int(row['Student_ID'])
                first_name = row['First name']
                last_name = row['Last Name']
                year_level = row['Year Level']
                class_name = row['Class']
                subject = row['Subject']
                answer = row['Answers']
                correct_answer = row['Correct Answers']
                question_number = int(row['Question Number'])
                subject_contents = row['Subject Contents']
                assessment_areas = row['Assessment Areas']
                sydney_correct_count_percentage = float(row['sydney_correct_count_percentage'])
                sydney_average_score = float(row['sydney_average_score'])
                sydney_participants = int(row['sydney_participants'])
                student_score = float(row['student_score'])
                student_total_assessed = float(row['student_total_assessed'])
                student_area_assessed_score = float(row['student_area_assessed_score'])
                total_area_assessed_score = float(row['total_area_assessed_score'])
                participant = row['participant']
                correct_answer_percentage_per_class = float(row['correct_answer_percentage_per_class'])
                average_score = float(row['average_score'])
                school_percentile = float(row['school_percentile'])
                sydney_percentile = float(row['sydney_percentile'])
                strength_status = row['strength_status']
                high_distinct_count = int(row['high_distinct_count'])
                distinct_count = int(row['distinct_count'])
                credit_count = int(row['credit_count'])
                participant_count = int(row['participant_count'])
                award = row['award']

                # Create or update the Summary model
                summary, created = Summary.objects.get_or_create(
                    school_name=school_name,
                    student_id=student_id,
                    year_level=year_level,
                    class_name=class_name,
                    subject=subject,
                    answer=answer,
                    correct_answer=correct_answer,
                    assessment_areas=assessment_areas,
                    sydney_participants=sydney_participants,
                    student_score=student_score,
                    participant=participant,
                    correct_answer_percentage_per_class=correct_answer_percentage_per_class,
                    sydney_percentile=sydney_percentile,
                    award=award,
                )

                summary.save()
                record_count += 1

                self.stdout.write(self.style.SUCCESS(f'Successfully updated {school_name} - {award}'))
