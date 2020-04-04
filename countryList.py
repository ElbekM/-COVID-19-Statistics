
def getByCountryName(country):
    return country_dict.get(country)

def listOfCountries():
    string = ""
    for key, value in country_dict.items():
        string += key + '\n'
    return string

country_dict = {'afghanistan': 'AF', 'albania': 'AL', 'algeria': 'DZ', 'andorra': 'AD', 'angola': 'AO', 'antigua': 'AG', 'argentina': 'AR', 'armenia': 'AM', 'austria': 'AT', 'azerbaijan': 'AZ', 'bahamas': 'BS', 'bahrain': 'BH', 'bangladesh': 
'BD', 'barbados': 'BB', 'belarus': 'BY', 'belgium': 'BE', 'benin': 'BJ', 'bhutan': 'BT', 'bolivia': 'BO', 'bosnia': 'BA', 'brazil': 'BR', 'brunei': 'BN', 'bulgaria': 'BG', 'burkina': 'BF', 'cabo': 'CV', 'cambodia': 'KH', 'cameroon': 'CM', 'central': 'CF', 'chad': 'TD', 'colombia': 'CO', 'costa': 'CR', 'cote': 'CI', 'croatia': 'HR', 'diamond': 'XX', 'cuba': 'CU', 'cyprus': 'CY', 'czechia': 'CZ', 'djibouti': 'DJ', 'dominican': 'DO', 'ecuador': 'EC', 'egypt': 'EG', 'el': 'SV', 'equatorial': 'GQ', 'eritrea': 'ER', 'estonia': 'EE', 'eswatini': 'SZ', 'ethiopia': 'ET', 'fiji': 'FJ', 'finland': 'FI', 'gabon': 'GA', 'gambia': 'GM', 'georgia': 'GE', 'germany': 'DE', 'ghana': 'GH', 'greece': 'GR', 'guatemala': 'GT', 'guinea': 'GN', 'guyana': 'GY', 'haiti': 'HT', 'holy': 'VA', 'honduras': 'HN', 'hungary': 'HU', 'iceland': 'IS', 'india': 'IN', 'indonesia': 'ID', 'iran': 'IR', 'iraq': 'IQ', 'ireland': 'IE', 'israel': 'IL', 'italy': 'IT', 'jamaica': 'JM', 'japan': 'JP', 'jordan': 'JO', 'kazakhstan': 'KZ', 'kenya': 'KE', 'korea,': 'KR', 'kuwait': 'KW', 'kyrgyzstan': 'KG', 'latvia': 'LV', 'lebanon': 'LB', 'liberia': 'LR', 'liechtenstein': 'LI', 'lithuania': 'LT', 'luxembourg': 'LU', 'madagascar': 'MG', 'malaysia': 'MY', 'maldives': 'MV', 'malta': 'MT', 'mauritania': 'MR', 'mauritius': 'MU', 'mexico': 'MX', 'moldova': 'MD', 'monaco': 'MC', 'mongolia': 'MN', 
'montenegro': 'ME', 'morocco': 'MA', 'namibia': 'NA', 'nepal': 'NP', 'new': 'NZ', 'nicaragua': 'NI', 'niger': 'NE', 'nigeria': 'NG', 'north': 'MK', 'norway': 'NO', 'oman': 'OM', 'pakistan': 'PK', 'panama': 'PA', 'papua': 'PG', 
'paraguay': 'PY', 'peru': 'PE', 'philippines': 'PH', 'poland': 'PL', 'portugal': 'PT', 'qatar': 'QA', 'romania': 'RO', 'russia': 'RU', 'rwanda': 'RW', 'saint': 'KN', 'san': 'SM', 'saudi': 'SA', 'senegal': 'SN', 'serbia': 'RS', 
'seychelles': 'SC', 'singapore': 'SG', 'somalia': 'SO', 'south': 'ZA', 'spain': 'ES', 'sri': 'LK', 'sudan': 'SD', 'suriname': 'SR', 'sweden': 'SE', 'switzerland': 'CH', 'taiwan': 'TW', 'tanzania': 'TZ', 'thailand': 'TH', 'togo': 'TG', 'trinidad': 'TT', 'tunisia': 'TN', 'turkey': 'TR', 'uganda': 'UG', 'ukraine': 'UA', 'united': 'AE', 'uruguay': 'UY', 'usa': 'US', 'uzbekistan': 'UZ', 'venezuela': 'VE', 'vietnam': 'VN', 'zambia': 'ZM', 'zimbabwe': 'ZW', 'dominica': 'DM', 'grenada': 'GD', 'mozambique': 'MZ', 'syria': 'SY', 'timor-leste': 'TL', 'belize': 'BZ', 'canada': 'CA', 'laos': 'LA', 'libya': 'LY', 'west': 'PS', 'guinea-bissau': 'GW', 'mali': 'ML', 'kosovo': 'XK', 'burma': 'MM', 'ms': 'XX', 'botswana': 'BW', 'burundi': 'BI', 'sierra': 'SL', 'netherlands': 'NL', 'malawi': 'MW'}

'''
file = open('countries.txt', "r")
for line in file:
    country = line.strip().split()
    country_dict[country[1].lower()] = country[0]

file.close()

file = open('countries.txt', "w")

for i in data['locations']:
    file.write(i['country_code'] + " " + i['country'] + '\n')
    
file.close()
'''
