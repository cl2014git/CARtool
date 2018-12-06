def changestart(filepath):

	with open('filepath', 'r') as regions_file:
		with open('regions_fixed_file.bed', 'w') as myfile:
			for line in regions_file:
				element=line.split('\t')
				row = str(element[0]) + '\t' + str(int(element[1])-1) + '\t' + str(element[2]) + '\t' + str(element[3])
				myfile.write(row)
	regions_file.close()
	myfile.close()
	return '/regions_fixed_file.bed'
