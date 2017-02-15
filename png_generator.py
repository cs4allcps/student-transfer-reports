import os
import sys
from draw_school import draw 

'''
generates treemaps for all schools and saves them to ./images
'''


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

def main():
	'''
	Must be in the same working directory as /reports, as has been generated
	by student-transfer-reports.py 
	'''
	if os.path.isdir('reports/'):
		for folder in ['current/', 'previous/']:
			out_dir = 'images/' + folder
			mkdir_p(out_dir)
			path = 'reports/' + folder + 'csv_reports/'
			filenames = os.listdir(path)
			for filename in filenames:
				if  filename[-3:] == 'csv' and filename[:-4] not in ['--', '']: #the notation for no data in original dashboard csv
					draw(path + filename, out_dir + filename[:-3] + 'png')
	else:
		print("'Reports' folder from student-transfer-reports.py not in working directory...")
		print('No data from which to generate images.')

if __name__ == '__main__':
	main()
