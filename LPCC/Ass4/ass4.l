%{

#include "y.tab.h" 
extern int yylval;

%}

%%

[0-9]+	{yylval=atoi(yytext);return number;}
[ \t] {;}		/* ignore whitespace */	
[-+*/\n]	return *yytext;

[\n]+	{return 0; }	/*logical EOF*/

=	{return yytext[0];}


%%
