var results = []
$(document).ready(function(){


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
                    <a target="_blank" href="${result.site_detail_url}"><img class="responsive-img" src="${result.image.screen_url}"></a>
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
            results = games.results;
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
                        <a class="${result.id} waves-effect waves-light btn" id='add-current'>Add to Games List</a>
                        <a class="${result.id} waves-effect waves-light btn" id='add-wish'>Add to Wishlist</a>
                    </div>
                </div>
                <div class="divider"></div>`
                $('.games').append(card1)
            })

        }
    })

    //Add game to user's currently playing list//
    $('.games').on('click','#add-current', function(e){
        e.preventDefault();
        let gameData = this.className.split(" ");
        
        var gameObj = results.find(result => {
            return result.id==gameData[0]
        })

        let gameModel = {
            "title": gameObj.name,
            "image": gameObj.image.screen_url,
            "platform": gameObj.platforms[0].name,
            "genre": "Unknown",
            "description": gameObj.deck,
            "rating":0,
        }

        console.log(gameModel);

        $.ajax({
            method: 'POST',
            url: 'game/create',
            data: gameModel,
            success: onSuccess,
        })

        function onSuccess(response) {
            console.log(response);
            if(response){
                window.location.href = 'user/'+response; 
            }
            else{
                window.location.href = '/'
            }
        }
    });

    //Add game to user's wishlist//
    $('.games').on('click', '#add-wish', function(e) {
        e.preventDefault();
        let gameData = this.className.split(" ");
        
        var gameObj = results.find(result => {
            return result.id==gameData[0]
        })

        let gameModel = {
            "title": gameObj.name,
            "image": gameObj.image.screen_url,
            "platform": gameObj.platforms[0].name,
            "genre": "Unknown",
            "description": gameObj.deck,
            "rating":0,
        }

        $.ajax({
            method: 'POST',
            url: 'game/wish',
            data: gameModel,
            success: onSuccess,
        })

        function onSuccess(response) {
            console.log(response);
            if(response){
                window.location.href = 'user/'+response; 
            }
            else{
                window.location.href = '/'
            }
        }
    })


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
});
