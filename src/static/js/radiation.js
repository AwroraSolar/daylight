function getRadiation(){
    radiation = document.getElementById("avg-radiation");
    // el promedio de radiacion esta en kWh/m²/d
    var result = document.getElementById("radiation");
    // primero lo expresamos en Wh/m²/d y lo multiplicamos por el 10% que es la superficie de nuestra lente
    // Ademas lo multiplico por 0.2 calculando una eficiencia del 20% en nuestro producto
    result.innerHTML = Math.round((((radiation.value * 1000) * 0.1) * 0.2) * 100) / 100 + " Wh"xt;
}
