/*==============================
**  Programa exemplo em miniC  
**
**  - fatora um inteiro lido.
**==============================
*/  

int main() {
	int num, div, resto;
	scan("Entre com o inteiro:", num);

	print("Fatorando...\n");
	print(num, " = ");

    // procura e imprime os fatores
    while (num > 1) {
        // encontra o menor fator
	    for (div = 2; num % div; div = div + 1);

	    print(div)
	    num = num / div;
	    if (num > 1)
	       print(" * ");
	}
	-1.4;
	2;
	-8;
	5.2;
    return 0;
} 
