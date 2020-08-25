import openpyxl, os, smtplib
os.chdir('F://automate_online-materials')
#reading and saving datas from the excel
#this code has been writtten for members who has not paid for one or more than one month
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
person ={}
for row in range(2,8):
    for column in 'CDEFGH':
        if(sheet[str(column) + str(row)].value == None):
            member_name =  sheet['A' + str(row)].value
            mail_name = sheet['B' + str(row)].value
            person.setdefault(member_name, {})
            person[member_name] = mail_name
print(person)
print('writing results...')
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('uranium235exist@gmail.com', 'iamanindustrialist')
for name, email in person.items():
    body = "Subject: Dues unpaid.\nDear %s, \nRecords show that you have not paid dues.Please make this payment as soon as possible. Thank you!'"%(name)
    print("Sending mails to %s..." % email)
    sendmailStatus = smtpObj.sendmail('uranium235exist@gmail.com', email, body)
    if sendmailStatus != {}:
        print('There was a problem sending mail to%s: %s' % (email, sendmailStatus))
    print(sendmailStatus)
smtpObj.quit()





