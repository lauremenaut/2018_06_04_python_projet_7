var dialogueAreaElt = document.getElementById("dialogue_area");
var queryFieldElt = document.getElementById("query_field");

document.addEventListener("keypress", function(e) {
    console.log("Appuyé sur : " + e.charCode);
    if (e.charCode == 108) {
        console.log("Bien appuyé sur le 'l' !");
        console.log("queryFieldElt.value : " + queryFieldElt.value);
        var pElt = document.createElement("p");
        var form = document.querySelector("form");
        pElt.textContent = form.elements[0].value;
        console.log("pElt.textContent : " + pElt.textContent);
        dialogueAreaElt.appendChild(pElt);
    }
});
