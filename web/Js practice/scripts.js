function change() {
    var body = document.getElementsByTagName('body')[0];
    if (body.style.backgroundColor == 'blue') {
        body.style.backgroundColor = 'white';
    } else {
        body.style.backgroundColor = 'blue';
    }
}

function colorChange() {
    document.getElementsByTagName('p')[1].innerHTML = 'Try this!';
}

function tryi(id, nameOf) {
    nameOf.textContent = 'Hello!';
}