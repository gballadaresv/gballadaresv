int main() {

    int var = 5;
    // &var es la dirección de la variable (puntero)
    int* ptr = &var;
    // type* indica que es tipo puntero para una variable de tipo type

    // *ptr es el valor guardado en la dirección del puntero (int)
    int value = *ptr;
    // *ptr accede al valor guardado en memoria


    struct aa {
        int a;
        float b;
        char c;
        char d[10];
    };

    struct aa x {
        .a = 10;
        .b = 3.14;
        .c = 'z';
        .d = "String"
    };

    return 0;
}