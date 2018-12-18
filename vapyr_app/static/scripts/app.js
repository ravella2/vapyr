$(document).ready(function(){

    var recentGameUrl = 'https://www.giantbomb.com/api/games/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=jsonp&sort=original_release_date:desc&filter=original_release_date:1700-01-01|2018-12-17&limit=10'

    $.ajax({
        method: 'GET',
        url: recentGameUrl,
        success: handleS,
        dataType: 'jsonp',
        jsonp: 'json_callback',
        crossDomain: true,
    });


    function handleS(games){
        $('.games').empty();
        games.results.forEach(result => {
            let card1 = `
            <div class= "row">
                <div class="col l3">
                    <img class="responsive-img" src="${result.image.screen_url}">
                </div>
                <div class="col l6">
                    <h5>${result.name}</h5>
                    <p>${result.deck}</p>
                </div>
                <div class="col l3">
                    <a class="waves-effect waves-light btn" id='add-current'>Add to Games List</a>
                    <a class="waves-effect waves-light btn add-wish">Add to Wishlist</a>
                </div>
            </div>
            <div class="divider"></div>`
            $('.games').append(card1)
        })
    }

    $('.games').one('click','#add-current', function(e){
        e.preventDefault();
        let gameData = $(this).data()

        console.log(gameData)

    });


    $('form').on('submit', function(e){
        e.preventDefault();

        let gameSearch = $('#search').val();
        let gameUrl = `https://www.giantbomb.com/api/search/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=jsonp&resources=game&query=${gameSearch}`

        $.ajax({
            method:'GET',
            url: gameUrl,
            success: onSuccess,
            dataType: 'jsonp',
            jsonp: 'json_callback',
            crossDomain: true,
        })

        function onSuccess(games) {
            $('.games').empty();
            games.results.forEach(result => {
                let card1 = `
                <div class= "row">
                    <div class="col l3">
                        <img class="responsive-img" src="${result.image.screen_url}">
                    </div>
                    <div class="col l6">
                        <h5>${result.name}</h5>
                        <p>${result.deck}</p>
                    </div>
                    <div class="col l3">
                        <a class="waves-effect waves-light btn" id='add-current'>Add to Games List</a>
                        <a class="waves-effect waves-light btn add-wish">Add to Wishlist</a>
                    </div>
                </div>
                <div class="divider"></div>`
                $('.games').append(card1)
            })

        }
    })
});