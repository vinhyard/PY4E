data = 'X-DSPAM-Confidence:0.8475'
atpos = data.find('0')
nipos = data.find('5')
host = data[19:25]
float(host)
print(host)
