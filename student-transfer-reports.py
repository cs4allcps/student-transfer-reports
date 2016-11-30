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

def make_txt_from_csv(csv_file, txt_file):
	'''
	http://codereview.stackexchange.com/questions/81990/manipulating-csv-files-to-regular-text-file
	'''
	# A simple program to create a formatted text file from a *.csv file.

	try:
		my_input_file = open(csv_file, "r")
	except IOError as e:
		print("I/O error({0}): {1}".format(e.errno, e.strerror))

	if not my_input_file.closed:
		text_list = [];
		for line in my_input_file.readlines():
			line = line.strip().split(",", 2)
			text_list.append("\t".join([line[2], line[0], line[1]]) + "\n")
		my_input_file.close()

	try:
		my_output_file = open(txt_file, "w")
	except IOError as e:
		print("I/O error({0}): {1}".format(e.errno, e.strerror))

	if not my_output_file.closed:
		for line in text_list:
			my_output_file.write(line)
		#print('File Successfully written.')
		my_output_file.close()

def write_reports(schools, report_type, names):
	'''
	Writes a csv report for each school with
		(1) For current schools: a list of all freshmans' previous schools with counts
		(2) For previous schools: a list of schools students matriculated to wiht counts
	'''
	mkdir_p('reports/' + report_type + '/csv_reports')
	mkdir_p('reports/' + report_type + '/txt_reports')
	for index in schools:
		school = schools[index]
		name = names[index]
		'''
		If using these reports for data alnalysis in conjunction with other datasets,
		it is important to note that any slash in the school name has been replaced with
		a bar in the report file names, as follows:
		'''
		name = name.replace("/", " | ") #so as not to be confused with a filepath
		with open('reports/' + report_type + '/csv_reports/' + name + '.csv', 'w') as f:
			w = csv.writer(f)
			w.writerow(['School Code', 'School Name', 'Count'])
			for key in school:
				w.writerow([key, names[key], school[key]])
		make_txt_from_csv('reports/' + report_type + '/csv_reports/' + name + '.csv', 'reports/' + report_type + '/txt_reports/' + name + '.txt')


if __name__ == '__main__':
	main("Inbound9thGradeStudentCourseRecommendations.csv")


