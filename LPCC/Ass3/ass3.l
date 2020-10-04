%{
%}

%%

Jay|Viru|John|Abdul|are {printf("%s is a Noun",yytext);}
ran|walk|playing|dancing|sleeping {printf("%s: is a verb\n",yytext);}
at|in|on|from|above|below {printf("%s: is Preposition\n",yytext);}
effortlessly|simply|gently|quickly|slowly {printf("%s: is a adverb\n",yytext);}
and|or|also|so|but|if|then {printf("%s: is Conjuction\n",yytext);}
this|that|he|she|it|we|they|him|her|they {printf("%s: is Pronoun\n",yytext);}
[a-zA-Z]+  {printf("%s: don't recognize\n",yytext);}

%%

int yywrap(){
	return 1;
}
int main()
{
	yylex();
	yywrap();
	return 0;
}
