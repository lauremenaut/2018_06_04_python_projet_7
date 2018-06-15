// // On vide le champ de recherche
// var form = document.querySelector("form");
// var queryElt = form.elements[1];
// queryElt.textContent = "";

document.addEventListener("keypress", function(e) {
    if (e.key == "Enter") {
        // On affiche la saisie de l'utilisateur dans la zone de dialogue
        var pElt1 = document.createElement("p");
        var form = document.querySelector("form");
        pElt1.textContent = form.elements[1].value;
        $('#dialogue_area').append(pElt1);
        console.log(pElt1.textContent);

        // On interroge l'application via Apache
        // ajaxGet("http://localhost:8888/app_AJAX.py", function (reponse) {
        //     console.log(reponse);
        // }, pElt1.textContent);

    }
});

