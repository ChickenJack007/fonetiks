english = input('english to convert:\n')
thornmode = input(':: is thorn mode enabled? [Y/n] ')
while thornmode != 'Y' and thornmode != 'n':
    thornmode = input(':: that didn\'t work. is thorn mode enabled? [Y/n] ')
if thornmode == 'Y':
    english = english.replace('th','þ')
elif thornmode == 'n':
    english = english.replace('th','ð')
else:
    print('sorry, thornmode toggle could not be determined.') #might be redundant
english = english.replace('sh','ʃ')
english = english.replace('tio','ʃo')
english = english.replace('co','ko') #soft c -> s
english = english.replace('cu','ku') #hard c -> k
english = english.replace('ca','ka') #ch sound -> c
english = english.replace('ic','ik')
english = english.replace('ci','si')
english = english.replace('ce','se')
english = english.replace('ch','c')
english = english.replace('ec','ek')
english = english.replace('cem','kem')
english = english.replace('ng','ŋ')
english = english.replace('ph','f')
english = english.replace('cough','koff')
english = english.replace('laugh','laff')
english = english.replace('gh','')
english = english.replace('ax','aks')
english = english.replace('ox','oks')
english = english.replace('ux','uks')
english = english.replace('ix','iks')
english = english.replace('ex','eks')
english = english.replace('x','z')
english = english.replace('oo','u')
# english = english.replace('ge','j')
english = english.replace('throu','thru')
print('sorry this may not be perfect (it isnt) and you may need to make edits after.\nbut the output is:\n'+english)

