var results = []
//Populate newest games to landing page//

var recentGameUrl = 'https://www.giantbomb.com/api/games/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=jsonp&sort=original_release_date:desc&filter=original_release_date:1700-01-01|2018-12-17&limit=40'

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
    results = games.results;
    games.results.forEach(result => {
        releaseDate= result.original_release_date.split(' ')[0]
        let card1 = `
        <div class= "row gamerow valign-wrapper ">
            <div class="col l3 ">
                <a target="_blank" href="${result.site_detail_url}"><img class="responsive-img" src="${result.image.medium_url}"></a>
            </div>
            <div class="col l6">
                <h5>${result.name}</h5><h6>Released: ${releaseDate}</h6>
                <p>${result.deck}</p>
            </div>
            <div class="col l3 valign-wrapper">
                <ul>
                    <li><a class="${result.id} waves-effect waves-light center-align light-blue darken-4 btn" id='add-current'>Add to Games List</a></li>
                    <li><a class="${result.id} waves-effect waves-light center-align light-blue darken-4 btn" id='add-wish'>Add to Wishlist</a></li>
                </ul>
            </div>
        </div>
        <div class="divider"></div>`
        $('.games').append(card1)
        
    })
}