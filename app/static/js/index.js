var dialogueAreaElt = document.getElementById("dialogue_area");
var queryFieldElt = document.getElementById("query_field");

document.addEventListener("keypress", function(e) {
    console.log("Appuyé sur : " + e.charCode);
    if (e.charCode == 0) {
        console.log("Bien appuyé sur le 'l' !");
        var pElt = document.createElement("p");
        var form = document.querySelector("form");
        pElt.textContent = form.elements[1].value;
        dialogueAreaElt.appendChild(pElt);
    }
});
