inst(socrate,chat).
inst(amenophis,immortel).

subs(chat,mortel).
subs(mortel,some(parent,mortel)).
subs(mortel, all(croit_en,immortel)).
subs(and(mortel, immortel),nothing).

equi(sculpture,and(objet,all(cree_par,sculpteur))).
equi(artefact,and(objet,all(cree_par,personne))).
equi(parent,and(personne,some(a_enfant, anything))).
equi(sculteur,and(personne, some(a_cree,sculpture))).
equi(auteur, and(personne,some(a_ecrit,livre))).
equi(editeur,and(personne, and(not(some(a_ecrit,livre)),some(a_edite,livre)))).



inst(Y,D) :- subs(D,C), inst(Y,C).
subs(all(R,D),all(R,C)) :- subs(D,C).
subs(all(R,D),all(R,C)) :- inst(C,D).
subs(and(D1,C1) , and(D2,C2)) :- subs(D1,D2),subs(C1,C2).





