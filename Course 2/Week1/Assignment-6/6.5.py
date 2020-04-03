text = "X-DSPAM-Confidence:    0.8475"
num=text.find("0")
newtext=text[num:]
print(float(newtext))
