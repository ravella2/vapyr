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
            <div class= "row gamerow valign-wrapper ">
                <div class="col l3 ">
                    <img class="responsive-img" src="${result.image.screen_url}">
                </div>
                <div class="col l6">
                    <h5>${result.name}</h5>
                    <p>${result.deck}</p>
                </div>
                <div class="col l3 valign-wrapper">
                    <ul>
                    <li><a class="waves-effect waves-light center-align grey btn">Add to Games List</a></li>
                    <li><a class="waves-effect waves-light center-align grey btn">Add to Wishlist</a></li>
                </div>
            </div>
            <div class="divider"></div>`
            $('.games').append(card1)
        })
    }

});