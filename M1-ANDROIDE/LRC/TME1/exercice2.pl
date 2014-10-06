et(0,1,0).
et(0,0,0).
et(1,0,0).
et(1,1,1).

ou(0,0,0).
ou(0,1,1).
ou(1,0,1).
ou(1,1,1).

non(0,1).
non(1,0).

nand(X,Y,Z):-et(X,Y,A),non(A,Z).

xor(A,B):-ou(A,B,1),not(et(A,B,1)).

xor(A,B,Z):-non(A,C),non(B,D),et(C,B,E),et(A,D,F),ou(E,F,Z).

circuit(X,Y,Z):-nand(X,Y,A),non(X,B),xor(A,B,C),non(C,Z).
