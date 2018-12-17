$(document).ready(function(){

    var recentGameUrl = 'https://www.giantbomb.com/api/games/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=JSON&sort=original_release_date:desc&filter=original_release_date:1700-01-01%7C2018-12-17&limit=10'

    $.ajax({
        method: 'GET',
        url: recentGameUrl,
        success: handleS
    });

    function handleS(games){
        $('.container').empty();
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
                    <a class="waves-effect waves-light btn">Add to Games List</a>
                    <a class="waves-effect waves-light btn">Add to Wishlist</a>
                </div>
            </div>
            <div class="divider"></div>`
            $('.container').append(card1)
        })
    }

});