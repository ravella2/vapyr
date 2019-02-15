# Vapyr
A web-based application that lets users create a list of games they're currently playing, as well as a wishlist for future games. Made using Materialize, Django and utilizes Giantbomb's API for the game data.

## User Stories

### Landing Page
Displays list of most recently released games from Giantbomb API
On Sign In
Brings you back to landing page, but now populates from API based on user’s preferred platform (PS4, Switch, etc.)
### Profile Page
Shows list of currently playing games as well as a game wishlist.
### Add Game
On click of button, form collects info from API and saves it to our DB, and then populates the game in the user’s list.

## Challenges and Triumphs
Requesting information from the Giantbomb API was a little tricky at first. We kept getting CORS issues and data that wasn't displaying correctly when we requested it. However, with the help of our instructors we figured out that we needed to request the data in JSONP format instead of JSON and make a callback request when saving the data to our own database. 

```javascript
    $('.search').on('submit', function(e){
        e.preventDefault();

        let gameSearch = $('#search').val();
        let gameUrl = `https://www.giantbomb.com/api/search/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=jsonp&resources=game&query=${gameSearch}&limit=20`

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
                if (result.original_release_date){
                releaseDate= result.original_release_date.split(' ')[0]}
```

I also learned how to use Materialize as a front-end library for this project, which made some aspects of the project easier. In projects before this one, I had only used plain HTML and CSS. 
