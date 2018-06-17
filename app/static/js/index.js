$('#dialogue_area').append("<br>Bonjour mon petit, as-tu une question pour moi ?<br>")

var form = document.querySelector("form"); // Champ de saisie
var query = form.elements[1].value; // Contenu du champ de saisie (= saisie de l'utilisateur)


function locate(sourceElt, destElt) {
// Ajouter le .gif quand GrandPy réfléchit
    $.post('/locate', {
        // query: $(sourceElt).text() Pourquoi ça ne fonctionne pas ?
        query: query
    }).done(function(response) {
        $(destElt).append('Oh oui, je connais ! Tu trouveras ça au ' + response['localisation'][0] + '.<br>')
        $(destElt).append('En parlant de ça, j\'avais une petite chose à te raconter ... ' + response['localisation'][1])
    }).fail(function() {
        $(destElt.text("Ça, je ne m'en souviens plus ..."))
    });
}

document.addEventListener("keypress", function(e) {
    if (e.key == "Enter") {
        // On affiche la saisie de l'utilisateur dans la zone de dialogue
        var pElt1 = document.createElement("p");
        pElt1.textContent = query;
        $('#dialogue_area').append(pElt1);

        locate(
            'query',
            '#dialogue_area'
            )
    }
});

// Vider le champ de recherche au démarrage
// Ajouter une boucle
// Ajouter le nom de celui qui parle
// Ajouter un ascenseur quand le contenu dépasse la taille de la zone de dialogue
