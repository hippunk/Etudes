pere(pepin, charlemagne).
mere(berthe, charlemagne).
pere(david, arthur).
pere(aimer, david).
pere(yury, asya).
pere(alexandre, yury).
mere(anne-marie, arthur).
mere(galina, asya).
mere(anne-marie, hélène).
pere(david, hélène).
mere(galina, yevgeniy).
parent(X,Y):-mere(X,Y).
parent(X,Y):-pere(X,Y).
parents(X,Y,Z):-pere(X,Z),mere(Y,Z).
grandPere(X,Y):-pere(X,Z),parent(Z,Y).
frereOuSoeur(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.

ancetre(X,Y):-parent(X,Y).
ancetre(X,Y):-parent(Z,Y),ancetre(X,Z).
