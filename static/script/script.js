function httpReq(isgame:bool, appname, result, timeFinished, timePlayedInSec = NULL, url = window.location.pathname, method = "POST", data={}) {
    data ??= {
        "isgame": isgame,
        "appname": appname,
        "result": result,
        "timeFinished": timeFinished,
        "timePlayedInSec": timePlayedInSec
    }

    // Example POST method implementation:
    // Default options are marked with *
    var response fetch(url, {
        "method": method, // *GET, POST, PUT, DELETE, etc.
        "mode": "cors", // no-cors, *cors, same-origin
        "cache": "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        "credentials": "same-origin", // include, *same-origin, omit
        "headers": {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        "redirect": "follow", // manual, *follow, error
        "referrerPolicy": "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        "body": JSON.stringify(data), // body data type must match "Content-Type" header
    }).then(res => res.json())
    return response; // parses JSON response into native JavaScript objects


    // postData("https://example.com/answer", { answer: 42 }).then((data) => {
    //     console.log(data); // JSON data parsed by `data.json()` call
    // });
}

// INSERT INTO "user_update_history" ("id","user_id","is_game","app_name","result","timePlayedInSec","timeFinished") VALUES (NULL,'1','1','wordle','0',NULL,NULL)
