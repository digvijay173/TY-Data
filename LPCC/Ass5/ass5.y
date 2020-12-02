%{
#include <stdio.h>
void yyerror(char*);
int yylex(void);
char n ='A';
int i=0;
%}

%token NUM
%token ID
%left '+''-''*''/'
%nonassoc UMINUS
%%

S : E {printf("x=%c\n",n-1);}

;

E:     	NUM{}
	|E'+'E{if(i==0){ printf("%c = %d %c %d\n",n,$1,'+',$3); n++;i++;}
	else{ printf("%c = %c %c %d\n",n,n-1,'+',$3);n++;}}
	|E'-'E{if(i==0){ printf("%c = %d %c %d\n",n,$1,'-',$3); n++;i++;}
	else{ printf("%c = %c %c %d\n",n,n-1,'-',$3);n++;}}
	|E'*'E{if(i==0){ printf("%c = %d %c %d\n",n,$1,'*',$3); n++;i++;}
	else{ printf("%c = %c %c %d\n",n,n-1,'*',$3);n++;}}
	|E'/'E{if(i==0){ printf("%c = %d %c %d\n",n,$1,'/',$3); n++;i++;}
	else{ printf("%c = %c %c %d\n",n,n-1,'/',$3);n++;}}
;

%%
void yyerror(char* s)
{
	fprintf(stderr,"%s\n",s);
}

int yywrap()
{
	return 1;
}
int main()
{

	printf("Enter Expression x => ");
	yyparse();
	yywrap();
	return 0;
}
