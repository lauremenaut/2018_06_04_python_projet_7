$('#dialogue_area').append('<br>GrandPy : Bonjour mon petit, as-tu une question pour moi ?<br>');


function initMap(lat, lng) {
        var place = {lat: lat, lng: lng};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 17,
          center: place
        });
        var marker = new google.maps.Marker({
          position: place,
          map: map
        });
      }

function locate(query, dialogue_area) {
    // Ajout de l'animation pendant que "GrandPy réfléchit"
    $(dialogue_area).append("<img src='../static/img/loading_mini.gif' alt='loading' class='loading' />");

    $.post('/locate', {
        query: query
    }).done(function(response) {
        // Retrait de l'animation
        $('.loading').remove();

        // Affichage de l'adresse
        address = response['localisation'][0];
        $(dialogue_area).append('GrandPy : Hum ... oh oui, je me souviens ! Tu trouveras ça au ' + address + '.<br><br>');

        // Insertion de la carte
        lat = response['localisation'][1];
        lng = response['localisation'][2];
        initMap(lat, lng);

        // Affichage de l'anecdote
        summary = response['localisation'][3];
        $(dialogue_area).append('GrandPy : En parlant de ça, j\'avais une petite chose à te raconter ... ' + summary);
        $(dialogue_area).append('<br><br>GrandPy : As-tu autre chose à me demander ?<br>');
    }).fail(function() {
        $(dialogue_area.append('Ça, je ne m\'en souviens plus ...'));
    });
}

document.addEventListener("keypress", function(e) {

    var form = document.querySelector("form"); // Champ de saisie
    var query = form.elements[1].value; // Contenu du champ de saisie (= saisie de l'utilisateur)

    if (e.key == "Enter") {
        // On affiche la saisie de l'utilisateur dans la zone de dialogue
        var pElt = document.createElement("p");
        pElt.textContent = 'Vous : ' + query;
        $('#dialogue_area').append(pElt);

        locate(
            query,
            '#dialogue_area'
            );

        form.elements[1].value = "";  // Est-ce une bonne façon de vider le champ de saisie ??
    };
});
