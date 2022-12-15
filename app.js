
let up = document.querySelector("arrowUP");
up.addEventListener("touchstart", mouseUp1);
up.addEventListener("touchend", mouseDown1);
let down = document.querySelector("arrowDOWN");
down.addEventListener("touchstart", mouseUp2);
down.addEventListener("touchend", mouseDown2);


function mouseUp1()
{
    console.log("up p");
    
}
function mouseDown1()
{
    console.log("up r");
}

function mouseUp2()
{
   
    console.log("down p");
    
}
function mouseDown2()
{
    console.log("down r");
}


