with open('caba_cases.csv', 'r') as data:
    with open('clean_caba_cases.csv', 'w') as output:
        for line in data:
            splitted_line = line.split('\t')
            splitted_line[0] = splitted_line[0].split(' ')[0]
            output.write('\t'.join(splitted_line))