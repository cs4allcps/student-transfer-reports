#encoding: utf-8

import matplotlib
import csv
import os
import errno

def main(filename):
	students = make_list_of_dicts_from(filename) 
	hs, ms, names = make_dicts(students)
	write_reports(hs, 'current', names)
	write_reports(ms, 'previous', names)
	#make_plots(hs, 'current', names)
	#make_plots(ms, 'previous', names)

def make_dicts(students):
	'''
	Creates reports on where 9th graders went to school before

	Input: list of dicts with student data

	Returns: (1) dict of of dicts of high schools with middle school counts
			(2) dict of dicts of middle schools with high schools counts
			(3) a dictionary {school_code: school_name}
	'''
	hs = {} # dict of dicts {high_school_id: {middle_school_id: count}} 
	ms = {} # dict of dicts {middle_school_id: {high_school_id: count}}
	directory = {}
	for student in students:
		if student:
			high_school_id = student['STUDENT_CURRENT_SCHOOL_CODE']
			high_school_name = student['STUDENT_CURRENT_SCHOOL']
			directory[high_school_id] = high_school_name
			middle_school_id = student['STUDENT_NEXT_OR_PREV_YEAR_SCHOOL_CODE']
			middle_school_name = student['STUDENT_NEXT_YEAR_SCHOOL_NAME']
			directory[middle_school_id] = middle_school_name
			if high_school_id in hs:
				hs[high_school_id][middle_school_id] = hs[high_school_id].get(middle_school_id, 0) + 1
			else:
				hs[high_school_id] = {middle_school_id: 1}
			if middle_school_id in ms:
				ms[middle_school_id][high_school_id] = ms[middle_school_id].get(high_school_id, 0) + 1
			else: 
				ms[middle_school_id] = {high_school_id: 1}
	return hs, ms, directory


def make_list_of_dicts_from(filename):
	'''
	http://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
	'''
	with open(filename) as f:
		reader = csv.reader(f, skipinitialspace=True)
		header = next(reader)
		a = [dict(zip(header, row)) for row in reader]
	return a 

def mkdir_p(path):
    '''
    http://stackoverflow.com/questions/600268
    '''
    try:
        os.makedirs(path)
    except OSError as exc:  # python > 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def write_reports(schools, report_type, names):

	mkdir_p('reports/' + report_type + '/csv_reports')
	for index in schools:
		school = schools[index]
		name = names[index]
		name = name.replace("/", " | ") #so as not to be confused with a filepath
		with open('reports/' + report_type + '/csv_reports/' + name + '.csv', 'w') as f:
			w = csv.writer(f)
			w.writerow(['School Code', 'School Name', 'Count'])
			for key in school:
				w.writerow([key, names[key], school[key]])


if __name__ == '__main__':
	main("Inbound9thGradeStudentCourseRecommendations.csv")


