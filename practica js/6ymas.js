//6

/*window.alert("Ingrese 2 numeros para conocer cual es mayor y cual menor");
var num1 = prompt("Ingrese primer numero");
var num2 = prompt("Ingrese segundo numero");

if (num1 > num2){
    document.write("El numero ",num1," es el mayor");
}else{
    document.write("El numero ",num2," es el mayor");
}
*/

//7
/*
window.alert("Ingrese 3 numeros para conocer cual es mayor y cual menor");
var num1 = prompt("Ingrese primer numero");
var num2 = prompt("Ingrese segundo numero");
var num3 = prompt("Ingrese tercer numero");

if (num1 > num2 && num>num3){
    document.write("El numero ",num1," es el mayor");
}else if (num1<num2  && num2>num3){
    document.write("El numero ",num2," es el mayor");
}else if(num3>num1 && num3>num2){
    document.write("El numero ",num3," es el mayor");

}*/

//8


/* window.alert("Ingrese un numero para saber si es divisible por 2");
var num = prompt("Ingrese el numero");

if (num % 2 == 0){
    document.write("El numero ",num," es divisible por 2");
}else{
    document.write("El numero ",num," NO es divisible por 2");
} */

//9
// Escribe un programa que pida una frase y escriba cuantas veces aparece la
// letra a

// var frase = prompt("Ingrese una frase:");
// let contador = 0;
// for (let i = 0; i < frase.length; i++) {
//     if (frase[i].toLowerCase() === 'a' ){
//         contador++;
//     }
// }

// document.write("La frase : '",frase,"' contiene ",contador, " veces la letra 'A'");

// 10. Escribe un programa que pida una frase y escriba las vocales que aparecen

var frase = prompt("Ingrese una frase:");
 let vocalesPresentes;
 for (let i = 0; i < frase.length; i++) {
     if (frase[i].toLowerCase() === 'a' || frase[i].toLowerCase() === 'e' || frase[i].toLowerCase() === 'i' || frase[i].toLowerCase() === 'o' || frase[i].toLowerCase() === 'u'){
         if()
         vocalesPresentes.frase[i] + " ";   }
  }
  document.write("La frase : '",frase,"' contiene las vocales ",vocalesPresentes)