%{

#include<stdio.h> 
void yyerror(char*); 
int yylex(void);

%}
%token number
%%

var1 :  exp	{printf("%d\n",$$); }
;

exp: exp '+' number {$$ = $1 + $3; }
| exp '-' number {$$ = $1 - $3; }
| exp '*' number {$$ = $1 * $3; }
| exp '/' number {$$ = $1 / $3; }
| number {$$ = $$;}
;

%%

void yyerror(char* s){
	fprintf(stderr,"%s\n",s);
}

int yywrap()
{
	return 1;
}
int main()
{
	yyparse(); 
	yywrap();
}

