$(document).ready(function() {
    var counter = 0;
    $("#get_card").on('click', function() {
//            while (counter <= 26) {
//                counter = +1;
//                getCard();
//                console.log(counter);
//            };
        });

        var getCard = function () {
            $.ajax({
                url: '/get_card',
                type: "GET",
                success: function (data) {
                    $("#player").html("<p>Your card: " + data.user_card + "</p><br><p>Dealers Card: " + data.dealer_card + "</p>");
                    console.log(data);

                }
            })
        }

        });

