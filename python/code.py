age=int(input('enter age'))
nationality=input('are you a citizen of india')
voter_id=input('do you have voter id?')
if nationality=='yes':
    if age>18:
        if voter_id=='yes':
            print('eligible')
        else:
            print('not eligible')
    else:
        print('f due to age')
else:
    print('f due to nationality')