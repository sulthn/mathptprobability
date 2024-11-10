// Player logic

let player1 = {};
let player2 = {};
let player3 = {};
let player4 = {};
window.players = [player1, player2, player3, player4];

// Game
window.game = {};


function update_table() {
    const header = document.getElementById('header');
    const tbody = document.getElementById('tbody');

    header.innerHTML = "";

    Object.keys(window.players[0]).forEach(key => {
        header.innerHTML += `<th>${key}</th>`;
    });

    tbody.innerHTML = "";

    for (let i = 0; i < window.players.length; i++) {
        const tr = document.createElement('tr');
        tr.innerHTML += '<td>' + window.players[i].Player + '</td>';
        tr.innerHTML += '<td class="points">' + window.players[i].Points + '</td>';

        tbody.append(tr);
    }
}

const setup_html = '<h1 class="center vazirmatn-font" style="margin:0;">Setup</h1> <table class="point-table vazirmatn-font" style="width: 30%;"> <thead> <tr> <th>Player</th> <th>Points</th> </tr> </thead> <tbody id="tbody"> <tr> <td class="td-textbox"> <input class="table-textbox" type="text" id="p1-name"> </td> <td class="td-textbox"> <input class="table-textbox" type="number" id="p1-point" min=0 value=0> </td> </tr> <tr> <td class="td-textbox"> <input class="table-textbox" type="text" id="p2-name"> </td> <td class="td-textbox"> <input class="table-textbox" type="number" id="p2-point" min=0 value=0> </td> </tr> <tr> <td class="td-textbox"> <input class="table-textbox" type="text" id="p3-name"> </td> <td class="td-textbox"> <input class="table-textbox" type="number" id="p3-point" min=0 value=0> </td> </tr> <tr> <td class="td-textbox"> <input class="table-textbox" type="text" id="p4-name"> </td> <td class="td-textbox"> <input class="table-textbox" type="number" id="p4-point" min=0 value=0> </td> </tr> </tbody> </table> <div> <label class="vazirmatn-font">Current Round: </label><input style=" margin: 0px 0px 10px 0px;" type="number" id="rounds-count" min=1 value=1> </div> <input type="button" onclick="play()" value="OK">'
function setup() {
    const inner_window = document.getElementById('inner-window');

    inner_window.style = "align-items: center; justify-content: center; flex-direction: column;";

    inner_window.innerHTML = setup_html;
}

function play() {
    const inner_window = document.getElementById('inner-window');
    const names  = [document.getElementById('p1-name'), document.getElementById('p2-name'), document.getElementById('p3-name'), document.getElementById('p4-name')]
    const points = [document.getElementById('p1-point'), document.getElementById('p2-point'), document.getElementById('p3-point'), document.getElementById('p4-point')]
    const current_round = document.getElementById('rounds-count');

    for (let p = 0; p < names.length; p++) {
        if (names[p].value == "") {
            window.players[p].Player = "Player " + (p + 1);
        }
        else {
            window.players[p].Player = names[p].value;
        }

        if (points[p].value == "") {
            window.players[p].Points = 0;
        }
        else {
            window.players[p].Points = points[p].value;
        }
    }

    window.game.round = current_round.value;

    document.getElementById('round').innerHTML = window.game.round;

    update_table();

    inner_window.style = "";

    inner_window.innerHTML = "";
}

document.addEventListener("DOMContentLoaded", function(event) {
    for (let i = 0; i < players.length; i++) {
        window.players[i].Player = "Player " + (i + 1);
        window.players[i].Points = 0;
    }

    window.game.round = 0;

    update_table();
    setup();
});