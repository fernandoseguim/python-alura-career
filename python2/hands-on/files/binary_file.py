logo = open('python-logo.png', 'rb')
data_file = logo.read()
logo.close()


new_logo = open('new-python-logo.png', 'wb')
new_logo.write(data_file)
logo.close()