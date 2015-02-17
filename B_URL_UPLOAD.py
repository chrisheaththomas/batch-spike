import re

def validate( url ):
    p = re.compile('^[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU)[a-zA-Z0-9\-\./]*$')
    m = p.match(url)

    if m:
        is_match = True
    else:
        is_match = False

    return is_match

#FOR_EACH record in the input data set
	#IF(URL valid)
		#INSERT/UPDATE URL table
	#ELSE
		#CREATE ERROR record
	#ENDIF
#ENDLOOP