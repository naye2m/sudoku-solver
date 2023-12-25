init();
var pSudoku = new URL(window.location.href);
pSudoku = pSudoku.searchParams.get("s");
var res;
if (pSudoku) {
    if (/^\d{81}$/.test(pSudoku)) {
        printResult(pSudoku);
        // window.history.pushState({}, document.title, window.location.origin + window.location.pathname);
    } else {
        alert("S argument is not in correct syntext");
        window.history.pushState({}, document.title, window.location.origin + window.location.pathname);
        // window.location.search = '';
    }
}
// cleaned for not confuse


function printResult(pSudoku) {
    if (/^\d{81}$/.test(pSudoku)) {
        // TODO what will done by calling s as sudoku param
        res = fetch(origin + "/api/ss?sudoku=" + pSudoku).then(r => r.json()).then(r => res = r).then(res => {
            console.log(res);
            var str = "";
            str += `<button type="button" class="btn btn-dark" onclick="document.getElementById('area').innerHTML = '';document.getElementById('input').classList.remove('hide');document.getElementById('selector').classList.add('hide');">Clear Result. And try another one 🙂💖</button>
            <table><tbody>`;
            for (let i = 0; i < 9; i++) {
                str += `<tr>`;
                for (let j = 0; j < 9; j++) {
                    str += `<td><input class="${res.input[i * 9 + j] == '0' ? "ss_yellow" : res.input[i * 9 + j] == res.result[i * 9 + j] ? 'ss_red' : 'ss_green'}" readonly value=${res.result[i * 9 + j]} h="h${res.result[i * 9 + j]}" type="text" id="cellOfResSudokU${i * 9 + j}" ></td>`
                }
                str += `</tr>`
            }
            str += `</tbody></table>`
            document.getElementById('input').classList.toggle('hide');
            document.getElementById("area").innerHTML = str;
            // document.getElementById("cellOfResSudokU0").innerHTML = `<td><input class="${res.input[0] == '0' ? "ss_yellow" : res.input[0] == res.result[0] ? 'ss_red' : "ss_green"}" readonly value=${res.result[0]} type="text" id="cellOfResSudokU${0}" onchange="console.log(this.value);document.getElementById("cellOfResSudokU${i * 9 + j + 1}").focus()"></td>`;
            // document.getElementById("cellOfResSudokU0").innerHTML = `<td><input class="${res.input[0] == '0' ? "ss_yellow" : res.input[0] == res.result[0] ? 'ss_red' : "ss_green"}" readonly value=${res.result[0]} type="text" id="cellOfResSudokU0" onchange="console.log(this.value);document.getElementById("cellOfResSudokU2").focus()"></td>`;
            // document.getElementById("cellOfResSudokU80").innerHTML = `<td><input class="${res.input[80] == '0' ? "ss_yellow" : res.input[80] == res.result[80] ? 'ss_red' : "ss_green"}" readonly value=${res.result[80]} type="text" id="cellOfResSudokU81" onchange="console.log(this.value);"></td>`;
            // document.getElementById("cellOfResSudokU80").setAttribute("onchange", "console.log(this.value);");
            document.getElementById("selector").style.display = '';
            console.log(res);
            animateHighlight(2000);
        })
    } else { alert("Wrong chars only 81digit numeric number acceptable") }
}
var str = "";
str += `<table id="inpTbl"><tbody>`
for (let i = 0; i < 9; i++) {
    str += `<tr>`
    for (let j = 0; j < 9; j++) {
        str += `<td><input data-ani-sirial=${(i * 9 + j) % 10} pattern="[0-9]" value=0 maxlength=1  max=9 min=0 type="text" id="cellOfInpSudokU${i * 9 + j}" onkeyup="stinp();document.getElementById('cellOfInpSudokU${i * 9 + j + 1}').focus()" onkeydown="this.value = ''"></td>`
    }
    str += `</tr>`
}
str += `</tbody></table>`
document.getElementById("area2").innerHTML = str;
document.getElementById("cellOfInpSudokU0").focus();
document.getElementById("cellOfInpSudokU0").setAttribute("onchange", "stinp();document.getElementById('cellOfInpSudokU2').dispatchEvent(new Event('focus'));");
document.getElementById("cellOfInpSudokU80").setAttribute("onchange", "stinp();");
function stinp() {
    let str = "";
    for (let index = 0; index < 81; index++) {
        str += `${document.getElementById("cellOfInpSudokU" + index).value}`;
    }
    console.log(str);
    document.getElementById("s").value = str;
    return str;
}
function inpts() {
    let str = document.getElementById("s").value;
    for (let index = 0; index < 81; index++) {
        let a = ''
        if (str[index]) {
            a = str[index];
        } else {
            a = '0';
        }
        document.getElementById("cellOfInpSudokU" + index).value = a;
    }
}
function fillBoard(timeout = 1000) {
    var elements = document.querySelectorAll('[h]');
    elements.forEach(function(element) {
        element.style.opacity = 0.2;
    });
    var a = timeout / 81;
    for (let i = 0; i < 81; i++) {
        setTimeout(() => {
            elements[i].classList.add('h');
            elements[i].style.opacity = 1;
            setTimeout(() => {
                elements[i].classList.remove('h');
            }, a * 2.5);// a * how many tails
        }, a * i + 50);
    }
    setTimeout(() => {
        highlight(0)
    }, timeout + a * 2.5 + 60);
}
function animateHighlight(timeout = 1000) {
    var elements = document.querySelectorAll('[h]');
    var a = timeout / 81;
    for (let i = 0; i < 81; i++) {
        setTimeout(() => {
            highlight(elements[i].value);
        }, a * i + 50);
    }
    setTimeout(() => {
        highlight(0);
        fillBoard(2000);
    }, timeout + 60);
}
function highlight(n) {
    var elements = document.querySelectorAll('[h]');
    elements.forEach(function(element) {
        element.classList.remove('h');
        element.style.opacity = 1;
    });
    if (n == 0) {
        return;
    }
    elements = document.querySelectorAll('[h]:not([h="h' + n + '"])');
    elements.forEach(function(element) {
        element.classList.remove('h');
        element.style.opacity = 0.3;
    });
    elements = document.querySelectorAll('[h=h' + n + ']');
    elements.forEach(function(element) {
        element.classList.add('h');
    });
}
function init() {
    document.getElementById("selector").style.display = 'none';
}
