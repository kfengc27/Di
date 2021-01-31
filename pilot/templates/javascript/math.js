function generateMath(){
    num1 = rand(1, 100);
    console.log(num1);
    num2 = rand(1, 100);
    add = rand(0,1);
    if(num2>num1){add = 0};
      document.getElementById("math").style.display = 'block';
    document.getElementById("math").innerHTML=" Quick! Solve the following equation : " + num1 + " "+["+","-"][add]+" "+num2 + " = " ;
    document.getElementById("equ").innerHTML = '<input type="number" id="myNumber"> <button type="button" onclick="update()" id="myButton">Submit</button>'
    setTimeout(generateMath, 40000);
}