fetch("/history_ss_api")
    .then(response => response.json())
    .then(response => response["massage"])
    .then(res => {
        if (res.length == 0) {
            let node = document.createElement("div");
            node.classList.add('items');
            node.innerHTML = 'No search History';
            document.getElementById("con").appendChild(node);
            return;
        };
        let str = '';
        for (let i = 0; i < res.length; i++) {
            // let node = document.createElement("div").classList.add('items');
            // node.innerHtml = printItem(res[i])
            // document.getElementById("con").appendChild(node);
            console.log(res[i])
            let node = document.createElement("div");
            node.classList.add('items');
            node.innerHTML = printItem(res[i]);
            document.getElementById("con").appendChild(node);
        }

    })
    .catch(e => console.log(e.massege))
    .finally(console.log('end'))

function printItem(item) {
    return `<table><tbody><tr><td class="time">time &nbsp;</td><td>: ${item[2].substring(11)} </td></tr>
    <tr><td class="date">date &nbsp;</td><td>: ${item[2].substring(0, 10)}</td></tr>
    <tr><td class="comp">complexity &nbsp; </td><td>: ${item[3]}</td></tr></tbody></table><hr >
    <div class="sudoku">${printBlock(item[0], item[1])}</div>`
}

function printBlock(...res) {
    let str = "";
    if (/^\d{81}$/.test(res[0]) && /^\d{81}$/.test(res[1])) {
        // TODO what will done by calling s as sudoku param
        // res = fetch(origin + "/api/ss?sudoku=" + pSudoku).then(r => r.json()).then(r => res = r).then(res => {
        // console.log(res);
        str = "<table><tbody>";
        // str += ``;
        for (let i = 0; i < 9; i++) {
            str += `<tr>`;
            for (let j = 0; j < 9; j++) {
                str += `<td class="${res[0][i * 9 + j] == '0' ? "ss_yellow" : res[0][i * 9 + j] == res[1][i * 9 + j] ? 'ss_red' : 'ss_green'}" readonly  h="h${res[1][i * 9 + j]}" type="text" id="cellOfResSudokU${i * 9 + j}" >${res[1][i * 9 + j]}</td>`
            }
            str += `</tr>`
        }
        str += `</tbody></table>`
        // })
    } else { return "Wrong chars only 81digit numeric number acceptable" }
    return str;
}
