concatenate([],X,X).
concatenate([T|Q],A,[T|R]):-concatenate(Q,A,R).