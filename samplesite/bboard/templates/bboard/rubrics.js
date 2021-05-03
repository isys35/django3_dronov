const domain = 'http://127.0.0.1:8000/';

let list = document.getElementById('list');
let listLoader = new XMLHttpRequest();

listLoader.addEventListener('readystatechange', () => {
    if (listLoader.readyState == 4) {
        if (listLoader.status == 200) {
            let data = JSON.parse(listLoader.responseText);
            let s = '<ul>', d;
            for (let  i=0; i<data.length; i++){
                d = data[i];
                s += '<li>' + d.name + ' <a href="'+ domain+ 'api/rubrics/' + d.id + '/" class="detail">Вывести</a> <a href="'+ domain + 'api/rubrics/' + d.id + '/" class="delete">Удалить</a></li>' ;
            }
            s += '</ul>';
            list.innerHTML = s;
            let links = list.querySelectorAll('ul li a.detail')
            links.forEach((link) => {link.addEventListener('click', rubricLoad)})
            links = list.querySelectorAll('ul li a.delete')
            links.forEach((link) => {link.addEventListener('click', rubricDelete)})
        } else
            window.alert(listLoader.statusText);

    }
});

function listLoad() {
    listLoader.open('GET', domain + 'api/rubrics/', true);
    listLoader.send();
}

listLoad();

let id = document.getElementById('id');
let name = document.getElementById('name');
let rubricLoader = new XMLHttpRequest();

rubricLoader.addEventListener('readystatechange', () => {
    if (rubricLoader.readyState == 4) {
        if (rubricLoader.status == 200) {
            let data = JSON.parse(rubricLoader.responseText);
            id.value = data.id;
            name.value = data.name;}
            } else
                {window.alert(rubricLoader.statusText);}
            });

function rubricLoad(evt) {
    evt.preventDefault();
    rubricLoader.open('GET', evt.target.href, true);
    rubricLoader.send();
}

let rubricUpdater = new XMLHttpRequest();
rubricUpdater.addEventListener('readystatechange', () => {
    if (rubricUpdater.readyState == 4) {
        if ((rubricUpdater.status == 200) ||
            (rubricUpdater.status == 201)) {
            listLoad();
            name.form.reset();
            id.value = '';
        } else
            window.alert(rubricUpdater.statusText);
    }
        });

name.form.addEventListener('submit', (evt) => {
    evt.preventDefault();
    let vid = id.value, url, method;
    if (vid) {
        url = 'api/rubrics/' + vid + '/';
        method = 'PUT';
        } else {
            url = 'api/rubrics/';
            method = 'POST';
        }
    let data = JSON.stringify({id: vid, name: name.value});
    rubricUpdater.open(method, domain + url, true);
    rubricUpdater.setRequestHeader('Content-Type', 'application/json');
    rubricUpdater.send(data);
});


let rubricDeleter = new XMLHttpRequest();
rubricDeleter.addEventListener('readystatechange', () => {
    if (rubricDeleter.readyState == 4) {
        if (rubricDeleter.status == 204)
            listLoad();
        else
            window.alert(rubricDeleter.statusText);
    }
});

function rubricDelete(evt) {
    evt.preventDefault();
    rubricDeleter.open('DELETE', evt.target.href, true);
    rubricDeleter.send();
}