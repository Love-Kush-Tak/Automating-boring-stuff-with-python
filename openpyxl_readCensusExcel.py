#Tabulates population and number of census tracts for each county
import openpyxl, pprint, os
os.chdir('F://automate_online-materials')
print('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
# TODO: Fill in countyData with each county's population and tracts
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    #tracts = sheet['A' + str(row)].value
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts' :0, 'pop':0})
    #print(countyData[state][county])
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')










