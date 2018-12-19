
$(document).ready(function(){

    var recentGameUrl = 'https://www.giantbomb.com/api/games/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=jsonp&sort=original_release_date:desc&filter=original_release_date:1700-01-01|2018-12-17&limit=50'

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
        console.log(games.results);
        games.results.forEach(result => {
            releaseDate= result.original_release_date.split(' ')[0]
            let card1 = `
            <div class= "row gamerow valign-wrapper ">
                <div class="col l3 ">
                    <a target="_blank" href="${result.site_detail_url}"><img class="responsive-img" src="${result.image.screen_url}"></a>
                </div>
                <div class="col l6">
                    <h5>${result.name}</h5><h6>Released: ${releaseDate}</h6>
                    <p>${result.deck}</p>
                </div>
                <div class="col l3 valign-wrapper">
                    <ul>
                    <li><a class="waves-effect waves-light center-align light-blue darken-4 btn">Add to Games List</a></li>
                    <li><a class="waves-effect waves-light center-align light-blue darken-4 btn">Add to Wishlist</a></li>
                    </ul>
                </div>
            </div>
            <div class="divider"></div>`
            $('.games').append(card1)
            
        })
    }




    
});
$('.addToWishList').on('click', function(e) {
    console.log('clicked move game button on', $(this).attr('data-id'));
    let game = $(this).attr('data-id')
    
    e.preventDefault();
    $.ajax({
        method: 'GET',
        url: '/move_game',
        data: {game_id: game}

        })
    })