%{
#include "y.tab.h"
extern int yylval;

%}

%%

[A-Za-z]([A-Za-z][0-9])* return ID;

[0-9]+ {yylval=atoi(yytext);return NUM;}

. {return yytext[0];}

\n {return 0;}

%%
