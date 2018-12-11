"use strict";

function MapCookie() {
    this.pokestopsHidden = getBooleanCookieValue('pokestopsHidden', true);
    this.gymsHidden = getBooleanCookieValue('gymsHidden', false);
    this.regularPokemonHidden = getBooleanCookieValue('regularPokemonHidden', false);
    this.ivPokemonHidden = getBooleanCookieValue('ivPokemonHidden', false);
    this.mapperHidden = getBooleanCookieValue('mapperHidden', true);
}

MapCookie.prototype.toggleCookieSetting = function (name) {
    this[name] = !this[name];
    setCookie(name, this[name], 365);
    return this[name]
};

function setCheckboxes () {
    var checkboxes = $( "input:checkbox" );
    for (var checkbox in checkboxes) {
        if (checkboxes.hasOwnProperty(checkbox)) {
            var cb = checkboxes[checkbox];
            if (cb.tagName === 'INPUT') {
                var cb_bool = mapCookie[cb.name];
                $(cb).attr( {checked: (!cb_bool)});
                $(cb).prop( {checked: (!cb_bool)});
            }
        }
    }

}

var mapCookie = new MapCookie();
console.log(mapCookie)
setCheckboxes();

var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

var pokedex = undefined;
$.getJSON('/api/pokedex/', function (data) {
    pokedex = data;
});

var getPokemonData = function () {
    $.getJSON("/api/pokemon/spawns", function(data) {
        addPokemonToMap(data)
    });
};

var getPointOfInterestData = function() {
    $.getJSON("/api/poi/all", function (data) {
        addPointOfInterestToMap(data);
    });
};

var getMapperData = function() {
    $.getJSON("/api/mapper", function (data) {
        addMapperToMap(data);
    });
};


var togglePokestops = function() {
    var pokestopsHidden = mapCookie.toggleCookieSetting('pokestopsHidden');
    toggleMapLayer(pokestopLayer, pokestopsHidden);
};

var toggleGyms = function() {
    var gymsHidden = mapCookie.toggleCookieSetting('gymsHidden');
    toggleMapLayer(gymLayer, gymsHidden);
};

var toggleIVPokemon = function() {
    var ivPokemonHidden = mapCookie.toggleCookieSetting('ivPokemonHidden');
    toggleMapLayer(ivPokemonLayer, ivPokemonHidden);
};

var toggleRegularPokemon = function() {
    var regularPokemonHidden = mapCookie.toggleCookieSetting('regularPokemonHidden');
    toggleMapLayer(regularPokemonLayer, regularPokemonHidden);
};

var toggleMapper = function() {
    var mapperHidden = mapCookie.toggleCookieSetting('mapperHidden');
    toggleMapLayer(mapperLayer, mapperHidden);
};


var update_time = function() {
    var date = new Date();
    return date.getTime();
};

var last_update = 0;
var loading_data = false;

function reloadData(model) {
        // if pokestop not yet loaded or another pokemon update is not long ago, wait a sec
        if (!loading_data) {
            if (pokedex === undefined) {
                setTimeout(function () {
                    reloadData()
                }, 200);
                return
            }
            loading_data = true;
            last_update = update_time();
            if (model === "PokemonSpawn") {
                getPokemonData();
            }
            else if (model === "PointOfInterest") {
                getPointOfInterestData();
            }
            else if (model === "Mapper") {
                getMapperData();
            }
            else if (model === "Quest") {
                getQuestInfo();
            }
            else {
                getPointOfInterestData();
                getPokemonData();
                getMapperData();
                getQuestInfo()
            }
            setTimeout(function () {
                loading_data = false;
            }, 2000);
        }
}

var websocket_protocol = 'ws://';
if (location.protocol === 'https:') {
    websocket_protocol = 'wss://'
}

var updateSocket = new ReconnectingWebSocket(
websocket_protocol + window.location.host +
'/ws/update/');

updateSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    console.log(data);
    if (data.type === 'change') {
        reloadData(data.model)
    }
};

reloadData();

$( function() {
    $( "#datepicker" ).datepicker();
} );