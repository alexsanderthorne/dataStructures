questions = ['name' , 'quest', 'favorite color']
answers = ['lancelot' , 'the hole grail' , 'blue']

for q, a in zip(questions,answers):
    print(' Whats is your {0}? It is {1}.'.format(q,a))