%{
#include<stdio.h>
#include<string.h>

char str_out [] = "VIIT";
char str_in [] =  "viit";

%}

%%

[a-zA-Z]+    { if(strcmp(yytext, str_in)==0)
                   fprintf(yyout, "%s", str_out);
                else
                    fprintf(yyout, "%s", yytext);}
.            fprintf(yyout, "%s", yytext);

%%

int yywrap()
{
    return 1;
}

int main()
{
        extern FILE *yyin, *yyout;
        yyin=fopen("input.txt", "r");
        yyout=fopen("output.txt", "w");

        yylex();
        fclose(yyin);
        fclose(yyout);
}
