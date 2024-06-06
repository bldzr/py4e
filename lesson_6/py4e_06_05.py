str = 'X-DSPAM-Confidence: 0.8475'

colon = str.find(':')

num_str = str[colon+1:]

num_str.strip()

num = float(num_str)

print(num)