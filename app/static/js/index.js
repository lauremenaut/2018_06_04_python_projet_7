// displayMap() is a function displaying a map from Google Maps.
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

// initMap() function is called in the script section at the end of
// index.html template as a callback method
function initMap() {
        displayMap(0, 0, 2);
      }

// locate() function send 'query' through '/locate' route to get back a
// json object containing 'location' data
function locate(query, dialogue_area) {
    // Display loading animation while process is on going
    $(dialogue_area).append("<img src='../static/img/loading_mini.gif' \
alt='loading' class='loading' />");

    $.post('/locate', {
        query: query
    }).done(function(response) {
        // Remove loading animation
        $('.loading').remove();

        error = response['location'][0];
        message = response['location'][1];

        if (error) {
            // Display failure message
            $(dialogue_area).append(message + '<br>');
            // Force the scrollbar to go down
            $(dialogue_area).scrollTop(100000);
        } else {

            // Display success message and address
            address = response['location'][2];
            $(dialogue_area).append(message + address + '.<br><br>');

            // Display map
            lat = response['location'][3];
            lng = response['location'][4];
            displayMap(lat, lng, 17);

            // Display more information about the place
            summary_message = response['location'][5];
            summary = response['location'][6];
            if (summary) {
                // Display success message and summary
                $(dialogue_area).append(summary_message + summary);
            } else {
                // Display failure message
                $(dialogue_area).append(summary_message);
            }

            // Display a message suggesting to ask a new question
            next_question_message = response['location'][7];
            $(dialogue_area).append(
                '<br><br>' + next_question_message + '<br>');
            $(dialogue_area).scrollTop(100000);
        }

    }).fail(function() {
        // Remove loading animation
        $('.loading').remove();

        // Display failure message
        $(dialogue_area).append('GrandPy : Oh, désolé ! J\'ai un problème \
d\'accès à ma mémoire ...<br>');
        $(dialogue_area).scrollTop(100000);
    });
}

$(function() {
    $('#query').keypress(function(e){
        // 13 is key code for 'Enter' key
        if (e.which == 13) {
            // 'query' is the user input in query field
            var query = $('#query').val();

            // Display user input in dialogue area
            $('<br>').appendTo($('#dialogue_area'));
            $('<div class="user_query"></div>').appendTo($('#dialogue_area'));
            $('.user_query:last-child').text('Vous : ' + query);
            $('<br>').appendTo($('#dialogue_area'));

            // Clear the input field
            $('#query').val("");

            // Call locate() function to display GrandPy answer
            locate(
                query,
                '#dialogue_area'
                );
        };
    });
});

