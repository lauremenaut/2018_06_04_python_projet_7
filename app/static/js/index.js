$('#dialogue_area').append('GrandPy : Bonjour mon petit, as-tu une question pour moi ?<br>');


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

        error = response['localisation'][0];
        message = response['localisation'][1];

        if (error) {
            $(dialogue_area).append(message + '<br>');
            $(dialogue_area).scrollTop(100000);
        } else {

            // Affichage de l'adresse
            address = response['localisation'][2];
            $(dialogue_area).append(message + address + '.<br><br>');

            // Insertion de la carte
            lat = response['localisation'][3];
            lng = response['localisation'][4];
            initMap(lat, lng);

            // Affichage de l'anecdote
            summary = response['localisation'][5];
            if (summary) {
                $(dialogue_area).append('GrandPy : En parlant de ça, j\'avais une petite chose à te raconter ... ' + summary);
            } else {
                $(dialogue_area).append('GrandPy : Par contre, c\'est bien un des rares endroits au sujet duquel je n\'ai rien à raconter ;-) !');
            }

            $(dialogue_area).append('<br><br>GrandPy : As-tu autre chose à me demander ?<br>');

            // Récupérer la hauteur de l'élément 'dialogue_Area'
            height = $(dialogue_area).height();
            // console.log('Heigth = ' + height)

            $(dialogue_area).scrollTop(100000);
            // $(dialogue_area).scrollTop(height);

        }

    }).fail(function() {
        // Retrait de l'animation
        $('.loading').remove();

        $(dialogue_area).append('GrandPy : Oh, désolé ! J\'ai un problème d\'accès à ma mémoire ...');

        $(dialogue_area).scrollTop(100000);
    });
}

document.addEventListener("keypress", function(e) {

    var form = document.querySelector("form"); // Champ de saisie
    var query = form.elements[1].value; // Contenu du champ de saisie (= saisie de l'utilisateur)

    if (e.key == "Enter") {
        // On affiche la saisie de l'utilisateur dans la zone de dialogue
        var divElt = document.createElement("div");
        divElt.textContent = 'Vous : ' + query;
        $('#dialogue_area').append('<br>');
        $('#dialogue_area').append(divElt);
        $('#dialogue_area').append('<br>');

        locate(
            query,
            '#dialogue_area'
            );

        form.elements[1].value = "";  // Est-ce une bonne façon de vider le champ de saisie ??
    };
});
