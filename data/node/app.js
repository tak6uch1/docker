//======== Express settings ========
let express = require('express'),
    app = express();

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

//======== Postgresql settings ========
let address_list;
let { Client } = require('pg');
let client = new Client({
    user: 'dbuser',
    database: 'mydb',
    password: 'dbpass',
    host: '172.18.0.2',
    port: 5432
});
client.connect();

//======== Routing ========
app.get('/', (req, res) => {
    client.query("SELECT * from address_book")
        .then(res1 => {
            address_list = res1.rows;
            console.log('--------');
            console.log(address_list);
            res.render('index', {posts: address_list});
        })
        .catch(e => console.error(e.stack));
});

app.get('/add/:name', (req, res) => {
    client.query("INSERT INTO address_book (name, address) VALUES ('"
        + req.params.name + "', '" + req.query.address + "')")
        .then(res1 => {
            client.query("SELECT * from address_book")
                .then(res2 => {
                    address_list = res2.rows;
                    console.log('--------');
                    console.log(address_list);
                    res.json(address_list);
                })
                .catch(e => console.error(e.stack));
        })
        .catch(e => console.error(e.stack));
});

app.get('/del/:name', (req, res) => {
    client.query("DELETE FROM address_book WHERE name='"
        + req.params.name + "' AND address='" + req.query.address + "'")
        .then(res1 => {
            client.query("SELECT * from address_book")
                .then(res2 => {
                    address_list = res2.rows;
                    console.log('--------');
                    console.log(address_list);
                    res.json(address_list);
                })
                .catch(e => console.error(e.stack));
        })
        .catch(e => console.error(e.stack));
});

app.listen(3000, () => {
    console.log('server listening...');
});
