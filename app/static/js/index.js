function displayMap(lat, lng, zoom) {
        var place = {lat: lat, lng: lng};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: zoom,
          center: place
        });
        var marker = new google.maps.Marker({
          position: place,
          map: map
        });
      }

function initMap() {
        displayMap(0, 0, 2);
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
            displayMap(lat, lng, 17);

            // Affichage de l'anecdote
            summary_message = response['localisation'][5];
            summary = response['localisation'][6];
            if (summary) {
                $(dialogue_area).append(summary_message + summary);
            } else {
                $(dialogue_area).append(summary_message);
            }

            end_message = response['localisation'][7];

            $(dialogue_area).append('<br><br>' + end_message + '<br>');

            $(dialogue_area).scrollTop(100000);
        }

    }).fail(function() {
        // Retrait de l'animation
        $('.loading').remove();

        $(dialogue_area).append('GrandPy : Oh, désolé ! J\'ai un problème d\'accès à ma mémoire ...<br>');

        $(dialogue_area).scrollTop(100000);
    });
}

$(function() {
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

            form.elements[1].value = "";
        };
    });
});

