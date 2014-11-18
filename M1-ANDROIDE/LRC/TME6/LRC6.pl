compositionBase(<,<,[<]).
compositionBase(<,m,[<]).
compositionBase(<,o,[<]).
compositionBase(<,et,[<]).
compositionBase(<,s,[<]).
compositionBase(<,d,[<,m,o,s,d]).
compositionBase(<,dt,[<]).
compositionBase(<,e,[<,m,o,s,d]).
compositionBase(<,st,[<]).
compositionBase(<,ot,[<,m,o,s,d]).
compositionBase(<,mt,[<,m,o,s,d]).
compositionBase(<,>,[<,>,m,mt,o,ot,e,et,s,st,d,dt,=]).
compositionBase(m,m,[<]).
compositionBase(m,o,[<]).
compositionBase(m,et,[<]).
compositionBase(m,s,[m]).
compositionBase(m,d,[o,s,d]).
compositionBase(m,dt,[<]).
compositionBase(m,e,[o,s,d]).
compositionBase(m,st,[m]).
compositionBase(m,ot,[o,s,d]).
compositionBase(m,mt,[e,et,=]).
compositionBase(o,o,[<,m,o]).
compositionBase(o,et,[<,m,o]).
compositionBase(o,s,[o]).
compositionBase(o,d,[o,s,d]).
compositionBase(o,dt,[<,m,o,et,dt]).
compositionBase(o,e,[o,s,d]).
compositionBase(o,st,[o,et,dt]).
compositionBase(o,ot,[o,ot,e,et,d,dt,st,s,=]).
compositionBase(s,et,[<,m,o]).
compositionBase(s,s,[s]).
compositionBase(s,d,[d]).
compositionBase(s,dt,[<,m,o,et,dt]).
compositionBase(s,e,[d]).
compositionBase(s,st,[s,st,=]).
compositionBase(et,s,[o]).
compositionBase(et,d,[o,s,d]).
compositionBase(et,dt,[dt]).
compositionBase(et,e,[e,et,=]).
compositionBase(d,d,[d]).
compositionBase(d,dt,[<,>,m,mt,o,ot,e,et,s,st,d,dt,=]).
compositionBase(dt,d,[o,ot,e,et,d,dt,st,s,=]).

symetrique(<,>).
symetrique(>,<).
symetrique(e,s).
symetrique(s,e).
symetrique(et,st).
symetrique(st,et).
symetrique(d,d).
symetrique(m,mt).
symetrique(dt,dt).
symetrique(mt,m).
symetrique(o,ot).
symetrique(ot,o).
symetrique(=,=).

symetrique([],[]).
symetrique([T1|Q1],[T2|Q2]):-symetrique(T1,T2),symetrique(Q1,Q2).

transpose(<,>).
transpose(>,<).
transpose(e,et).
transpose(s,st).
transpose(et,e).
transpose(st,s).
transpose(d,dt).
transpose(m,mt).
transpose(dt,d).
transpose(mt,m).
transpose(o,ot).
transpose(ot,o).
transpose(=,=).

transpose([],[]).
transpose([T1|Q1],[T2|Q2]):-transpose(T1,T2),transpose(Q1,Q2).

composite(R1,R2,Z):-symetrique(R1,X),symetrique(R2,Y),compositionBase(X,Y,L),symetrique(L,Z).
composite(R1,R2,Z):-transpose(R1,X),transpose(R2,Y),compositionBase(Y,X,L),transpose(L,Z).


composite(R1,R2,L):-compositionBase(R1,R2,L).


